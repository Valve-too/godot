# SCons to CMake Converter

A Python-based tool that converts SCons build system configurations to CMake.

## Overview

This tool helps migrate projects from SCons to CMake by automatically converting SConstruct files to their CMake equivalents. It generates a `CMakeLists.txt` file based on your existing SCons configuration.

## Project Structure

The project should be structured as follows:

```
cmakeconverter/
├── __init__.py
├── main.py
├── converter.py
├── interpreter.py
└── README.md
```

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository or download the source files
2. Install as a package:

```bash
# From the parent directory containing cmakeconverter/
pip install -e .
```

Alternative installation methods:

1. Add the project root to PYTHONPATH:
```bash
# Linux/Mac
export PYTHONPATH=/path/to/parent/directory:$PYTHONPATH

# Windows (Command Prompt)
set PYTHONPATH=D:\path\to\parent\directory;%PYTHONPATH%

# Windows (PowerShell)
$env:PYTHONPATH = "D:\path\to\parent\directory;$env:PYTHONPATH"
```

2. Create a `setup.py` in the parent directory:
```python
from setuptools import setup, find_packages

setup(
    name="cmakeconverter",
    version="0.1",
    packages=find_packages(),
)
```

## Usage

### Command Line

Run the converter using the `main.py` script:

```bash
python -m cmakeconverter.main <path_to_sconstruct> [output_path]
```

Arguments:
- `path_to_sconstruct`: Path to your SConstruct file (required)
- `output_path`: Destination path for the generated CMakeLists.txt (optional, defaults to same directory as SConstruct)

### Python Module

Use the converter in your Python code:

```python
from cmakeconverter.converter import convert_build_system

# Convert SConstruct to CMakeLists.txt
convert_build_system('path/to/SConstruct', 'path/to/CMakeLists.txt')
```

## Examples

1. Basic usage with default output location:
```bash
python -m cmakeconverter.main ./SConstruct
```

2. Specifying a custom output path:
```bash
python -m cmakeconverter.main ./SConstruct ./build/CMakeLists.txt
```

3. Using Python directly:
```python
from cmakeconverter.converter import convert_build_system
convert_build_system('SConstruct', 'CMakeLists.txt')
```

## Troubleshooting

### Import Errors

If you see errors like:
```
ImportError: attempted relative import with no known parent package
```

This usually means the package is not properly installed or not in the Python path. Try:
1. Ensure you have an `__init__.py` file in the cmakeconverter directory
2. Install the package using pip or add it to PYTHONPATH as described in the Installation section
3. Run the script using `python -m cmakeconverter.main` instead of directly running main.py

## Error Handling

The tool will display helpful error messages in case of:
- Missing SConstruct file
- Invalid file paths
- Conversion errors

If an error occurs during conversion, the stack trace will be printed to help with debugging.

## Contributing

Feel free to submit issues and pull requests to help improve the converter.

## License

[Add your license information here]