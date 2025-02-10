"""Mock detect module for SCons"""
from typing import Any, Dict, List, Optional, Union

def get_name() -> str:
    """Get platform name"""
    return "LinuxBSD"

def can_build() -> bool:
    """Check if platform can be built"""
    return True

def get_opts() -> List[Any]:
    """Get platform options"""
    return []

def get_doc_classes() -> List[str]:
    """Get platform doc classes"""
    return []

def get_doc_path() -> str:
    """Get platform doc path"""
    return ""

def get_flags() -> Dict[str, Any]:
    """Get platform flags"""
    return {}

def configure(env: Any) -> None:
    """Configure platform"""
    pass

def get_tools(env: Any) -> List[str]:
    """Get platform tools"""
    return []

def get_program_suffix() -> str:
    """Get program suffix"""
    return ""

# Make module importable
import sys
sys.modules['detect'] = sys.modules[__name__]
