SET(Illyrian_ROOT			"${CMAKE_BINARY_DIR}/illyrian")
SET(Illyrian_SYMLINK_ROOT	"${Illyrian_ROOT}/symlinks")
SET(ILLYRIAN_NO_PYTHON OFF CACHE BOOL "Enables/Disables looking for Python with Illyrian")

MACRO(ILLYRIAN_PROJECT)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		"C_STANDARD;CXX_STANDARD;INSTALL_PREFIX"
		"SUPPORTED_OS"
		"${ARGN}"
	)

	IF(ILLYRIAN_ARGS_SUPPORTED_OS)
		SET(FAILED TRUE)
		FOREACH(OS in ${ILLYRIAN_ARGS_SUPPORTED_OS})
			IF(${CMAKE_HOST_SYSTEM_NAME} MATCHES ${OS})
				SET(FAILED FALSE)
			ENDIF()
		ENDFOREACH()

		IF(FAILED)
			MESSAGE(FATAL_ERROR "Unsupported operating system (${CMAKE_HOST_SYSTEM_NAME}). Only ${ILLYRIAN_ARGS_SUPPORTED_OS} is/are supported!")
		ENDIF()
	ENDIF()

	IF(NOT ILLYRIAN_ARGS_C_STANDARD)
		SET(ILLYRIAN_ARGS_C_STANDARD 17)
	ENDIF()

	IF(NOT ILLYRIAN_ARGS_CXX_STANDARD)
		SET(ILLYRIAN_ARGS_CXX_STANDARD 17)
	ENDIF()

	SET(CMAKE_C_STANDARD			${ILLYRIAN_ARGS_C_STANDARD})
	SET(CMAKE_C_STANDARD_REQUIRED	ON)
	SET(CMAKE_CXX_STANDARD			${ILLYRIAN_ARGS_CXX_STANDARD})
	SET(CMAKE_CXX_STANDARD_REQUIRED	ON)
	SET(CXX_EXTENSIONS				OFF)

	IF(NOT CMAKE_BUILD_TYPE)
		SET(CMAKE_BUILD_TYPE RELEASE CACHE STRING "" FORCE)
	ENDIF()

	IF(ILLYRIAN_ARGS_INSTALL_PREFIX)
		IF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT OR NOT CMAKE_INSTALL_PREFIX)
			SET(CMAKE_INSTALL_PREFIX ${ILLYRIAN_ARGS_INSTALL_PREFIX} CACHE PATH "CMAKE install path" FORCE)
		ENDIF()
	ENDIF()

	SET(CMAKE_INSTALL_RPATH "\$ORIGIN")

	UNSET(ILLYRIAN_ARGS_C_STANDARD)
	UNSET(ILLYRIAN_ARGS_CXX_STANDARD)
	UNSET(ILLYRIAN_ARGS_INSTALL_PREFIX)
	UNSET(ILLYRIAN_ARGS_SUPPORTED_OS)
ENDMACRO()

FUNCTION(ILLYRIAN_INSTALL_PYTHON_PACKAGE)
	ILLYRIAN_FIND_PYTHON()
	EXECUTE_PROCESS(COMMAND ${Python3_EXECUTABLE} -m pip install ${ARGN} RESULT_VARIABLE RES)
	IF(NOT RES EQUAL 0)
		MESSAGE(SEND_ERROR "Failed to run PIP install ${ARGN}")
	ENDIF()
ENDFUNCTION()

