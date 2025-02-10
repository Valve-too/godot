"""Mock platform_methods module for SCons"""
from typing import Any, Dict, List, Optional, Union

compatibility_platform_aliases = {
    "osx": "macos",
    "iphone": "ios",
    "x11": "linuxbsd",
    "javascript": "web",
}

architectures = ["x86_32", "x86_64", "arm32", "arm64", "rv64", "ppc32", "ppc64", "wasm32", "loongarch64"]

architecture_aliases = {
    "x86": "x86_32",
    "x64": "x86_64",
    "amd64": "x86_64",
    "armv7": "arm32",
    "armv8": "arm64",
    "arm64v8": "arm64",
    "aarch64": "arm64",
    "rv": "rv64",
    "riscv": "rv64",
    "riscv64": "rv64",
    "ppcle": "ppc32",
    "ppc": "ppc32",
    "ppc64le": "ppc64",
    "loong64": "loongarch64",
}

def detect_arch() -> str:
    """Detect CPU architecture"""
    return "x86_64"

def validate_arch(arch: str, platform_name: str, supported_arches: List[str]) -> None:
    """Validate CPU architecture"""
    pass

def get_build_version(short: bool) -> str:
    """Get build version"""
    return "4.4.0"

def lipo(prefix: str, suffix: str) -> str:
    """Create fat binary"""
    return ""

def get_mvk_sdk_path(osname: str) -> str:
    """Get MoltenVK SDK path"""
    return ""

def detect_mvk(env: Any, osname: str) -> str:
    """Detect MoltenVK"""
    return ""

# Make module importable
import sys
sys.modules['platform_methods'] = sys.modules[__name__]
