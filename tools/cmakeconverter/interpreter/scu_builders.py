"""Mock scu_builders module for SCons"""
from typing import Any, Dict, List, Optional, Union

def generate_scu_files(max_includes_per_scu: int) -> set:
    """Generate SCU files"""
    return set()

# Make module importable
import sys
sys.modules['scu_builders'] = sys.modules[__name__]
