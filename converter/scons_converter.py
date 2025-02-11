import os
import re
from dataclasses import dataclass
from typing import List, Dict, Set, Optional, Tuple
from pathlib import Path
import ast
import logging

@dataclass
class BuildTarget:
    name: str
    sources: List[str]
    includes: List[str]
    libraries: List[str]
    definitions: List[str]
    dependencies: List[str]
    type: str  # 'executable', 'static_library', 'shared_library'

class SConsConverter:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.processed_files: Set[str] = set()
        self.cmake_minimum = "3.12"
        self.project_name = os.path.basename(root_dir)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("SConsConverter")
        self.found_variables = set()
        self.custom_methods = set()

    def parse_scons_file(self, file_path: Path) -> Dict:
        """Parse a SConstruct/SConscript file and extract relevant information."""
        self.logger.info(f"Parsing SCons file: {file_path}")
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            self.logger.error(f"Failed to parse {file_path}: {e}")
            return {}

        build_info = {
            'targets': [],
            'env_settings': {},
            'dependencies': [],
            'includes': [],
            'libraries': [],
            'definitions': [],
            'source_files': [],
            'custom_vars': {},
            'custom_methods': set(),
            'platforms': set(),
            'options': []
        }

        self._extract_godot_specific_info(tree, build_info)
        
        # Walk through the AST to extract information
        for node in ast.walk(tree):
            self._process_node(node, build_info)

        return build_info

    def _extract_godot_specific_info(self, tree: ast.AST, build_info: Dict):
        """Extract Godot-specific build information."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                # Look for common Godot build variables
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        if var_name in ['opts', 'env', 'targets']:
                            build_info['custom_vars'][var_name] = self._extract_value(node.value)
            
            elif isinstance(node, ast.Call):
                # Look for Godot's custom builders and methods
                if isinstance(node.func, ast.Name):
                    method_name = node.func.id
                    if method_name in ['add_source_files', 'add_sources', 'configure']:
                        build_info['custom_methods'].add(method_name)

    def _process_node(self, node: ast.AST, build_info: Dict):
        """Process an AST node to extract build information."""
        if isinstance(node, ast.Call):
            self._process_call_node(node, build_info)
        elif isinstance(node, ast.Assign):
            self._process_assign_node(node, build_info)
        elif isinstance(node, ast.FunctionDef):
            self._process_function_node(node, build_info)

    def _process_assign_node(self, node: ast.Assign, build_info: Dict):
        """Process assignment nodes to extract variables."""
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id
                self.found_variables.add(var_name)
                if var_name in ['CCFLAGS', 'CXXFLAGS', 'LINKFLAGS']:
                    value = self._extract_value(node.value)
                    build_info['env_settings'][var_name] = value

    def _extract_value(self, node: ast.AST) -> any:
        """Extract value from an AST node."""
        if isinstance(node, ast.Constant):
            return node.value
        elif isinstance(node, ast.List):
            return [self._extract_value(elt) for elt in node.elts]
        elif isinstance(node, ast.Dict):
            return {
                self._extract_value(k): self._extract_value(v)
                for k, v in zip(node.keys, node.values)
            }
        elif isinstance(node, ast.Name):
            return f"${node.id}"
        return str(node)

    def generate_cmake_file(self, build_info: Dict, output_path: Path):
        """Generate CMakeLists.txt from parsed build information."""
        self.logger.info(f"Generating CMake file: {output_path}")
        
        cmake_contents = []
        
        # Add header
        cmake_contents.extend([
            f"cmake_minimum_required(VERSION {self.cmake_minimum})",
            f"project({self.project_name})\n",
            "# Generated from SCons build system\n"
        ])

        # Add Godot-specific settings
        if 'custom_vars' in build_info and build_info['custom_vars']:
            cmake_contents.append("# Godot build settings")
            self._add_godot_settings(build_info, cmake_contents)

        # Add platform-specific settings
        if build_info['platforms']:
            cmake_contents.append("\n# Platform-specific settings")
            self._add_platform_settings(build_info, cmake_contents)

        # Add build options
        if build_info['options']:
            cmake_contents.append("\n# Build options")
            self._add_build_options(build_info, cmake_contents)

        # Add dependencies
        if build_info['dependencies']:
            cmake_contents.append("\n# Dependencies")
            for dep in build_info['dependencies']:
                # Convert SCons path to CMake path
                dep_path = self._convert_path_to_cmake(dep)
                cmake_contents.append(f"add_subdirectory({dep_path})")

        # Add targets
        for target in build_info['targets']:
            cmake_contents.extend(self._generate_target_cmake(target))

        # Write the file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w') as f:
            f.write('\n'.join(cmake_contents))

    def _convert_path_to_cmake(self, path: str) -> str:
        """Convert SCons path to CMake path format."""
        # Remove ./ prefix if present
        if path.startswith('./'):
            path = path[2:]
        # Remove SConstruct/SConscript suffix if present
        if path.endswith('/SConstruct') or path.endswith('/SConscript'):
            path = os.path.dirname(path)
        return path

    def _add_godot_settings(self, build_info: Dict, cmake_contents: List[str]):
        """Add Godot-specific build settings."""
        cmake_contents.extend([
            "# Godot build configuration",
            "option(TOOLS \"Build with tools\" ON)",
            "option(TARGET_PLATFORM \"Target platform\" \"\")",
            "option(PLATFORM \"Build platform\" ${CMAKE_SYSTEM_NAME})",
            ""
        ])

    def _add_platform_settings(self, build_info: Dict, cmake_contents: List[str]):
        """Add platform-specific settings."""
        cmake_contents.append("if(${CMAKE_SYSTEM_NAME} STREQUAL \"Windows\")")
        cmake_contents.append("    add_definitions(-DWINDOWS_ENABLED)")
        cmake_contents.append("elseif(${CMAKE_SYSTEM_NAME} STREQUAL \"Linux\")")
        cmake_contents.append("    add_definitions(-DUNIX_ENABLED -DLINUX_ENABLED)")
        cmake_contents.append("elseif(${CMAKE_SYSTEM_NAME} STREQUAL \"Darwin\")")
        cmake_contents.append("    add_definitions(-DUNIX_ENABLED -DAPPLE_ENABLED)")
        cmake_contents.append("endif()")
        cmake_contents.append("")

    def _add_build_options(self, build_info: Dict, cmake_contents: List[str]):
        """Add build options from SCons."""
        for opt in build_info['options']:
            cmake_contents.append(f"option({opt['name']} \"{opt.get('help', '')}\" {opt.get('default', 'OFF')})")
        cmake_contents.append("")

    def convert_project(self):
        """Convert entire SCons project to CMake."""
        self.logger.info("Starting project conversion")

        # Find all SCons files
        scons_files = []
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if file in ['SConstruct', 'SConscript']:
                    scons_files.append(Path(root) / file)

        # Process each file
        for scons_file in scons_files:
            if scons_file in self.processed_files:
                continue

            self.logger.info(f"Processing {scons_file}")
            
            # Parse SCons file
            build_info = self.parse_scons_file(scons_file)
            
            # Generate CMakeLists.txt in same directory
            cmake_path = scons_file.parent / 'CMakeLists.txt'
            self.generate_cmake_file(build_info, cmake_path)
            
            self.processed_files.add(scons_file)

        self.logger.info("Project conversion completed")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Convert SCons build system to CMake')
    parser.add_argument('project_root', help='Root directory of the SCons project')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose output')
    parser.add_argument('--godot', '-g', action='store_true', help='Enable Godot-specific processing')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger("SConsConverter").setLevel(logging.DEBUG)
    
    converter = SConsConverter(args.project_root)
    converter.convert_project()

if __name__ == '__main__':
    main()