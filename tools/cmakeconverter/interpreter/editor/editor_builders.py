"""Mock editor_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def make_doc_header(target: Any, source: Any, env: Any) -> None:
    """Build doc header"""
    pass

def make_translations_header(target: Any, source: Any, env: Any, category: str) -> None:
    """Build translations header"""
    pass

def make_editor_translations_header(target: Any, source: Any, env: Any) -> None:
    """Build editor translations header"""
    pass

def make_property_translations_header(target: Any, source: Any, env: Any) -> None:
    """Build property translations header"""
    pass

def make_doc_translations_header(target: Any, source: Any, env: Any) -> None:
    """Build doc translations header"""
    pass

def make_extractable_translations_header(target: Any, source: Any, env: Any) -> None:
    """Build extractable translations header"""
    pass

# Make module importable
import sys
sys.modules['editor.editor_builders'] = sys.modules[__name__]