MACRO(ILLYRIAN_FIND_PYTHON)
	IF(ILLYRIAN_NO_PYTHON)
		# don't search for Python in this mode
	ELSEIF(NOT Python3_VERSION_MAJOR)
		CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
			"EXACT"
			"VERSION"
			""
			${ARGN})

		IF(NOT ILLYRIAN_ARGS_VERSION)
			IF($ENV{ILLYRIAN_PYTHON_VERSION})
				SET(ILLYRIAN_ARGS_VERSION $ENV{ILLYRIAN_PYTHON_VERSION})
				SET(ILLYRIAN_ARGS_EXACT EXACT)
			ELSE()
				SET(ILLYRIAN_ARGS_VERSION 3.7)
			ENDIF()
		ENDIF()

		IF(ILLYRIAN_ARGS_EXACT)
			SET(ILLYRIAN_ARGS_EXACT EXACT)
		ELSE()
			SET(ILLYRIAN_ARGS_EXACT "")
		ENDIF()

		FIND_PACKAGE(Python3 ${ILLYRIAN_ARGS_VERSION} ${ILLYRIAN_ARGS_EXACT} REQUIRED)
		
		SET(Python3_EXECUTABLE ${Python3_EXECUTABLE} CACHE STRING "")
		SET(Python3_VERSION_MAJOR ${Python3_VERSION_MAJOR} CACHE STRING "")
		SET(Python3_VERSION_MINOR ${Python3_VERSION_MINOR} CACHE STRING "")
		SET(Python3_SITELIB ${Python3_SITELIB} CACHE STRING "")
		SET(Python3_USERLIB "$ENV{HOME}/.local/lib/python${Python3_VERSION_MAJOR}.${Python3_VERSION_MINOR}/site-packages" CACHE STRING "")

		UNSET(ILLYRIAN_ARGS_EXACT)
		UNSET(ILLYRIAN_ARGS_VERSION)
	ENDIF()

	MARK_AS_ADVANCED(Python3_EXECUTABLE Python3_VERSION_MAJOR Python3_VERSION_MINOR Python3_SITELIB Python3_USERLIB)
ENDMACRO()

MACRO(ILLYRIAN_FIND_PACKAGE NAME)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		"REQUIRED"
		"VERSION"
		"PATHS;PYTHON"
		"${ARGN}"
	)

	SET(ILLYRIAN_ARGS_CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH})

	IF(ILLYRIAN_ARGS_REQUIRED)
		SET(ILLYRIAN_ARGS_REQUIRED REQUIRED)
	ENDIF()

	IF(ILLYRIAN_ARGS_PATHS)
		FOREACH(PATH ${ILLYRIAN_ARGS_PATHS})
			SET(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${PATH}")
		ENDFOREACH()
	ENDIF()

	IF(ILLYRIAN_ARGS_PYTHON)
		ILLYRIAN_FIND_PYTHON()
		FOREACH(PATH ${ILLYRIAN_ARGS_PYTHON})
			SET(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH};${Python3_SITELIB}/${PATH};${Python3_USERLIB}/${PATH}")
		ENDFOREACH()
	ENDIF()

	FIND_PACKAGE(${NAME} ${ILLYRIAN_ARGS_VERSION} ${ILLYRIAN_ARGS_REQUIRED})

	IF(${NAME}_VERSION)
		IF(ILLYRIAN_ARGS_VERSION)
			SET(${NAME}_VERSION_MIN ${ILLYRIAN_ARGS_VERSION})
		ELSE()
			SET(${NAME}_VERSION_MIN ${${NAME}_VERSION})
		ENDIF()

		STRING(REGEX MATCH "[0-9]+" ${NAME}_VERSION_MAX ${${NAME}_VERSION})
		MATH(EXPR ${NAME}_VERSION_MAX "${${NAME}_VERSION_MAX} + 1")
	ENDIF()

	# RESET MODULE PATH
	SET(CMAKE_MODULE_PATH ${ILLYRIAN_ARGS_CMAKE_MODULE_PATH})
	UNSET(ILLYRIAN_ARGS_CMAKE_MODULE_PATH)
	UNSET(ILLYRIAN_ARGS_REQUIRED)
	UNSET(ILLYRIAN_ARGS_VERSION)
	UNSET(ILLYRIAN_ARGS_PATHS)
ENDMACRO()

FUNCTION(ILLYRIAN_INSTALL_SYMLINK DST SRC)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		"DIRECTORY;PYTHON"
		"DESTINATION"
		""
		"${ARGN}"
	)

	GET_FILENAME_COMPONENT	(SYMLINK_PATH ${SRC} DIRECTORY)
	FILE					(MAKE_DIRECTORY ${Illyrian_SYMLINK_ROOT}/${SYMLINK_PATH})
	SET						(SRC ${Illyrian_SYMLINK_ROOT}/${SRC})

	IF(EXISTS ${SRC})
		FILE(REMOVE ${SRC})
	ENDIF()

	IF(ILLYRIAN_ARGS_PYTHON)
		FILE(WRITE ${SRC} "INPUT(${DST})")
	ELSE()
		EXECUTE_PROCESS(COMMAND ${CMAKE_COMMAND} -E create_symlink ${DST} ${SRC})
	ENDIF()
	
	IF(NOT ILLYRIAN_ARGS_DESTINATION)	
		SET(ILLYRIAN_ARGS_DESTINATION ".")
	ENDIF()

	IF(ILLYRIAN_ARGS_DIRECTORY)
		SET(INSTALL_TYPE DIRECTORY)
	ELSE()
		SET(INSTALL_TYPE FILES)
	ENDIF()

	INSTALL(${INSTALL_TYPE} ${SRC} DESTINATION ${ILLYRIAN_ARGS_DESTINATION}/${SYMLINK_PATH})
