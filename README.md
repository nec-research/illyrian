# Illyrian

Illyrian is CMake extension for easily creating Python packages. The drawback of
setuptools is that it is supposed to be encapsulate CMake. However, if your
CMake produces multiple Python libraries, you would need to split your CMake
project. With Illyrian you don't need to do it! With Illyrian CMake encapsulates
the Python Wheel build process!

## Release Notes
<table>
<tr><th>Version</th><th>Comment</th></tr>

<tr><td>v0.1.3</td><td>
Split "tag" into "abi-tag" and "platform-tag" as described in [PEP491](https://peps.python.org/pep-0491/#file-name-convention).
</td></tr>

<tr><td>v0.1.2</td><td>
Improved Illyrian command argument parsing.
</td></tr>

<tr><td>v0.1.1</td><td>
Added ```EXACT``` to ```ILLYRIAN_FIND_PYTHON```
</td></tr>

<tr><td>v0.1.0</td><td>
Initial Release
</td></tr>

</table>

## How to build?
```base
git clone ...
cmake3 -S illyrian -B illyrian/build

# Build in ${CMAKE_BINARY_DIR}/dist
cmake3 --build illyrian/build --target install

# Build WHEEL
cmake --build illyrian/build --target dist

# Build WHEEL and immediately install
cmake --build illyrian/build --target dist-install
```
---

## Installing Illyrian
Either follow the building steps or just run ```pip3 install illyrian```.

---

## Setting up your CMake project
In order to setup your CMake project, it needs to contain:
```cmake
FIND_PACKAGE(Illyrian 0.1 REQUIRED)
```

After this line you can use all CMake Illyrian functions. To properly setup your
project you either need to manually set the ```CMAKE_MODULE_PATH``` to
```/path/to/illyrian/cmake/``` or just run ```illyrian cmake arg0 arg1 arg1 ... path/to/src```

---

## Available CMake commands:
### ILLYRIAN_PROJECT([C_STANDARD int] [CXX_STANDARD int] [INSTALL_PREFIX str] [SUPPORTED_OS list(str)])

Convenience wrapper for easier setup of C/C++ CMake projects. ```SUPPORTED_OS```
checks for matching strings in ```CMAKE_HOST_SYSTEM_NAME```.
```INSTALL_PREFIX``` sets the default ```CMAKE_INSTALL_PREFIX``` if non is
provided by the user or project itself.

### ILLYRIAN_FIND_PYTHON([VERSION version])
Searches for Python and additionally sets ```Python3_USERLIB``` to
```.local/lib/.../site-packages```. ```VERSION``` can be used to define a
minimum Python version, default is 3.7.

### ILLYRIAN_INSTALL_PYTHON_PACKAGE(list(str))
Installs the mentioned package using ```${Python3_EXECUTABLE} -m pip install
...```. Executes ```ILLYRIAN_FIND_PYTHON()``` if was not run before.

### ILLYRIAN_FIND_PACKAGE(NAME [REQUIRED] [VERSION version] [PATHS list(str)] [PYTHON list(str)])
Convenience wrapper for ```FIND_PACKAGE(...)``` that not only looks in the provided list of paths (i.e. ```PATHS /usr/local/bla```), but also in Python packages (i.e. ```PYTHON my_project/cmake```).

Some examples:
```cmake
ILLYRIAN_FIND_PACKAGE(Tungl       VERSION 0.1 REQUIRED PYTHON "tungl/cmake"         PATHS "/usr/local/nle/tungl/cmake")
ILLYRIAN_FIND_PACKAGE(VEDA        VERSION 1.3 REQUIRED PYTHON "veda/cmake"          PATHS "/usr/local/ve/veda/cmake")
ILLYRIAN_FIND_PACKAGE(VEDATensors VERSION 0.1 REQUIRED PYTHON "veda/tensors/cmake"	PATHS "/usr/local/ve/veda-tensors/cmake")
```

### ILLYRIAN_INSTALL_SYMLINK(DST SRC [DIRECTORY] [PYTHON] [DESTINATION])
Creates a Symlink during installation of project. ```DIRECTORY``` indicates a
directory symlink.
- ```DESTINATION``` the installation folder where to place the
symlink.
- ```PYTHON``` activates Python packaging. As Python wheels don't support symlinks Illyrian instead creates a linker file that can be used for linking, but no
other purposes.

### ILLYRIAN_OPTIONS(NAME list(str))
Convenience wrapper to create list options for CCMake.

### ILLYRIAN_TARGET_OPTIONS(NAME [LINK_MAP] [PYTHON] [SOVERSION version] [DESTINATION str] [COMPILE_OPTIONS list(str)] [LINK_FLAGS list(str)] [PYTHON_RPATH list(str)] [RPATH list(str)])
Convenience wrapper that packages C/C++ executables + libraries.
- ```LINK_MAP```: will use the version-script ```${NAME}.map``` in the current folder when linking the project.
- ```PYTHON```: activates Python packaging of this target.
- ```SOVERSION```: Sets the SOversion of the project. In normal mode, it creates symlinks like ```libbla.so -> libbla.so.1 -> libbla.so.1.2.3```. In Python mode it creates the library as ```libbla.so.1``` and creates linker scripts ```libbla.so``` and ```lib.bla.so.1.2.3``` that point to ```libbla.so.1```.
- ```DESTINATION```: Path to install the target to.
- ```COMPILE_OPTIONS```: Sets the target's compile options.
- ```LINK_FLAGS```: Sets the target's linker flags.
- ```PYTHON_RPATH```: RPATHs used when Python packaging.
- ```RPATH```: Normal RPATHs.

### ADD_PYTHON_WHEEL(TARGET_NAME JSON)
Reads the Illyrian config file ```JSON``` can creates the targets
```${TARGET_NAME}``` and ```${TARGET_NAME}-install```. The first compiles the
Python Wheel, the second additionally installs it using ```python3 -m pip
install ...```. The JSON file will be configured by CMake using the ```@ONLY```
option, so you can i.e. set the version as ```"version":
"@MyProject_VERSION@"```.

#### ILLYRIAN_INSTALL_FIND*
The ```ILLYRIAN_INSTALL_FIND*``` methods can be used to create customized find scripts for your project.

```cmake
# creates a new Find${NAME}.cmake
ILLYRIAN_INSTALL_FIND_BEGIN(
	NAME                     # Find${NAME}.cmake
	[PYTHON_NAME str]        # name of the project in Python notation (usually lowercase)
	[FILE str]               # a file used to determine the ${NAME}_DIR
	[PYTHON_VERSION version] # min Python Version required by the find script
	[PATHS list(str)]        # list of folders to look for FILE
)

# add FIND_${TYPE}(${NAME}_${VAR} ...) to the find script
ILLYRIAN_INSTALL_FIND_OPTIONAL(TYPE NAME VAR ...)

# same as ..._OPTIONAL but will fail if not found
ILLYRIAN_INSTALL_FIND_REQUIRED(TYPE NAME VAR ...)

# adds SET(${NAME}_${VAR} ...) to the find script
ILLYRIAN_INSTALL_FIND_SET(NAME VAR ...)

# finalizes the find script
ILLYRIAN_INSTALL_FIND_END(
	NAME                # Project Name
	[DESTINATION str]   # path for installation of the find script
	[VERSION_FILE str]  # file that gets read for extracting the version i.e. "include/version.h"
	[VERSION_REGEX str] # CMake Regex to extract the version from VERSION_FILE
	[APPEND list(str)]  # list of commands that just get appended to the find script
)
```

### ILLYRIAN_INCLUDE_DIRECTORIES([TARGETS list(targets] [PATHS list(paths)]))
Convenience wrapper to set ```INCLUDE_DIRECTORIES``` by paths and target names.

### ILLYRIAN_FIND_PYTHON_[PATH, FILE](VAR NAME FILE [PATHS list(str)])
Searches ```FILE``` in the Python package ```NAME``` given the folders ```PATHS``` and stores the PATH or FILE in ```VAR```.

---

## Manually running Illyrian

You can use Illyrian also without CMake. For this just run ```illyrian your_config.json``` in the root folder of your project.

---

## Illyrian Config File

The Illyrian config file is a plain JSON file that supports the following fields. See https://peps.python.org/pep-0345/ for explanation of the fields.

| Fields | Type | Comment |
| --- | --- | --- |
| ```__include__``` | str/list | Allows to include other config JSON files. If a key exists in both, the value will be casted to a list and get appended. |
| author | str | |
| author-email | str | |
| classifier | str/list | |
| download-url | str | |
| homepage | str | |
| keywords | str | |
| license | str | |
| maintainer | str  | |
| maintainer-email | str | | 
| name | str | required |
| obsoletes-dist | str/list | |
| platform | str/list | |
| project-url | str/list | |
| provides-dist | str/list | |
| readme | ```path/to/readme.md``` | Expects the path to a Markdown file. The file DOES NOT get stored within the wheel. Use ```payload``` for that. |
| requires-dist | str/list | |
| requires-external | str/list | |
| requires-python | ```>= 3.X``` | required |
| summary | str | required |
| supported-platform | str/list | |
| abi-tag | str | default: none |
| platform-tag | str | default: any |
| version | ```[0-9\.]+``` | required |

Additionally there the ```packages``` key expects a list of paths to python
packages, i.e. ```"packages": ["bla", "bla/sub"]```. ALL subpackages need to be
manually specified AND only ```*.py``` files will be includes.

The ```payload``` key expects a list of paths. Here you can use GLOB syntax
```path/to/*.h``` or use ```**``` for recursive inclusion, i.e.,
```path/to/**```.

```packages``` and ```payload``` fail if no files are found in the specified
path. If the first letter of the path is a ```?``` for ```packages``` or ```payload```, it gets marked
as optional and will not fail.

Here an example:
```json
{
	"name":				"illyrian",
	"version":			"@Illyrian_VERSION@",
	"platform":			"linux_x86_x64",
	"summary":			"Illyrian is CMake extension for easily creating Python packages.",
	"readme":			"illyrian/README.md",
	"author":			"User Name <user.name@company.com>",
	"license":			"3 BSD-License",
	"requires-python":	">=3.7",
	"packages": [
		"illyrian"
	],
	"payload": [
		"illyrian/LICENSE",
		"illyrian/cmake/*.cmake"
	],
	"scripts": [
		"scripts/illyrian"
	]
}
```