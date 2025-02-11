"""Mock main_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def make_splash(target: Any, source: Any, env: Any) -> None:
    """Build splash screen"""
    pass

def make_splash_editor(target: Any, source: Any, env: Any) -> None:
    """Build editor splash screen"""
    pass

def make_app_icon(target: Any, source: Any, env: Any) -> None:
    """Build app icon"""
    pass

# Make module importable
import sys
sys.modules['main.main_builders'] = sys.modules[__name__]
