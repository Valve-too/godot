"""Mock version module for SCons"""
from typing import Any, Dict, List, Optional, Union

short_name = "godot"
name = "Godot Engine"
major = 4
minor = 4
patch = 0
status = "beta"
module_config = ""
website = "https://godotengine.org"
docs = "latest"

# Make module importable
import sys
sys.modules['version'] = sys.modules[__name__]
