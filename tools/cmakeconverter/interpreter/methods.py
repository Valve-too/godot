"""Mock methods module for SCons"""
from typing import Any, Dict, List, Optional, Union

def print_error(message: str) -> None:
    """Print error message"""
    print(f"ERROR: {message}")

def print_warning(message: str) -> None:
    """Print warning message"""
    print(f"WARNING: {message}")

def print_info(message: str) -> None:
    """Print info message"""
    print(f"INFO: {message}")

def to_raw_cstring(value: Union[str, List[str]]) -> str:
    """Convert to raw C string"""
    if isinstance(value, list):
        value = "\n".join(value) + "\n"
    return f'R"<!>({value})<!>"'

def add_source_files(self: Any, sources: List[Any], files: Union[str, List[str]], allow_gen: bool = False) -> bool:
    """Add source files"""
    return True

def add_module_version_string(self: Any, s: str) -> None:
    """Add module version string"""
    pass

def get_version_info(module_version_string: str = "", silent: bool = False) -> Dict[str, Any]:
    """Get version info"""
    return {}

def get_cmdline_bool(option: str, default: bool) -> bool:
    """Get command line bool"""
    return default

def detect_modules(search_path: str, recursive: bool = False) -> Dict[str, str]:
    """Detect modules"""
    return {}

def module_add_dependencies(self: Any, module: str, dependencies: List[str], optional: bool = False) -> None:
    """Add module dependencies"""
    pass

def module_check_dependencies(self: Any, module: str) -> bool:
    """Check module dependencies"""
    return True

def sort_module_list(env: Any) -> None:
    """Sort module list"""
    pass

def use_windows_spawn_fix(self: Any, platform: Optional[str] = None) -> None:
    """Use Windows spawn fix"""
    pass

def no_verbose(env: Any) -> None:
    """No verbose"""
    pass

def prepare_cache(env: Any) -> None:
    """Prepare cache"""
    pass

def convert_custom_modules_path(path: str) -> str:
    """Convert custom modules path"""
    return path

def set_scu_folders(scu_folders: set) -> None:
    """Set SCU folders"""
    pass

def using_gcc(env: Any) -> bool:
    """Check if using GCC"""
    return False

def using_clang(env: Any) -> bool:
    """Check if using Clang"""
    return False

def using_emcc(env: Any) -> bool:
    """Check if using Emscripten"""
    return False

def is_apple_clang(env: Any) -> bool:
    """Check if using Apple Clang"""
    return False

def get_compiler_version(env: Any) -> Dict[str, Any]:
    """Get compiler version"""
    return {"major": -1, "minor": -1, "metadata1": ""}

def show_progress(env: Any) -> None:
    """Show progress"""
    pass

def dump(env: Any) -> None:
    """Dump environment"""
    pass

def prepare_purge(env: Any) -> None:
    """Prepare purge"""
    pass

def prepare_timer() -> None:
    """Prepare timer"""
    pass

# Make module importable
import sys
sys.modules['methods'] = sys.modules[__name__]