ENDFUNCTION()

MACRO(ILLYRIAN_OPTIONS NAME)
	SET(${NAME} ${ARGV1} CACHE STRING "")
	SET_PROPERTY(CACHE ${NAME} PROPERTY STRINGS ${ARGN})
ENDMACRO()

FUNCTION(ILLYRIAN_TARGET_OPTIONS NAME)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		"LINK_MAP;PYTHON"
		"SOVERSION;DESTINATION"
		"COMPILE_OPTIONS;LINK_FLAGS;PYTHON_RPATH;RPATH"
		"${ARGN}"
	)

	SET(ILLYRIAN_LINK_FLAGS "")
	IF(ILLYRIAN_ARGS_LINK_MAP)
		SET(ILLYRIAN_LINK_FLAGS "${ILLYRIAN_LINK_FLAGS} -Wl,--version-script=${CMAKE_CURRENT_LIST_DIR}/${NAME}.map")
	ENDIF()

	IF(NOT ILLYRIAN_ARGS_RPATH)
		SET(ILLYRIAN_ARGS_RPATH "$ORIGIN")
	ENDIF()

	IF(ILLYRIAN_ARGS_PYTHON)
		SET(ILLYRIAN_ARGS_PYTHON "PYTHON")
		SET(ILLYRIAN_ARGS_RPATH ${ILLYRIAN_ARGS_PYTHON_RPATH})
	ENDIF()

	TARGET_COMPILE_OPTIONS(${NAME} PRIVATE
		-Wuninitialized
		-Wunknown-pragmas
		-Wunused-function
		-Wunused-label
		-Wunused-value
		-Wunused-variable
		-Wno-return-local-addr
		${ILLYRIAN_ARGS_COMPILE_OPTIONS}
	)
	SET_TARGET_PROPERTIES(${NAME} PROPERTIES
		LINK_FLAGS 		"-Wl,-z,defs ${ILLYRIAN_LINK_FLAGS}"
		INSTALL_RPATH	"${ILLYRIAN_ARGS_RPATH}"
	)

	IF(ILLYRIAN_ARGS_SOVERSION)
		STRING(REGEX MATCH "^[0-9]+" ILLYRIAN_ARGS_SOVERSION_MAJOR ${ILLYRIAN_ARGS_SOVERSION})

		IF(ILLYRIAN_ARGS_PYTHON)
			SET_TARGET_PROPERTIES(${NAME} PROPERTIES SUFFIX ".so.${ILLYRIAN_ARGS_SOVERSION_MAJOR}")
			ILLYRIAN_INSTALL_SYMLINK(
				"lib${NAME}.so.${ILLYRIAN_ARGS_SOVERSION_MAJOR}"
				"lib${NAME}.so"
				${ILLYRIAN_ARGS_PYTHON}
				DESTINATION ${ILLYRIAN_ARGS_DESTINATION})
			ILLYRIAN_INSTALL_SYMLINK(
				"lib${NAME}.so.${ILLYRIAN_ARGS_SOVERSION_MAJOR}"
				"lib${NAME}.so.${ILLYRIAN_ARGS_SOVERSION}"
				${ILLYRIAN_ARGS_PYTHON}
				DESTINATION ${ILLYRIAN_ARGS_DESTINATION})
		ELSE()
			SET_TARGET_PROPERTIES(${NAME} PROPERTIES
				VERSION		${ILLYRIAN_ARGS_SOVERSION}
				SOVERSION	${ILLYRIAN_ARGS_SOVERSION_MAJOR}
			)
		ENDIF()
	ENDIF()

	IF(ILLYRIAN_ARGS_DESTINATION)
		INSTALL(TARGETS ${NAME} DESTINATION ${ILLYRIAN_ARGS_DESTINATION})
	ENDIF()
