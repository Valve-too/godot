"""Mock core_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def make_certs_header(target: Any, source: Any, env: Any) -> None:
    """Build certs header"""
    pass

def make_authors_header(target: Any, source: Any, env: Any) -> None:
    """Build authors header"""
    pass

def make_donors_header(target: Any, source: Any, env: Any) -> None:
    """Build donors header"""
    pass

def make_license_header(target: Any, source: Any, env: Any) -> None:
    """Build license header"""
    pass

# Make module importable
import sys
sys.modules['core.core_builders'] = sys.modules[__name__]
