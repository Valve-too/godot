"""Mock template_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def parse_template(inherits: str, source: str, delimiter: str) -> str:
    """Parse template"""
    return ""

def make_templates(target: Any, source: Any, env: Any) -> None:
    """Build templates"""
    pass

# Make module importable
import sys
sys.modules['editor.template_builders'] = sys.modules[__name__]