ENDFUNCTION()

FUNCTION(ADD_PYTHON_WHEEL TARGET_NAME JSON)
	ILLYRIAN_FIND_PYTHON()

	IF(NOT TARGET illyrian_install)
		ADD_CUSTOM_TARGET(illyrian_install ${CMAKE_COMMAND} --build ${CMAKE_BINARY_DIR} --target install)
	ENDIF()

	GET_FILENAME_COMPONENT(CONFIGURED_JSON ${JSON} NAME)
	SET(CONFIGURED_JSON ${CMAKE_CURRENT_BINARY_DIR}/${CONFIGURED_JSON})
	CONFIGURE_FILE(${JSON} ${CONFIGURED_JSON} @ONLY)

	FILE(READ ${CONFIGURED_JSON} CONFIG)
	
	STRING(REGEX MATCH "\"name\":[ \t]*\"([a-zA-Z0-9_\\-]+)\"," NAME ${CONFIG})
	SET(NAME ${CMAKE_MATCH_1})
	IF(NOT NAME)
		MESSAGE(FATAL_ERROR "Missing name in ${JSON}")
	ENDIF()

	# https://www.python.org/dev/peps/pep-0427/#id13 # re.sub("[^\w\d.]+", "_", distribution, re.UNICODE)
	STRING(TOLOWER ${NAME} NAME)

	ADD_CUSTOM_TARGET(${TARGET_NAME}-pre
		COMMAND ${CMAKE_COMMAND} -E rm -f *.whl
		DEPENDS illyrian_install
		WORKING_DIRECTORY ${CMAKE_INSTALL_PREFIX})
	
	ADD_CUSTOM_TARGET(${TARGET_NAME}
		COMMAND ${Python3_EXECUTABLE} -m illyrian ${CONFIGURED_JSON}
		DEPENDS ${TARGET_NAME}-pre
		WORKING_DIRECTORY ${CMAKE_INSTALL_PREFIX})

	ADD_CUSTOM_TARGET(${TARGET_NAME}-install
		COMMAND	${Python3_EXECUTABLE} -m pip uninstall ${NAME} -y
		COMMAND ${Python3_EXECUTABLE} -m pip install -f . ${NAME}
		DEPENDS ${TARGET_NAME}
		WORKING_DIRECTORY ${CMAKE_INSTALL_PREFIX})
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_WRITE MODE NAME)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		"APPEND"
		""
		""
		"${ARGN}"
	)
	LIST(JOIN ARGN "\n" CONTENT)
	IF(MODE STREQUAL APPEND)
		SET(CONTENT "\n${CONTENT}")
	ENDIF()
	FILE(${MODE} ${CMAKE_CURRENT_BINARY_DIR}/Find${NAME}.cmake ${CONTENT})
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_SET NAME VAR)
	LIST(APPEND ILLYRIAN_INSTALL_FIND_VARS ${VAR})
	SET(ILLYRIAN_INSTALL_FIND_VARS ${ILLYRIAN_INSTALL_FIND_VARS} PARENT_SCOPE)
	LIST(JOIN ARGN "\" \"" CONTENT)
	ILLYRIAN_INSTALL_FIND_WRITE(APPEND ${NAME} "\t\tSET(${NAME}_${VAR} \"${CONTENT}\")")
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_OPTIONAL TYPE NAME VAR)
	LIST(JOIN ARGN "\" \"" CONTENT)
	ILLYRIAN_INSTALL_FIND_WRITE(APPEND ${NAME} "\t\tFIND_${TYPE}(${NAME}_${VAR} \"${CONTENT}\")")
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_REQUIRED TYPE NAME VAR)
	LIST(APPEND ILLYRIAN_INSTALL_FIND_VARS ${VAR})
	SET(ILLYRIAN_INSTALL_FIND_VARS ${ILLYRIAN_INSTALL_FIND_VARS} PARENT_SCOPE)
	ILLYRIAN_INSTALL_FIND_OPTIONAL(${TYPE} ${NAME} ${VAR} ${ARGN})
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_END NAME)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		"DESTINATION"
		"VERSION_FILE;VERSION_REGEX;APPEND"
		"${ARGN}"
	)

	IF(NOT ILLYRIAN_ARGS_VERSION_FILE OR NOT ILLYRIAN_ARGS_VERSION_REGEX)
		MESSAGE(FATAL_ERROR "Please provide ILLYRIAN_INSTALL_FIND_END(VERSION_FILE ... VERSION_REGEX ...)")
	ENDIF()

	FOREACH(VAR ${ILLYRIAN_INSTALL_FIND_VARS})
		IF(NOT CONTENT)
			SET(CONTENT "\n\t\tIF(")
		ELSE()
			SET(CONTENT "${CONTENT} AND ")
		ENDIF()
		SET(CONTENT "${CONTENT}${NAME}_${VAR}")
	ENDFOREACH()
	
	SET(CONTENT
		"${CONTENT})"
		"\t\t\tSET(${NAME}_FOUND TRUE)"
		"\t\t\tFILE(READ \"${ILLYRIAN_ARGS_VERSION_FILE}\" ${NAME}_VERSION)"
		"\t\t\tSTRING(REGEX MATCH \"${ILLYRIAN_ARGS_VERSION_REGEX}\" ${NAME}_VERSION \${${NAME}_VERSION})"
		"\t\t\tSET(${NAME}_VERSION \${CMAKE_MATCH_1})"
		"\t\t\tSET(${NAME}_VERSION \${${NAME}_VERSION} CACHE STRING \"${NAME} Version\")"
		"\t\t\tMESSAGE(STATUS \"Found ${NAME} v\${${NAME}_VERSION}: \${${NAME}_DIR}\")"
		"\t\tELSE()"
		"\t\t\tMESSAGE(STATUS \"Unable to find all requirements of ${NAME} in \${${NAME}_DIR}\")"
	)

	FOREACH(VAR ${ILLYRIAN_INSTALL_FIND_VARS})
		SET(CONTENT
			"${CONTENT}"
			"\t\t\tMESSAGE(STATUS \"${NAME}_${VAR}: \${${NAME}_${VAR}}\")"
		)
	ENDFOREACH()

	SET(CONTENT
		"${CONTENT}"
		"\t\tENDIF()"
		" "
		"\t\tSET(${NAME}_FOUND \${${NAME}_FOUND} CACHE BOOL \"Found ${NAME}\" FORCE)"
		"\t\tMARK_AS_ADVANCED(${NAME}_FOUND ${NAME}_VERSION ${NAME}_DIR"
	)
	
	FOREACH(VAR ${ILLYRIAN_INSTALL_FIND_VARS})
		SET(CONTENT "${CONTENT} ${NAME}_${VAR}")
	ENDFOREACH()
	
	SET(CONTENT
		"${CONTENT})"
		"\tENDIF()"
		"ENDIF()"
		" "
		"IF(${NAME}_FIND_REQUIRED AND NOT ${NAME}_FOUND)"
		"\tMESSAGE(FATAL_ERROR \"Unable to find ${NAME}!\")"
		"ENDIF()"
		" "
		"IF(${NAME}_FIND_VERSION AND ${NAME}_VERSION VERSION_LESS ${NAME}_FIND_VERSION)"
		"\tMESSAGE(FATAL_ERROR \"Found ${NAME} v\${${NAME}_VERSION} but expected at least v\${${NAME}_FIND_VERSION}\")"
		"ENDIF()"
		" "
		# don't ask me why we need so many \ here... but it works.
		"STRING(ASCII 59 ${NAME}_SEMICOLON)"
		"STRING(REPLACE \".\" \"\${${NAME}_SEMICOLON}\" ${NAME}_VERSION_LIST \${${NAME}_VERSION})"
		"SET(${NAME}_VERSION_MAJOR 0)"
		"SET(${NAME}_VERSION_MINOR 0)"
		"SET(${NAME}_VERSION_PATCH 0)"
		"LIST(LENGTH ${NAME}_VERSION_LIST ${NAME}_VERSION_LEN)"
		"IF(${NAME}_VERSION_LEN GREATER 0)"
		"\tLIST(GET ${NAME}_VERSION_LIST 0 ${NAME}_VERSION_MAJOR)"
		"ENDIF()"
		"IF(${NAME}_VERSION_LEN GREATER 1)"
		"\tLIST(GET ${NAME}_VERSION_LIST 1 ${NAME}_VERSION_MINOR)"
		"ENDIF()"
		"IF(${NAME}_VERSION_LEN GREATER 2)"
		"\tLIST(GET ${NAME}_VERSION_LIST 2 ${NAME}_VERSION_PATCH)"
		"ENDIF()"
		"UNSET(${NAME}_VERSION_LEN)"
		"UNSET(${NAME}_VERSION_LIST)"
		"UNSET(${NAME}_SEMICOLON)"
	)

	IF(ILLYRIAN_ARGS_APPEND)
		SET(CONTENT ${CONTENT} " " ${ILLYRIAN_ARGS_APPEND})
	ENDIF()

	ILLYRIAN_INSTALL_FIND_WRITE(APPEND ${NAME} ${CONTENT})

	IF(NOT ILLYRIAN_ARGS_DESTINATION)
		SET(ILLYRIAN_ARGS_DESTINATION .)
	ENDIF()

	INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/Find${NAME}.cmake DESTINATION ${ILLYRIAN_ARGS_DESTINATION})

	UNSET(ILLYRIAN_INSTALL_FIND_VARS PARENT_SCOPE)
