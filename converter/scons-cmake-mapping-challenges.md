# Challenging SCons to CMake Conversions

## 1. Environment Handling

### SCons Keywords
- `env.Clone()`
- `env.Replace()`
- `env.Append()`
- `env.PrependUnique()`
- `env.MergeFlags()`

### Challenge
SCons environments are more dynamic and can be modified at runtime. CMake's variable scope is more static and hierarchical. Environment inheritance and modification patterns need careful restructuring.

## 2. Builder Operations

### SCons Keywords
- `env.Command()`
- `env.Builder()`
- `env.StaticObject()`
- `env.SharedObject()`
- `env.InstallAs()`

### Challenge
SCons builders are more flexible and can be created/modified at runtime. CMake requires custom commands and targets to be defined more explicitly and has less runtime flexibility.

## 3. File Operations

### SCons Keywords
- `Glob()`
- `FindFile()`
- `FindSourceFiles()`
- `FindInstalledFiles()`

### Challenge
SCons has more powerful file discovery mechanisms. CMake's file globbing is discouraged for build inputs and has different semantics.

## 4. Variant Builds

### SCons Keywords
- `variant_dir`
- `duplicate`
- `Repository()`
- `BuildDir()`

### Challenge
SCons handles variant builds and source copying differently. CMake requires explicit configuration of build directories and output locations.

## 5. Custom Tools and Tool Chains

### SCons Keywords
- `Tool()`
- `AddMethod()`
- `env['TOOLS']`
- `env.Tool()`

### Challenge
SCons tools are more dynamic and can modify the environment at runtime. CMake toolchains are more static and require different configuration approaches.

## 6. Dependencies

### SCons Keywords
- `Depends()`
- `Requires()`
- `Ignore()`
- `AlwaysBuild()`
- `Precious()`

### Challenge
SCons has more granular control over dependency relationships. CMake's dependency model is more rigid and may require workarounds.

## 7. Node Factory Methods

### SCons Keywords
- `Entry()`
- `File()`
- `Dir()`
- `Value()`

### Challenge
SCons node types don't have direct equivalents in CMake. Need to use different abstractions for representing filesystem entities.

## 8. Scanner Objects

### SCons Keywords
- `Scanner()`
- `env.Scanner()`
- `env.Append(SCANNERS=)`

### Challenge
SCons scanners for custom dependency detection don't have direct equivalents. May need custom CMake modules or external scripts.

## 9. Pseudo-Builders

### SCons Keywords
- `AddMethod()`
- Custom pseudo-builders

### Challenge
SCons pseudo-builders are more flexible for creating high-level build operations. CMake requires more explicit function definitions and macro usage.

## 10. Action Objects

### SCons Keywords
- `Action()`
- `env.Action()`
- `CommandAction`
- `FunctionAction`

### Challenge
SCons actions are more dynamic and can be combined/modified at runtime. CMake requires more static definition of build steps.

## Conversion Strategies

### For Environment Operations
```cmake
# Instead of env.Clone()
function(create_target_with_env target_name)
    add_library(${target_name})
    target_compile_definitions(${target_name} PRIVATE ${parent_definitions})
    # ... other property copying
endfunction()
```

### For Custom Builders
```cmake
# Instead of env.Builder()
function(custom_build_step target output_files)
    add_custom_command(
        OUTPUT ${output_files}
        COMMAND ${custom_command}
        DEPENDS ${dependencies}
    )
    add_custom_target(${target} DEPENDS ${output_files})
endfunction()
```

### For File Operations
```cmake
# Instead of Glob()
file(GLOB_RECURSE sources 
    CONFIGURE_DEPENDS  # Note: Use with caution
    "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp"
)
```

### For Variant Builds
```cmake
# Instead of variant_dir
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
```

## Special Considerations

1. **Runtime vs. Configure Time**
   - SCons operates at runtime
   - CMake generates build files at configure time
   - Need to move runtime logic to configure time

2. **Environment Inheritance**
   - Replace SCons environment inheritance with CMake target properties
   - Use interface libraries for shared properties

3. **Custom Tools**
   - Convert SCons tools to CMake modules
   - May need to split complex tools into multiple CMake functions

4. **Dependency Handling**
   - Use generator expressions for complex dependencies
   - May need custom targets for special cases

5. **Build Variants**
   - Use CMake configurations instead of SCons variants
   - May need multiple configure steps
