"""Mock scons_hints module for SCons"""
from typing import Any, Dict, List, Optional, Union

# Global functions
def GetSConsVersion() -> str:
    """Get SCons version"""
    return "4.4.0"

def EnsurePythonVersion(major: int, minor: int) -> None:
    """Ensure Python version"""
    pass

def EnsureSConsVersion(major: int, minor: int, revision: int) -> None:
    """Ensure SCons version"""
    pass

def Exit(code: int = 0) -> None:
    """Exit SCons"""
    pass

def GetLaunchDir() -> str:
    """Get launch directory"""
    return "/workspace/godot"

def SConscriptChdir(chdir: bool) -> None:
    """Set SConscript chdir"""
    pass

# SConsEnvironment functions
def Default(*targets: Any) -> None:
    """Set default targets"""
    pass

def Export(*vars: Any) -> None:
    """Export variables"""
    pass

def Help(text: str) -> None:
    """Add help text"""
    pass

def Import(*vars: Any) -> None:
    """Import variables"""
    pass

def SConscript(script: str, *args: Any, **kwargs: Any) -> None:
    """Execute SConscript"""
    pass

# Environment functions
def AddPostAction(target: Any, action: Any) -> None:
    """Add post action"""
    pass

def AddPreAction(target: Any, action: Any) -> None:
    """Add pre action"""
    pass

def Alias(alias: str, targets: Any) -> None:
    """Create alias"""
    pass

def AlwaysBuild(*targets: Any) -> None:
    """Always build targets"""
    pass

def CacheDir(path: str) -> None:
    """Set cache directory"""
    pass

def Clean(target: Any, source: Any) -> None:
    """Clean target"""
    pass

def Command(target: Any, source: Any, action: Any) -> None:
    """Create command"""
    pass

def Decider(decider: str) -> None:
    """Set decider"""
    pass

def Depends(target: Any, dependency: Any) -> None:
    """Add dependency"""
    pass

def Dir(path: str) -> Any:
    """Create directory node"""
    pass

def Entry(name: str) -> Any:
    """Create entry node"""
    pass

def Execute(action: Any) -> None:
    """Execute action"""
    pass

def File(path: str) -> Any:
    """Create file node"""
    pass

def FindFile(file: str, dirs: Any) -> Any:
    """Find file"""
    pass

def FindInstalledFiles() -> List[Any]:
    """Find installed files"""
    return []

def FindSourceFiles() -> List[Any]:
    """Find source files"""
    return []

def Flatten(sequence: Any) -> List[Any]:
    """Flatten sequence"""
    return []

def GetBuildPath(file: str) -> str:
    """Get build path"""
    return ""

def Glob(pattern: str) -> List[Any]:
    """Glob files"""
    return []

def Ignore(target: Any, dependency: Any) -> None:
    """Ignore dependency"""
    pass

def Install(dir: str, source: Any) -> None:
    """Install source"""
    pass

def InstallAs(target: str, source: Any) -> None:
    """Install source as target"""
    pass

def InstallVersionedLib(target: str, source: Any) -> None:
    """Install versioned library"""
    pass

def Literal(string: str) -> Any:
    """Create literal"""
    pass

def Local(*targets: Any) -> None:
    """Mark targets as local"""
    pass

def NoCache(*targets: Any) -> None:
    """Disable caching for targets"""
    pass

def NoClean(*targets: Any) -> None:
    """Disable cleaning for targets"""
    pass

def ParseDepends(filename: str) -> None:
    """Parse dependencies"""
    pass

def Precious(*targets: Any) -> None:
    """Mark targets as precious"""
    pass

def PyPackageDir(package: str) -> str:
    """Get Python package directory"""
    return ""

def Repository(*dirs: str) -> None:
    """Add repository"""
    pass

def Requires(*targets: Any) -> None:
    """Add requirements"""
    pass

def SConsignFile(file: str) -> None:
    """Set SConsign file"""
    pass

def SideEffect(side_effect: Any, target: Any) -> None:
    """Add side effect"""
    pass

def Split(arg: str) -> List[str]:
    """Split string"""
    return []

def Tag(node: Any, tags: Any) -> None:
    """Add tags"""
    pass

def Value(value: Any) -> Any:
    """Create value node"""
    pass

def VariantDir(variant_dir: str, src_dir: str) -> None:
    """Create variant directory"""
    pass

# Make module importable
import sys
sys.modules['misc.utility.scons_hints'] = sys.modules[__name__]