ENDFUNCTION()

FUNCTION(ILLYRIAN_INSTALL_FIND_BEGIN NAME)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		"PYTHON_NAME;FILE;PYTHON_VERSION"
		"PATHS"
		"${ARGN}"
	)

	SET(ILLYRIAN_INSTALL_FIND_VARS "")

	IF(NOT ILLYRIAN_ARGS_FILE)
		MESSAGE(FATAL_ERROR "Missing ILLYRIAN_INSTALL_FIND_BEGIN(FILE ...)")
	ENDIF()

	SET(CONTENT
		# if an older version had been found, retry searching
		"IF(${NAME}_FIND_VERSION AND ${NAME}_VERSION AND ${NAME}_VERSION VERSION_LESS ${NAME}_FIND_VERSION)"
		"\tUNSET(${NAME}_VERSION CACHE)"
		"\tUNSET(${NAME}_FOUND CACHE)"
		"ENDIF()"
		# has been found?
		"IF(NOT ${NAME}_FOUND)"
		"\tSET(${NAME}_FOUND FALSE)"
		"\tFIND_PATH(${NAME}_DIR \"${ILLYRIAN_ARGS_FILE}\" PATHS \"\${CMAKE_CURRENT_LIST_DIR}/../\""
	)

	FOREACH(PATH ${ILLYRIAN_ARGS_PATHS})
		SET(CONTENT "${CONTENT} \"${PATH}\"")
	ENDFOREACH()

	SET(CONTENT "${CONTENT})" " ")

	IF(ILLYRIAN_ARGS_PYTHON_NAME)
		IF(NOT ILLYRIAN_ARGS_PYTHON_VERSION)
			SET(ILLYRIAN_ARGS_PYTHON_VERSION 3.7)
		ENDIF()

		LIST(APPEND CONTENT
			"\tIF(NOT ${NAME}_DIR)"
			"\t\tFIND_PACKAGE(Python3 ${ILLYRIAN_ARGS_PYTHON_VERSION} REQUIRED)"
			"\t\tSET(Python3_USERLIB \"\$ENV{HOME}/.local/lib/python\${Python3_VERSION_MAJOR}.\${Python3_VERSION_MINOR}/site-packages\")"
			"\t\tFIND_FILE(${NAME}_DIR \"${ILLYRIAN_ARGS_FILE}\" PATHS \"\${Python3_SITELIB}/${ILLYRIAN_ARGS_PYTHON_NAME}\" \"\${Python3_USERLIB}/${ILLYRIAN_ARGS_PYTHON_NAME}\")"
			"\tENDIF()"
			" "
		)
	ENDIF()

	LIST(APPEND CONTENT "\tIF(${NAME}_DIR)")
	ILLYRIAN_INSTALL_FIND_WRITE(WRITE ${NAME} ${CONTENT})
