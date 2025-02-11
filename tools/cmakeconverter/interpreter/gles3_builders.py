"""Mock gles3_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def build_gles3_headers(target: Any, source: Any, env: Any) -> None:
    """Build GLES3 headers"""
    pass

# Make module importable
import sys
sys.modules['gles3_builders'] = sys.modules[__name__]
