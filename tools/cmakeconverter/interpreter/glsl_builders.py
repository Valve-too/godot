"""Mock glsl_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def build_rd_headers(target: Any, source: Any, env: Any) -> None:
    """Build RD headers"""
    pass

def build_raw_headers(target: Any, source: Any, env: Any) -> None:
    """Build raw headers"""
    pass

# Make module importable
import sys
sys.modules['glsl_builders'] = sys.modules[__name__]