ENDFUNCTION()

MACRO(ILLYRIAN_INCLUDE_DIRECTORIES)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		""
		"TARGETS;PATHS"
		"${ARGN}"
	)

	FOREACH(TARGET ${ILLYRIAN_ARGS_TARGETS})
		GET_TARGET_PROPERTY(ILLYRIAN_ARGS_PATH ${TARGET} SOURCE_DIR)
		LIST(APPEND ILLYRIAN_ARGS_PATHS ${ILLYRIAN_ARGS_PATH})
		GET_TARGET_PROPERTY(ILLYRIAN_ARGS_PATH ${TARGET} BINARY_DIR)
		LIST(APPEND ILLYRIAN_ARGS_PATHS ${ILLYRIAN_ARGS_PATH})
	ENDFOREACH()

	FOREACH(PATH ${ILLYRIAN_ARGS_PATHS})
		INCLUDE_DIRECTORIES(${PATH})
	ENDFOREACH()

	UNSET(ILLYRIAN_ARGS_PATH)
	UNSET(ILLYRIAN_ARGS_PATHS)
	UNSET(ILLYRIAN_ARGS_TARGETS)
ENDMACRO()

FUNCTION(ILLYRIAN_FIND_PYTHON_HELPER VAR NAME FILE)
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		"REQUIRED"
		""
		""
		"${ARGN}"
	)
	IF(ILLYRIAN_ARGS_REQUIRED AND NOT ${VAR})
		MESSAGE(FATAL_ERROR "Unable to locate ${FILE} in ${Python3_SITELIB}/${NAME} or ${Python3_USERLIB}/${NAME}")
	ENDIF()
