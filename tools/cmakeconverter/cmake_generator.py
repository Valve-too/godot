"""CMake generator module for SCons to CMake converter"""
from typing import Any, Dict, List, Optional, Union

class CMakeGenerator:
    """CMake generator class"""
    def __init__(self) -> None:
        self.cmake_minimum_version = "3.20"
        self.project_name = "godot"
        self.project_version = "4.4.0"
        self.project_languages = ["C", "CXX"]
        self.variables = {}
        self.targets = {}
        self.dependencies = {}
        self.options = {}

    def add_variable(self, name: str, value: Any, type: str = None) -> None:
        """Add CMake variable"""
        self.variables[name] = {
            "value": value,
            "type": type
        }

    def add_target(self, name: str, type: str, sources: List[str], includes: List[str] = None, 
                  defines: List[str] = None, options: Dict[str, Any] = None) -> None:
        """Add CMake target"""
        self.targets[name] = {
            "type": type,
            "sources": sources,
            "includes": includes or [],
            "defines": defines or [],
            "options": options or {}
        }

    def add_dependency(self, target: str, dependency: str) -> None:
        """Add target dependency"""
        if target not in self.dependencies:
            self.dependencies[target] = []
        self.dependencies[target].append(dependency)

    def add_option(self, name: str, description: str, default: Any, type: str = None) -> None:
        """Add CMake option"""
        self.options[name] = {
            "description": description,
            "default": default,
            "type": type
        }

    def generate(self, output_file: str) -> None:
        """Generate CMakeLists.txt"""
        with open(output_file, "w", encoding="utf-8", newline="\n") as f:
            # Write CMake minimum version
            f.write(f"cmake_minimum_required(VERSION {self.cmake_minimum_version})\n\n")

            # Write project declaration
            f.write(f"project({self.project_name}\n")
            f.write(f"    VERSION {self.project_version}\n")
            f.write(f"    LANGUAGES {' '.join(self.project_languages)}\n")
            f.write(")\n\n")

            # Write options
            if self.options:
                f.write("# Options\n")
                for name, option in self.options.items():
                    if option["type"]:
                        f.write(f"option({name} \"{option['description']}\" {option['default']} TYPE {option['type']})\n")
                    else:
                        f.write(f"option({name} \"{option['description']}\" {option['default']})\n")
                f.write("\n")

            # Write variables
            if self.variables:
                f.write("# Variables\n")
                for name, var in self.variables.items():
                    if var["type"]:
                        f.write(f"set({name} {var['value']} TYPE {var['type']})\n")
                    else:
                        f.write(f"set({name} {var['value']})\n")
                f.write("\n")

            # Write targets
            if self.targets:
                f.write("# Targets\n")
                for name, target in self.targets.items():
                    if target["type"] == "executable":
                        f.write(f"add_executable({name}\n")
                    elif target["type"] == "static":
                        f.write(f"add_library({name} STATIC\n")
                    elif target["type"] == "shared":
                        f.write(f"add_library({name} SHARED\n")
                    else:
                        f.write(f"add_library({name} MODULE\n")

                    # Write sources
                    for source in target["sources"]:
                        f.write(f"    {source}\n")
                    f.write(")\n")

                    # Write includes
                    if target["includes"]:
                        f.write(f"target_include_directories({name} PRIVATE\n")
                        for include in target["includes"]:
                            f.write(f"    {include}\n")
                        f.write(")\n")

                    # Write defines
                    if target["defines"]:
                        f.write(f"target_compile_definitions({name} PRIVATE\n")
                        for define in target["defines"]:
                            f.write(f"    {define}\n")
                        f.write(")\n")

                    # Write options
                    if target["options"]:
                        for option_name, option_value in target["options"].items():
                            f.write(f"set_target_properties({name} PROPERTIES {option_name} {option_value})\n")

                    f.write("\n")

            # Write dependencies
            if self.dependencies:
                f.write("# Dependencies\n")
                for target, deps in self.dependencies.items():
                    for dep in deps:
                        f.write(f"add_dependencies({target} {dep})\n")
                f.write("\n")
