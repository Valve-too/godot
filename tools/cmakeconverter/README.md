# SCons to CMake Converter

A Python-based tool that converts SCons build system configurations to CMake, designed specifically for the Godot Engine build system.

## Features

Current capabilities:
- SCons environment simulation
- Variable handling and translation
- Platform detection and configuration
- Basic file operations (Glob, Object, etc.)
- Module loading framework
- CMake target generation

Supported SCons features:
- Basic environment variables
- Build targets (Program, Library)
- Source file handling
- Platform-specific configurations
- Module dependencies

## Development Status

This tool is currently in development. While it can handle basic SCons configurations, some advanced features are still being implemented:

- [ ] Complete module dependency handling
- [ ] Full platform-specific configuration support
- [ ] Advanced build target translation
- [ ] Custom builder support
- [ ] Test coverage

## Project Structure

```
cmakeconverter/
├── __init__.py
├── converter.py
├── cmake_generator.py
├── interpreter/
│   ├── __init__.py
│   ├── base.py
│   ├── builders.py
│   ├── detect.py
│   ├── environment.py
│   ├── functions.py
│   ├── methods.py
│   ├── module_loader.py
│   ├── platform.py
│   ├── utils.py
│   └── variables.py
├── SCons/
│   ├── __init__.py
│   ├── Script/
│   │   └── __init__.py
│   └── Variables/
│       └── __init__.py
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- SCons (for comparing build outputs)
- CMake (for verifying generated files)

For Windows users:
- Git Bash or similar Unix-like shell (recommended)
- Visual Studio with C++ workload (for building generated CMake files)

## Installation

### Method 1: Using pip (Recommended)

```bash
# From the parent directory containing cmakeconverter/
pip install -e .
```

### Method 2: Using PYTHONPATH

Windows (PowerShell):
```powershell
$env:PYTHONPATH = "C:\path\to\parent\directory;$env:PYTHONPATH"
```

Windows (Command Prompt):
```cmd
set PYTHONPATH=C:\path\to\parent\directory;%PYTHONPATH%
```

Linux/Mac:
```bash
export PYTHONPATH=/path/to/parent/directory:$PYTHONPATH
```

### Method 3: Development Setup

Create a `setup.py` in the parent directory:
```python
from setuptools import setup, find_packages

setup(
    name="cmakeconverter",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'setuptools',
    ],
    python_requires='>=3.8',
)
```

## Usage

### Command Line Examples

1. Basic conversion (Windows PowerShell):
```powershell
# From the Godot root directory
python -m tools.cmakeconverter.converter SConstruct CMakeLists.txt
```

2. With specific paths (Windows CMD):
```cmd
python -m tools.cmakeconverter.converter C:\projects\godot\SConstruct C:\projects\godot\build\CMakeLists.txt
```

3. Using relative paths:
```bash
cd /path/to/godot
python -m tools.cmakeconverter.converter ./SConstruct ./build/CMakeLists.txt
```

### Python Module Usage

```python
from tools.cmakeconverter.converter import convert_build_system

# Basic conversion
convert_build_system('SConstruct', 'CMakeLists.txt')

# With full paths
convert_build_system(
    'C:/projects/godot/SConstruct',
    'C:/projects/godot/build/CMakeLists.txt'
)
```

## Design

The converter uses a multi-stage approach:

1. **SCons Interpreter**: Simulates the SCons build system environment to understand the build configuration
2. **Build Analysis**: Analyzes the build targets, dependencies, and configurations
3. **CMake Generation**: Converts the analyzed build system into CMake syntax

Key components:
- `interpreter/`: Contains the SCons simulation environment
- `cmake_generator.py`: Handles CMake file generation
- `converter.py`: Orchestrates the conversion process

## Testing

To run the tests:

```bash
python -m unittest discover tests
```

When adding new features, please:
1. Add corresponding unit tests
2. Test with real SCons configurations
3. Verify CMake output builds correctly

## Known Limitations

Current version has the following limitations:

1. Complex custom builders may not convert correctly
2. Some platform-specific configurations need manual adjustment
3. Advanced SCons features might require manual intervention
4. Not all SCons functions are fully supported yet

Please check the issues page for known bugs and feature requests.

## Troubleshooting

### Common Issues

1. Import Errors:
```
ImportError: attempted relative import with no known parent package
```
Solution:
- Ensure you have `__init__.py` files in all directories
- Add the project root to PYTHONPATH
- Use the module format: `python -m tools.cmakeconverter.converter`

2. Path Issues on Windows:
```
FileNotFoundError: [Errno 2] No such file or directory
```
Solution:
- Use forward slashes (/) or escaped backslashes (\\) in paths
- Use absolute paths if relative paths fail
- Ensure all parent directories exist

3. Module Loading Errors:
```
ModuleNotFoundError: No module named 'tools.cmakeconverter'
```
Solution:
- Add the Godot root directory to PYTHONPATH
- Install the package using pip
- Run from the correct directory

### Debug Mode

To get more detailed output, set the debug environment variable:

Windows:
```cmd
set CMAKECONVERTER_DEBUG=1
```

Linux/Mac:
```bash
export CMAKECONVERTER_DEBUG=1
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add documentation for new features
- Include test cases
- Update the README if needed

## License

This tool is part of the Godot Engine project and follows its license terms.
See [LICENSE.txt](../../LICENSE.txt) for details.