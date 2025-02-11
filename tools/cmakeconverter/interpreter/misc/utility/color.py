"""Mock color module for SCons"""
from typing import Any, Dict, List, Optional, Union

STDOUT_COLOR = False
STDERR_COLOR = False

def print_error(*values: object) -> None:
    """Print error message"""
    print("ERROR:", *values)

def print_warning(*values: object) -> None:
    """Print warning message"""
    print("WARNING:", *values)

def print_info(*values: object) -> None:
    """Print info message"""
    print("INFO:", *values)

class Ansi:
    """Mock Ansi class"""
    RESET = ""
    BOLD = ""
    DIM = ""
    ITALIC = ""
    UNDERLINE = ""
    STRIKETHROUGH = ""
    REGULAR = ""
    BLACK = ""
    RED = ""
    GREEN = ""
    YELLOW = ""
    BLUE = ""
    MAGENTA = ""
    CYAN = ""
    WHITE = ""
    GRAY = ""

# Make module importable
import sys
sys.modules['misc.utility.color'] = sys.modules[__name__]
