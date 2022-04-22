CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

PROJECT(Illyrian VERSION 0.1.3)

SET(CMAKE_INSTALL_PREFIX "${CMAKE_BINARY_DIR}/dist" CACHE STRING "" FORCE)

SET(Illyrian_INSTALL_PATH illyrian)

CONFIGURE_FILE(${CMAKE_CURRENT_LIST_DIR}/illyrian/version.py ${CMAKE_CURRENT_BINARY_DIR}/illyrian/version.py @ONLY)

INSTALL(FILES
	${CMAKE_CURRENT_LIST_DIR}/LICENSE
	${CMAKE_CURRENT_LIST_DIR}/README.md
	${CMAKE_CURRENT_LIST_DIR}/illyrian/__init__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/__main__.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/run.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/env.py
	${CMAKE_CURRENT_LIST_DIR}/illyrian/wheel.py
	${CMAKE_CURRENT_BINARY_DIR}/illyrian/version.py
DESTINATION ${Illyrian_INSTALL_PATH})
INSTALL(FILES ${CMAKE_CURRENT_LIST_DIR}/illyrian/cmake/illyrian.cmake DESTINATION ${Illyrian_INSTALL_PATH}/cmake)
INSTALL(FILES ${CMAKE_CURRENT_LIST_DIR}/scripts/illyrian DESTINATION scripts)

INCLUDE(illyrian/cmake/illyrian.cmake)
ILLYRIAN_FIND_PYTHON()

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