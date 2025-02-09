"""Module loader for SCons interpreter"""
from importlib.util import module_from_spec, spec_from_file_location
from types import ModuleType
import sys
import traceback
from typing import Any, Dict, Optional

class ModuleLoader:
    """Helper class to load modules"""
    def __init__(self):
        self._modules: Dict[str, Any] = {}

    def load_module(self, name: str, path: str) -> Optional[Any]:
        """Load a module from a file"""
        print(f"DEBUG: Loading module {name} from {path}")
        try:
            # Check if module is already loaded
            if name in self._modules:
                print(f"DEBUG: Module {name} already loaded")
                return self._modules[name]

            # Create spec and module
            spec = spec_from_file_location(name, path)
            if spec is None:
                print(f"DEBUG: Could not create spec for {name} from {path}")
                return None
            
            module = module_from_spec(spec)
            if module is None:
                print(f"DEBUG: Could not create module from spec for {name}")
                return None

            # Execute module
            if spec.loader is None:
                print(f"DEBUG: No loader for {name}")
                return None
            spec.loader.exec_module(module)

            # Store module
            sys.modules[name] = module
            self._modules[name] = module

            # Handle parent modules
            child_module = module
            parent_name = name
            while True:
                try:
                    parent_name, child_name = parent_name.rsplit(".", 1)
                except ValueError:
                    break
                try:
                    parent_module = sys.modules[parent_name]
                except KeyError:
                    parent_module = ModuleType(parent_name)
                    sys.modules[parent_name] = parent_module
                setattr(parent_module, child_name, child_module)
                child_module = parent_module

            print(f"DEBUG: Successfully loaded module {name}")
            return module

        except Exception as e:
            print(f"DEBUG: Error loading module {name}: {e}")
            print(f"DEBUG: Traceback:\n{traceback.format_exc()}")
            return None