ENDFUNCTION()

FUNCTION(ILLYRIAN_FIND_PYTHON_PATH VAR NAME FILE)
	ILLYRIAN_FIND_PYTHON()
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		""
		"PATHS"
		"${ARGN}"
	)
	IF(NOT ILLYRIAN_ARGS_PATHS)
		SET(PATHS "${Python3_SITELIB}/${NAME}" "${Python3_USERLIB}/${NAME}")
	ELSE()
		SET(PATHS)
		FOREACH(PATH ${ILLYRIAN_ARGS_PATHS})
			LIST(APPEND PATHS "${Python3_SITELIB}/${NAME}/${PATH}")
			LIST(APPEND PATHS "${Python3_USERLIB}/${NAME}/${PATH}")
		ENDFOREACH()
	ENDIF()
	FIND_PATH(${VAR} ${FILE} PATHS ${PATHS})
	ILLYRIAN_FIND_PYTHON_HELPER(${VAR} ${NAME} ${FILE} ${ARGN})
ENDFUNCTION()

FUNCTION(ILLYRIAN_FIND_PYTHON_FILE VAR NAME FILE)
	ILLYRIAN_FIND_PYTHON()
	CMAKE_PARSE_ARGUMENTS(ILLYRIAN_ARGS
		""
		""
		"PATHS"
		"${ARGN}"
	)
	IF(NOT ILLYRIAN_ARGS_PATHS)
		SET(PATHS "${Python3_SITELIB}/${NAME}" "${Python3_USERLIB}/${NAME}")
	ELSE()
		SET(PATHS)
		FOREACH(PATH ${ILLYRIAN_ARGS_PATHS})
			LIST(APPEND PATHS "${Python3_SITELIB}/${NAME}/${PATH}")
			LIST(APPEND PATHS "${Python3_USERLIB}/${NAME}/${PATH}")
		ENDFOREACH()
	ENDIF()
	FIND_FILE(${VAR} ${FILE} PATHS ${PATHS})
	ILLYRIAN_FIND_PYTHON_HELPER(${VAR} ${NAME} ${FILE} ${ARGN})
ENDFUNCTION()