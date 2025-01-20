CMAKE_MINIMUM_REQUIRED(VERSION 3.19)

PROJECT(Illyrian VERSION 0.3.6)

SET(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/dist" CACHE STRING "" FORCE)

SET(Illyrian_INSTALL_PATH illyrian)

CONFIGURE_FILE(${CMAKE_CURRENT_LIST_DIR}/illyrian/version.py ${CMAKE_CURRENT_BINARY_DIR}/illyrian/version.py @ONLY)

INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/LICENSE
DESTINATION .)
INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/README.md
	${CMAKE_CURRENT_LIST_DIR}/illyrian/__init__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/__main__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/env.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/info.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/run.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/verify.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/wheel.py
	${CMAKE_CURRENT_BINARY_DIR}/illyrian/version.py
DESTINATION ${Illyrian_INSTALL_PATH})
INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/illyrian/manylinux/__init__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/manylinux/code.py
DESTINATION ${Illyrian_INSTALL_PATH}/manylinux)
INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/illyrian/util/__init__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/util/code.py
DESTINATION ${Illyrian_INSTALL_PATH}/util)
INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/__init__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/code.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython36.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython37.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython38.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython39.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython310.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/cpython/cpython311.py
DESTINATION ${Illyrian_INSTALL_PATH}/cpython)
INSTALL(FILES ${CMAKE_CURRENT_LIST_DIR}/illyrian/cmake/illyrian.cmake DESTINATION ${Illyrian_INSTALL_PATH}/cmake)

INCLUDE(illyrian/cmake/illyrian.cmake)
ILLYRIAN_FIND_PYTHON()
ILLYRIAN_INSTALL_PYTHON_PACKAGE("pydot")
ILLYRIAN_INSTALL_PYTHON_PACKAGE("auditwheel")

IF("${Python3_VERSION_MINOR}" LESS 7)
	ILLYRIAN_INSTALL_PYTHON_PACKAGE("importlib_resources")
ENDIF()

ADD_PYTHON_WHEEL(dist ${CMAKE_CURRENT_LIST_DIR}/illyrian.json)

ILLYRIAN_INSTALL_FIND_BEGIN(Illyrian PYTHON_NAME illyrian FILE "__main__.py")
ILLYRIAN_INSTALL_FIND_REQUIRED(FILE Illyrian MAIN "__main__.py" PATHS "\${Illyrian_DIR}")
ILLYRIAN_INSTALL_FIND_REQUIRED(FILE Illyrian CMAKE "illyrian.cmake" PATHS "\${Illyrian_DIR}/cmake")
ILLYRIAN_INSTALL_FIND_END(Illyrian
VERSION_FILE "\${Illyrian_DIR}/version.py"
VERSION_REGEX "__version__ = '([0-9\\.]+)'"
APPEND
	"IF(Illyrian_FOUND)"
	"\tINCLUDE(\${Illyrian_CMAKE})"
	"ENDIF()"
DESTINATION illyrian/cmake
)