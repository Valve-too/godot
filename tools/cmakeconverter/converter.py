"""SCons to CMake converter module"""
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from .cmake_generator import CMakeGenerator
from .interpreter import SConsInterpreter

def convert_build_system(sconstruct_path: str) -> None:
    """Convert SCons build system to CMake"""
    print("Starting conversion from", os.path.basename(sconstruct_path))
    print("Current working directory:", os.getcwd())

    # Get absolute path to SConstruct file
    abs_sconstruct = os.path.abspath(sconstruct_path)
    print("Looking for SConstruct at:", abs_sconstruct)

    # Get output path
    output_path = os.path.join(os.path.dirname(abs_sconstruct), "CMakeLists.txt")
    print("Output will be written to:", output_path)

    # Create converter
    converter = SConsConverter()

    try:
        # Process SCons build system
        print("Processing SCons build system...")
        converter.process_scons(abs_sconstruct)

        # Generate CMake build system
        print("Generating CMake build system...")
        converter.generate_cmake(output_path)

        print("Conversion complete!")

    except Exception as e:
        print("Error during conversion:", str(e))
        print("Traceback:")
        import traceback
        traceback.print_exc()
        raise

class SConsConverter:
    """SCons to CMake converter class"""
    def __init__(self) -> None:
        self.interpreter = SConsInterpreter()
        self.generator = CMakeGenerator()

    def process_scons(self, sconstruct_path: str) -> None:
        """Process SCons build system"""
        self.interpreter.interpret_file(sconstruct_path)

    def generate_cmake(self, output_path: str) -> None:
        """Generate CMake build system"""
        # Convert SCons variables to CMake variables
        for name, value in self.interpreter.variables.items():
            self.generator.add_variable(name, value)

        # Convert SCons targets to CMake targets
        for name, target in self.interpreter.targets.items():
            self.generator.add_target(
                name=name,
                type=target["type"],
                sources=target["sources"],
                includes=target.get("includes"),
                defines=target.get("defines"),
                options=target.get("options")
            )

        # Convert SCons dependencies to CMake dependencies
        for target, deps in self.interpreter.dependencies.items():
            for dep in deps:
                self.generator.add_dependency(target, dep)

        # Generate CMakeLists.txt
        self.generator.generate(output_path)
