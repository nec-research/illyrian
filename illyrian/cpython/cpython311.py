CPYTHON311 = ('cp311-cp311', set((	
	'PyAIter_Check',
	'PyArg_Parse',
	'PyArg_ParseTuple',
	'PyArg_ParseTupleAndKeywords',
	'PyArg_UnpackTuple',
	'PyArg_VaParse',
	'PyArg_VaParseTupleAndKeywords',
	'PyArg_ValidateKeywordArguments',
	'PyAsyncGen_New',
	'PyBool_FromLong',
	'PyBuffer_FillContiguousStrides',
	'PyBuffer_FillInfo',
	'PyBuffer_FromContiguous',
	'PyBuffer_GetPointer',
	'PyBuffer_IsContiguous',
	'PyBuffer_Release',
	'PyBuffer_SizeFromFormat',
	'PyBuffer_ToContiguous',
	'PyByteArray_AsString',
	'PyByteArray_Concat',
	'PyByteArray_FromObject',
	'PyByteArray_FromStringAndSize',
	'PyByteArray_Resize',
	'PyByteArray_Size',
	'PyBytes_AsString',
	'PyBytes_AsStringAndSize',
	'PyBytes_Concat',
	'PyBytes_ConcatAndDel',
	'PyBytes_DecodeEscape',
	'PyBytes_FromFormat',
	'PyBytes_FromFormatV',
	'PyBytes_FromObject',
	'PyBytes_FromString',
	'PyBytes_FromStringAndSize',
	'PyBytes_Repr',
	'PyBytes_Size',
	'PyCFunction_Call',
	'PyCFunction_GetFlags',
	'PyCFunction_GetFunction',
	'PyCFunction_GetSelf',
	'PyCFunction_New',
	'PyCFunction_NewEx',
	'PyCMethod_New',
	'PyCallIter_New',
	'PyCallable_Check',
	'PyCapsule_GetContext',
	'PyCapsule_GetDestructor',
	'PyCapsule_GetName',
	'PyCapsule_GetPointer',
	'PyCapsule_Import',
	'PyCapsule_IsValid',
	'PyCapsule_New',
	'PyCapsule_SetContext',
	'PyCapsule_SetDestructor',
	'PyCapsule_SetName',
	'PyCapsule_SetPointer',
	'PyCell_Get',
	'PyCell_New',
	'PyCell_Set',
	'PyClassMethod_New',
	'PyCode_Addr2Line',
	'PyCode_Addr2Location',
	'PyCode_GetCellvars',
	'PyCode_GetCode',
	'PyCode_GetFreevars',
	'PyCode_GetVarnames',
	'PyCode_New',
	'PyCode_NewEmpty',
	'PyCode_NewWithPosOnlyArgs',
	'PyCode_Optimize',
	'PyCodec_BackslashReplaceErrors',
	'PyCodec_Decode',
	'PyCodec_Decoder',
	'PyCodec_Encode',
	'PyCodec_Encoder',
	'PyCodec_IgnoreErrors',
	'PyCodec_IncrementalDecoder',
	'PyCodec_IncrementalEncoder',
	'PyCodec_KnownEncoding',
	'PyCodec_LookupError',
	'PyCodec_NameReplaceErrors',
	'PyCodec_Register',
	'PyCodec_RegisterError',
	'PyCodec_ReplaceErrors',
	'PyCodec_StreamReader',
	'PyCodec_StreamWriter',
	'PyCodec_StrictErrors',
	'PyCodec_Unregister',
	'PyCodec_XMLCharRefReplaceErrors',
	'PyCompile_OpcodeStackEffect',
	'PyCompile_OpcodeStackEffectWithJump',
	'PyComplex_AsCComplex',
	'PyComplex_FromCComplex',
	'PyComplex_FromDoubles',
	'PyComplex_ImagAsDouble',
	'PyComplex_RealAsDouble',
	'PyConfig_Clear',
	'PyConfig_InitIsolatedConfig',
	'PyConfig_InitPythonConfig',
	'PyConfig_Read',
	'PyConfig_SetArgv',
	'PyConfig_SetBytesArgv',
	'PyConfig_SetBytesString',
	'PyConfig_SetString',
	'PyConfig_SetWideStringList',
	'PyContextVar_Get',
	'PyContextVar_New',
	'PyContextVar_Reset',
	'PyContextVar_Set',
	'PyContext_Copy',
	'PyContext_CopyCurrent',
	'PyContext_Enter',
	'PyContext_Exit',
	'PyContext_New',
	'PyCoro_New',
	'PyDescr_IsData',
	'PyDescr_NewClassMethod',
	'PyDescr_NewGetSet',
	'PyDescr_NewMember',
	'PyDescr_NewMethod',
	'PyDescr_NewWrapper',
	'PyDictProxy_New',
	'PyDict_Clear',
	'PyDict_Contains',
	'PyDict_Copy',
	'PyDict_DelItem',
	'PyDict_DelItemString',
	'PyDict_GetItem',
	'PyDict_GetItemString',
	'PyDict_GetItemWithError',
	'PyDict_Items',
	'PyDict_Keys',
	'PyDict_Merge',
	'PyDict_MergeFromSeq2',
	'PyDict_New',
	'PyDict_Next',
	'PyDict_SetDefault',
	'PyDict_SetItem',
	'PyDict_SetItemString',
	'PyDict_Size',
	'PyDict_Update',
	'PyDict_Values',
	'PyErr_BadArgument',
	'PyErr_BadInternalCall',
	'PyErr_CheckSignals',
	'PyErr_Clear',
	'PyErr_Display',
	'PyErr_ExceptionMatches',
	'PyErr_Fetch',
	'PyErr_Format',
	'PyErr_FormatV',
	'PyErr_GetExcInfo',
	'PyErr_GetHandledException',
	'PyErr_GivenExceptionMatches',
	'PyErr_NewException',
	'PyErr_NewExceptionWithDoc',
	'PyErr_NoMemory',
	'PyErr_NormalizeException',
	'PyErr_Occurred',
	'PyErr_Print',
	'PyErr_PrintEx',
	'PyErr_ProgramText',
	'PyErr_ProgramTextObject',
	'PyErr_RangedSyntaxLocationObject',
	'PyErr_ResourceWarning',
	'PyErr_Restore',
	'PyErr_SetExcInfo',
	'PyErr_SetFromErrno',
	'PyErr_SetFromErrnoWithFilename',
	'PyErr_SetFromErrnoWithFilenameObject',
	'PyErr_SetFromErrnoWithFilenameObjects',
	'PyErr_SetHandledException',
	'PyErr_SetImportError',
	'PyErr_SetImportErrorSubclass',
	'PyErr_SetInterrupt',
	'PyErr_SetInterruptEx',
	'PyErr_SetNone',
	'PyErr_SetObject',
	'PyErr_SetString',
	'PyErr_SyntaxLocation',
	'PyErr_SyntaxLocationEx',
	'PyErr_SyntaxLocationObject',
	'PyErr_WarnEx',
	'PyErr_WarnExplicit',
	'PyErr_WarnExplicitFormat',
	'PyErr_WarnExplicitObject',
	'PyErr_WarnFormat',
	'PyErr_WriteUnraisable',
	'PyEval_AcquireLock',
	'PyEval_AcquireThread',
	'PyEval_CallFunction',
	'PyEval_CallMethod',
	'PyEval_CallObjectWithKeywords',
	'PyEval_EvalCode',
	'PyEval_EvalCodeEx',
	'PyEval_EvalFrame',
	'PyEval_EvalFrameEx',
	'PyEval_GetBuiltins',
	'PyEval_GetFrame',
	'PyEval_GetFuncDesc',
	'PyEval_GetFuncName',
	'PyEval_GetGlobals',
	'PyEval_GetLocals',
	'PyEval_InitThreads',
	'PyEval_MergeCompilerFlags',
	'PyEval_ReleaseLock',
	'PyEval_ReleaseThread',
	'PyEval_RestoreThread',
	'PyEval_SaveThread',
	'PyEval_SetProfile',
	'PyEval_SetTrace',
	'PyEval_ThreadsInitialized',
	'PyExceptionClass_Name',
	'PyException_GetCause',
	'PyException_GetContext',
	'PyException_GetTraceback',
	'PyException_SetCause',
	'PyException_SetContext',
	'PyException_SetTraceback',
	'PyFile_FromFd',
	'PyFile_GetLine',
	'PyFile_NewStdPrinter',
	'PyFile_OpenCode',
	'PyFile_OpenCodeObject',
	'PyFile_SetOpenCodeHook',
	'PyFile_WriteObject',
	'PyFile_WriteString',
	'PyFloat_AsDouble',
	'PyFloat_FromDouble',
	'PyFloat_FromString',
	'PyFloat_GetInfo',
	'PyFloat_GetMax',
	'PyFloat_GetMin',
	'PyFloat_Pack2',
	'PyFloat_Pack4',
	'PyFloat_Pack8',
	'PyFloat_Unpack2',
	'PyFloat_Unpack4',
	'PyFloat_Unpack8',
	'PyFrame_FastToLocals',
	'PyFrame_FastToLocalsWithError',
	'PyFrame_GetBack',
	'PyFrame_GetBuiltins',
	'PyFrame_GetCode',
	'PyFrame_GetGenerator',
	'PyFrame_GetGlobals',
	'PyFrame_GetLasti',
	'PyFrame_GetLineNumber',
	'PyFrame_GetLocals',
	'PyFrame_LocalsToFast',
	'PyFrame_New',
	'PyFrozenSet_New',
	'PyFunction_GetAnnotations',
	'PyFunction_GetClosure',
	'PyFunction_GetCode',
	'PyFunction_GetDefaults',
	'PyFunction_GetGlobals',
	'PyFunction_GetKwDefaults',
	'PyFunction_GetModule',
	'PyFunction_New',
	'PyFunction_NewWithQualName',
	'PyFunction_SetAnnotations',
	'PyFunction_SetClosure',
	'PyFunction_SetDefaults',
	'PyFunction_SetKwDefaults',
	'PyGC_Collect',
	'PyGC_Disable',
	'PyGC_Enable',
	'PyGC_IsEnabled',
	'PyGILState_Check',
	'PyGILState_Ensure',
	'PyGILState_GetThisThreadState',
	'PyGILState_Release',
	'PyGen_New',
	'PyGen_NewWithQualName',
	'PyHash_GetFuncDef',
	'PyImport_AddModule',
	'PyImport_AddModuleObject',
	'PyImport_AppendInittab',
	'PyImport_ExecCodeModule',
	'PyImport_ExecCodeModuleEx',
	'PyImport_ExecCodeModuleObject',
	'PyImport_ExecCodeModuleWithPathnames',
	'PyImport_ExtendInittab',
	'PyImport_GetImporter',
	'PyImport_GetMagicNumber',
	'PyImport_GetMagicTag',
	'PyImport_GetModule',
	'PyImport_GetModuleDict',
	'PyImport_Import',
	'PyImport_ImportFrozenModule',
	'PyImport_ImportFrozenModuleObject',
	'PyImport_ImportModule',
	'PyImport_ImportModuleLevel',
	'PyImport_ImportModuleLevelObject',
	'PyImport_ImportModuleNoBlock',
	'PyImport_ReloadModule',
	'PyIndex_Check',
	'PyInit__abc',
	'PyInit__ast',
	'PyInit__codecs',
	'PyInit__collections',
	'PyInit__functools',
	'PyInit__imp',
	'PyInit__io',
	'PyInit__locale',
	'PyInit__operator',
	'PyInit__signal',
	'PyInit__sre',
	'PyInit__stat',
	'PyInit__string',
	'PyInit__symtable',
	'PyInit__thread',
	'PyInit__tokenize',
	'PyInit__tracemalloc',
	'PyInit__weakref',
	'PyInit_atexit',
	'PyInit_errno',
	'PyInit_faulthandler',
	'PyInit_gc',
	'PyInit_itertools',
	'PyInit_posix',
	'PyInit_pwd',
	'PyInit_time',
	'PyInit_xxsubtype',
	'PyInstanceMethod_Function',
	'PyInstanceMethod_New',
	'PyInterpreterState_Clear',
	'PyInterpreterState_Delete',
	'PyInterpreterState_Get',
	'PyInterpreterState_GetDict',
	'PyInterpreterState_GetID',
	'PyInterpreterState_Head',
	'PyInterpreterState_Main',
	'PyInterpreterState_New',
	'PyInterpreterState_Next',
	'PyInterpreterState_ThreadHead',
	'PyIter_Check',
	'PyIter_Next',
	'PyIter_Send',
	'PyList_Append',
	'PyList_AsTuple',
	'PyList_GetItem',
	'PyList_GetSlice',
	'PyList_Insert',
	'PyList_New',
	'PyList_Reverse',
	'PyList_SetItem',
	'PyList_SetSlice',
	'PyList_Size',
	'PyList_Sort',
	'PyLong_AsDouble',
	'PyLong_AsLong',
	'PyLong_AsLongAndOverflow',
	'PyLong_AsLongLong',
	'PyLong_AsLongLongAndOverflow',
	'PyLong_AsSize_t',
	'PyLong_AsSsize_t',
	'PyLong_AsUnsignedLong',
	'PyLong_AsUnsignedLongLong',
	'PyLong_AsUnsignedLongLongMask',
	'PyLong_AsUnsignedLongMask',
	'PyLong_AsVoidPtr',
	'PyLong_FromDouble',
	'PyLong_FromLong',
	'PyLong_FromLongLong',
	'PyLong_FromSize_t',
	'PyLong_FromSsize_t',
	'PyLong_FromString',
	'PyLong_FromUnicodeObject',
	'PyLong_FromUnsignedLong',
	'PyLong_FromUnsignedLongLong',
	'PyLong_FromVoidPtr',
	'PyLong_GetInfo',
	'PyMapping_Check',
	'PyMapping_GetItemString',
	'PyMapping_HasKey',
	'PyMapping_HasKeyString',
	'PyMapping_Items',
	'PyMapping_Keys',
	'PyMapping_Length',
	'PyMapping_SetItemString',
	'PyMapping_Size',
	'PyMapping_Values',
	'PyMarshal_Init',
	'PyMarshal_ReadLastObjectFromFile',
	'PyMarshal_ReadLongFromFile',
	'PyMarshal_ReadObjectFromFile',
	'PyMarshal_ReadObjectFromString',
	'PyMarshal_ReadShortFromFile',
	'PyMarshal_WriteLongToFile',
	'PyMarshal_WriteObjectToFile',
	'PyMarshal_WriteObjectToString',
	'PyMem_Calloc',
	'PyMem_Free',
	'PyMem_GetAllocator',
	'PyMem_Malloc',
	'PyMem_RawCalloc',
	'PyMem_RawFree',
	'PyMem_RawMalloc',
	'PyMem_RawRealloc',
	'PyMem_Realloc',
	'PyMem_SetAllocator',
	'PyMem_SetupDebugHooks',
	'PyMember_GetOne',
	'PyMember_SetOne',
	'PyMemoryView_FromBuffer',
	'PyMemoryView_FromMemory',
	'PyMemoryView_FromObject',
	'PyMemoryView_GetContiguous',
	'PyMethod_Function',
	'PyMethod_New',
	'PyMethod_Self',
	'PyModuleDef_Init',
	'PyModule_AddFunctions',
	'PyModule_AddIntConstant',
	'PyModule_AddObject',
	'PyModule_AddObjectRef',
	'PyModule_AddStringConstant',
	'PyModule_AddType',
	'PyModule_Create2',
	'PyModule_ExecDef',
	'PyModule_FromDefAndSpec2',
	'PyModule_GetDef',
	'PyModule_GetDict',
	'PyModule_GetFilename',
	'PyModule_GetFilenameObject',
	'PyModule_GetName',
	'PyModule_GetNameObject',
	'PyModule_GetState',
	'PyModule_New',
	'PyModule_NewObject',
	'PyModule_SetDocString',
	'PyNumber_Absolute',
	'PyNumber_Add',
	'PyNumber_And',
	'PyNumber_AsSsize_t',
	'PyNumber_Check',
	'PyNumber_Divmod',
	'PyNumber_Float',
	'PyNumber_FloorDivide',
	'PyNumber_InPlaceAdd',
	'PyNumber_InPlaceAnd',
	'PyNumber_InPlaceFloorDivide',
	'PyNumber_InPlaceLshift',
	'PyNumber_InPlaceMatrixMultiply',
	'PyNumber_InPlaceMultiply',
	'PyNumber_InPlaceOr',
	'PyNumber_InPlacePower',
	'PyNumber_InPlaceRemainder',
	'PyNumber_InPlaceRshift',
	'PyNumber_InPlaceSubtract',
	'PyNumber_InPlaceTrueDivide',
	'PyNumber_InPlaceXor',
	'PyNumber_Index',
	'PyNumber_Invert',
	'PyNumber_Long',
	'PyNumber_Lshift',
	'PyNumber_MatrixMultiply',
	'PyNumber_Multiply',
	'PyNumber_Negative',
	'PyNumber_Or',
	'PyNumber_Positive',
	'PyNumber_Power',
	'PyNumber_Remainder',
	'PyNumber_Rshift',
	'PyNumber_Subtract',
	'PyNumber_ToBase',
	'PyNumber_TrueDivide',
	'PyNumber_Xor',
	'PyODict_DelItem',
	'PyODict_New',
	'PyODict_SetItem',
	'PyOS_AfterFork',
	'PyOS_AfterFork_Child',
	'PyOS_AfterFork_Parent',
	'PyOS_BeforeFork',
	'PyOS_FSPath',
	'PyOS_InterruptOccurred',
	'PyOS_Readline',
	'PyOS_double_to_string',
	'PyOS_getsig',
	'PyOS_mystricmp',
	'PyOS_mystrnicmp',
	'PyOS_setsig',
	'PyOS_snprintf',
	'PyOS_string_to_double',
	'PyOS_strtol',
	'PyOS_strtoul',
	'PyOS_vsnprintf',
	'PyObject_ASCII',
	'PyObject_AsCharBuffer',
	'PyObject_AsFileDescriptor',
	'PyObject_AsReadBuffer',
	'PyObject_AsWriteBuffer',
	'PyObject_Bytes',
	'PyObject_Call',
	'PyObject_CallFinalizer',
	'PyObject_CallFinalizerFromDealloc',
	'PyObject_CallFunction',
	'PyObject_CallFunctionObjArgs',
	'PyObject_CallMethod',
	'PyObject_CallMethodObjArgs',
	'PyObject_CallNoArgs',
	'PyObject_CallObject',
	'PyObject_CallOneArg',
	'PyObject_Calloc',
	'PyObject_CheckBuffer',
	'PyObject_CheckReadBuffer',
	'PyObject_ClearWeakRefs',
	'PyObject_CopyData',
	'PyObject_DelItem',
	'PyObject_DelItemString',
	'PyObject_Dir',
	'PyObject_Format',
	'PyObject_Free',
	'PyObject_GC_Del',
	'PyObject_GC_IsFinalized',
	'PyObject_GC_IsTracked',
	'PyObject_GC_Track',
	'PyObject_GC_UnTrack',
	'PyObject_GET_WEAKREFS_LISTPTR',
	'PyObject_GenericGetAttr',
	'PyObject_GenericGetDict',
	'PyObject_GenericSetAttr',
	'PyObject_GenericSetDict',
	'PyObject_GetAIter',
	'PyObject_GetArenaAllocator',
	'PyObject_GetAttr',
	'PyObject_GetAttrString',
	'PyObject_GetBuffer',
	'PyObject_GetItem',
	'PyObject_GetIter',
	'PyObject_HasAttr',
	'PyObject_HasAttrString',
	'PyObject_Hash',
	'PyObject_HashNotImplemented',
	'PyObject_IS_GC',
	'PyObject_Init',
	'PyObject_InitVar',
	'PyObject_IsInstance',
	'PyObject_IsSubclass',
	'PyObject_IsTrue',
	'PyObject_Length',
	'PyObject_LengthHint',
	'PyObject_Malloc',
	'PyObject_Not',
	'PyObject_Print',
	'PyObject_Realloc',
	'PyObject_Repr',
	'PyObject_RichCompare',
	'PyObject_RichCompareBool',
	'PyObject_SelfIter',
	'PyObject_SetArenaAllocator',
	'PyObject_SetAttr',
	'PyObject_SetAttrString',
	'PyObject_SetItem',
	'PyObject_Size',
	'PyObject_Str',
	'PyObject_Type',
	'PyObject_Vectorcall',
	'PyObject_VectorcallDict',
	'PyObject_VectorcallMethod',
	'PyPickleBuffer_FromObject',
	'PyPickleBuffer_GetBuffer',
	'PyPickleBuffer_Release',
	'PyPreConfig_InitIsolatedConfig',
	'PyPreConfig_InitPythonConfig',
	'PyRun_AnyFile',
	'PyRun_AnyFileEx',
	'PyRun_AnyFileExFlags',
	'PyRun_AnyFileFlags',
	'PyRun_File',
	'PyRun_FileEx',
	'PyRun_FileExFlags',
	'PyRun_FileFlags',
	'PyRun_InteractiveLoop',
	'PyRun_InteractiveLoopFlags',
	'PyRun_InteractiveOne',
	'PyRun_InteractiveOneFlags',
	'PyRun_InteractiveOneObject',
	'PyRun_SimpleFile',
	'PyRun_SimpleFileEx',
	'PyRun_SimpleFileExFlags',
	'PyRun_SimpleString',
	'PyRun_SimpleStringFlags',
	'PyRun_String',
	'PyRun_StringFlags',
	'PySeqIter_New',
	'PySequence_Check',
	'PySequence_Concat',
	'PySequence_Contains',
	'PySequence_Count',
	'PySequence_DelItem',
	'PySequence_DelSlice',
	'PySequence_Fast',
	'PySequence_GetItem',
	'PySequence_GetSlice',
	'PySequence_In',
	'PySequence_InPlaceConcat',
	'PySequence_InPlaceRepeat',
	'PySequence_Index',
	'PySequence_Length',
	'PySequence_List',
	'PySequence_Repeat',
	'PySequence_SetItem',
	'PySequence_SetSlice',
	'PySequence_Size',
	'PySequence_Tuple',
	'PySet_Add',
	'PySet_Clear',
	'PySet_Contains',
	'PySet_Discard',
	'PySet_New',
	'PySet_Pop',
	'PySet_Size',
	'PySlice_AdjustIndices',
	'PySlice_GetIndices',
	'PySlice_GetIndicesEx',
	'PySlice_New',
	'PySlice_Unpack',
	'PyState_AddModule',
	'PyState_FindModule',
	'PyState_RemoveModule',
	'PyStaticMethod_New',
	'PyStatus_Error',
	'PyStatus_Exception',
	'PyStatus_Exit',
	'PyStatus_IsError',
	'PyStatus_IsExit',
	'PyStatus_NoMemory',
	'PyStatus_Ok',
	'PyStructSequence_GetItem',
	'PyStructSequence_InitType',
	'PyStructSequence_InitType2',
	'PyStructSequence_New',
	'PyStructSequence_NewType',
	'PyStructSequence_SetItem',
	'PySymtable_Lookup',
	'PySys_AddAuditHook',
	'PySys_AddWarnOption',
	'PySys_AddWarnOptionUnicode',
	'PySys_AddXOption',
	'PySys_Audit',
	'PySys_FormatStderr',
	'PySys_FormatStdout',
	'PySys_GetObject',
	'PySys_GetXOptions',
	'PySys_HasWarnOptions',
	'PySys_ResetWarnOptions',
	'PySys_SetArgv',
	'PySys_SetArgvEx',
	'PySys_SetObject',
	'PySys_SetPath',
	'PySys_WriteStderr',
	'PySys_WriteStdout',
	'PyThreadState_Clear',
	'PyThreadState_Delete',
	'PyThreadState_DeleteCurrent',
	'PyThreadState_EnterTracing',
	'PyThreadState_Get',
	'PyThreadState_GetDict',
	'PyThreadState_GetFrame',
	'PyThreadState_GetID',
	'PyThreadState_GetInterpreter',
	'PyThreadState_LeaveTracing',
	'PyThreadState_New',
	'PyThreadState_Next',
	'PyThreadState_SetAsyncExc',
	'PyThreadState_Swap',
	'PyThread_GetInfo',
	'PyThread_ReInitTLS',
	'PyThread_acquire_lock',
	'PyThread_acquire_lock_timed',
	'PyThread_allocate_lock',
	'PyThread_create_key',
	'PyThread_delete_key',
	'PyThread_delete_key_value',
	'PyThread_exit_thread',
	'PyThread_free_lock',
	'PyThread_get_key_value',
	'PyThread_get_stacksize',
	'PyThread_get_thread_ident',
	'PyThread_get_thread_native_id',
	'PyThread_init_thread',
	'PyThread_release_lock',
	'PyThread_set_key_value',
	'PyThread_set_stacksize',
	'PyThread_start_new_thread',
	'PyThread_tss_alloc',
	'PyThread_tss_create',
	'PyThread_tss_delete',
	'PyThread_tss_free',
	'PyThread_tss_get',
	'PyThread_tss_is_created',
	'PyThread_tss_set',
	'PyToken_OneChar',
	'PyToken_ThreeChars',
	'PyToken_TwoChars',
	'PyTraceBack_Here',
	'PyTraceBack_Print',
	'PyTraceMalloc_Track',
	'PyTraceMalloc_Untrack',
	'PyTuple_GetItem',
	'PyTuple_GetSlice',
	'PyTuple_New',
	'PyTuple_Pack',
	'PyTuple_SetItem',
	'PyTuple_Size',
	'PyType_ClearCache',
	'PyType_FromModuleAndSpec',
	'PyType_FromSpec',
	'PyType_FromSpecWithBases',
	'PyType_GenericAlloc',
	'PyType_GenericNew',
	'PyType_GetFlags',
	'PyType_GetModule',
	'PyType_GetModuleByDef',
	'PyType_GetModuleState',
	'PyType_GetName',
	'PyType_GetQualName',
	'PyType_GetSlot',
	'PyType_IsSubtype',
	'PyType_Modified',
	'PyType_Ready',
	'PyType_SUPPORTS_WEAKREFS',
	'PyUnicodeDecodeError_Create',
	'PyUnicodeDecodeError_GetEncoding',
	'PyUnicodeDecodeError_GetEnd',
	'PyUnicodeDecodeError_GetObject',
	'PyUnicodeDecodeError_GetReason',
	'PyUnicodeDecodeError_GetStart',
	'PyUnicodeDecodeError_SetEnd',
	'PyUnicodeDecodeError_SetReason',
	'PyUnicodeDecodeError_SetStart',
	'PyUnicodeEncodeError_GetEncoding',
	'PyUnicodeEncodeError_GetEnd',
	'PyUnicodeEncodeError_GetObject',
	'PyUnicodeEncodeError_GetReason',
	'PyUnicodeEncodeError_GetStart',
	'PyUnicodeEncodeError_SetEnd',
	'PyUnicodeEncodeError_SetReason',
	'PyUnicodeEncodeError_SetStart',
	'PyUnicodeTranslateError_GetEnd',
	'PyUnicodeTranslateError_GetObject',
	'PyUnicodeTranslateError_GetReason',
	'PyUnicodeTranslateError_GetStart',
	'PyUnicodeTranslateError_SetEnd',
	'PyUnicodeTranslateError_SetReason',
	'PyUnicodeTranslateError_SetStart',
	'PyUnicode_Append',
	'PyUnicode_AppendAndDel',
	'PyUnicode_AsASCIIString',
	'PyUnicode_AsCharmapString',
	'PyUnicode_AsDecodedObject',
	'PyUnicode_AsDecodedUnicode',
	'PyUnicode_AsEncodedObject',
	'PyUnicode_AsEncodedString',
	'PyUnicode_AsEncodedUnicode',
	'PyUnicode_AsLatin1String',
	'PyUnicode_AsRawUnicodeEscapeString',
	'PyUnicode_AsUCS4',
	'PyUnicode_AsUCS4Copy',
	'PyUnicode_AsUTF16String',
	'PyUnicode_AsUTF32String',
	'PyUnicode_AsUTF8',
	'PyUnicode_AsUTF8AndSize',
	'PyUnicode_AsUTF8String',
	'PyUnicode_AsUnicode',
	'PyUnicode_AsUnicodeAndSize',
	'PyUnicode_AsUnicodeEscapeString',
	'PyUnicode_AsWideChar',
	'PyUnicode_AsWideCharString',
	'PyUnicode_BuildEncodingMap',
	'PyUnicode_Compare',
	'PyUnicode_CompareWithASCIIString',
	'PyUnicode_Concat',
	'PyUnicode_Contains',
	'PyUnicode_CopyCharacters',
	'PyUnicode_Count',
	'PyUnicode_Decode',
	'PyUnicode_DecodeASCII',
	'PyUnicode_DecodeCharmap',
	'PyUnicode_DecodeFSDefault',
	'PyUnicode_DecodeFSDefaultAndSize',
	'PyUnicode_DecodeLatin1',
	'PyUnicode_DecodeLocale',
	'PyUnicode_DecodeLocaleAndSize',
	'PyUnicode_DecodeRawUnicodeEscape',
	'PyUnicode_DecodeUTF16',
	'PyUnicode_DecodeUTF16Stateful',
	'PyUnicode_DecodeUTF32',
	'PyUnicode_DecodeUTF32Stateful',
	'PyUnicode_DecodeUTF7',
	'PyUnicode_DecodeUTF7Stateful',
	'PyUnicode_DecodeUTF8',
	'PyUnicode_DecodeUTF8Stateful',
	'PyUnicode_DecodeUnicodeEscape',
	'PyUnicode_EncodeFSDefault',
	'PyUnicode_EncodeLocale',
	'PyUnicode_FSConverter',
	'PyUnicode_FSDecoder',
	'PyUnicode_Fill',
	'PyUnicode_Find',
	'PyUnicode_FindChar',
	'PyUnicode_Format',
	'PyUnicode_FromEncodedObject',
	'PyUnicode_FromFormat',
	'PyUnicode_FromFormatV',
	'PyUnicode_FromKindAndData',
	'PyUnicode_FromObject',
	'PyUnicode_FromOrdinal',
	'PyUnicode_FromString',
	'PyUnicode_FromStringAndSize',
	'PyUnicode_FromUnicode',
	'PyUnicode_FromWideChar',
	'PyUnicode_GetDefaultEncoding',
	'PyUnicode_GetLength',
	'PyUnicode_GetSize',
	'PyUnicode_InternFromString',
	'PyUnicode_InternImmortal',
	'PyUnicode_InternInPlace',
	'PyUnicode_IsIdentifier',
	'PyUnicode_Join',
	'PyUnicode_New',
	'PyUnicode_Partition',
	'PyUnicode_RPartition',
	'PyUnicode_RSplit',
	'PyUnicode_ReadChar',
	'PyUnicode_Replace',
	'PyUnicode_Resize',
	'PyUnicode_RichCompare',
	'PyUnicode_Split',
	'PyUnicode_Splitlines',
	'PyUnicode_Substring',
	'PyUnicode_Tailmatch',
	'PyUnicode_Translate',
	'PyUnicode_WriteChar',
	'PyVectorcall_Call',
	'PyVectorcall_Function',
	'PyWeakref_GetObject',
	'PyWeakref_NewProxy',
	'PyWeakref_NewRef',
	'PyWideStringList_Append',
	'PyWideStringList_Insert',
	'PyWrapper_New',
	'Py_AddPendingCall',
	'Py_AtExit',
	'Py_BuildValue',
	'Py_BytesMain',
	'Py_CompileString',
	'Py_CompileStringExFlags',
	'Py_CompileStringFlags',
	'Py_CompileStringObject',
	'Py_DecRef',
	'Py_DecodeLocale',
	'Py_EncodeLocale',
	'Py_EndInterpreter',
	'Py_EnterRecursiveCall',
	'Py_Exit',
	'Py_ExitStatusException',
	'Py_FatalError',
	'Py_FdIsInteractive',
	'Py_Finalize',
	'Py_FinalizeEx',
	'Py_FrozenMain',
	'Py_GETENV',
	'Py_GenericAlias',
	'Py_GetArgcArgv',
	'Py_GetBuildInfo',
	'Py_GetCompiler',
	'Py_GetCopyright',
	'Py_GetExecPrefix',
	'Py_GetPath',
	'Py_GetPlatform',
	'Py_GetPrefix',
	'Py_GetProgramFullPath',
	'Py_GetProgramName',
	'Py_GetPythonHome',
	'Py_GetRecursionLimit',
	'Py_GetVersion',
	'Py_IncRef',
	'Py_Initialize',
	'Py_InitializeEx',
	'Py_InitializeFromConfig',
	'Py_Is',
	'Py_IsFalse',
	'Py_IsInitialized',
	'Py_IsNone',
	'Py_IsTrue',
	'Py_LeaveRecursiveCall',
	'Py_Main',
	'Py_MakePendingCalls',
	'Py_NewInterpreter',
	'Py_NewRef',
	'Py_PreInitialize',
	'Py_PreInitializeFromArgs',
	'Py_PreInitializeFromBytesArgs',
	'Py_ReprEnter',
	'Py_ReprLeave',
	'Py_RunMain',
	'Py_SetPath',
	'Py_SetProgramName',
	'Py_SetPythonHome',
	'Py_SetRecursionLimit',
	'Py_SetStandardStreamEncoding',
	'Py_UniversalNewlineFgets',
	'Py_VaBuildValue',
	'Py_XNewRef',
	'_PyAST_Compile',
	'_PyAccu_Accumulate',
	'_PyAccu_Destroy',
	'_PyAccu_Finish',
	'_PyAccu_FinishAsList',
	'_PyAccu_Init',
	'_PyArena_AddPyObject',
	'_PyArena_Free',
	'_PyArena_Malloc',
	'_PyArena_New',
	'_PyArg_BadArgument',
	'_PyArg_CheckPositional',
	'_PyArg_NoKeywords',
	'_PyArg_NoKwnames',
	'_PyArg_NoPositional',
	'_PyArg_ParseStack',
	'_PyArg_ParseStackAndKeywords',
	'_PyArg_ParseStackAndKeywords_SizeT',
	'_PyArg_ParseStack_SizeT',
	'_PyArg_ParseTupleAndKeywordsFast',
	'_PyArg_ParseTupleAndKeywordsFast_SizeT',
	'_PyArg_ParseTupleAndKeywords_SizeT',
	'_PyArg_ParseTuple_SizeT',
	'_PyArg_Parse_SizeT',
	'_PyArg_UnpackKeywords',
	'_PyArg_UnpackKeywordsWithVararg',
	'_PyArg_UnpackStack',
	'_PyArg_VaParseTupleAndKeywordsFast',
	'_PyArg_VaParseTupleAndKeywordsFast_SizeT',
	'_PyArg_VaParseTupleAndKeywords_SizeT',
	'_PyArg_VaParse_SizeT',
	'_PyArgv_AsWstrList',
	'_PyBytesWriter_Alloc',
	'_PyBytesWriter_Dealloc',
	'_PyBytesWriter_Finish',
	'_PyBytesWriter_Init',
	'_PyBytesWriter_Prepare',
	'_PyBytesWriter_Resize',
	'_PyBytesWriter_WriteBytes',
	'_PyBytes_DecodeEscape',
	'_PyBytes_Find',
	'_PyBytes_FormatEx',
	'_PyBytes_FromHex',
	'_PyBytes_Join',
	'_PyBytes_Repeat',
	'_PyBytes_Resize',
	'_PyBytes_ReverseFind',
	'_PyCode_CheckLineNumber',
	'_PyCode_ConstantKey',
	'_PyCode_GetExtra',
	'_PyCode_New',
	'_PyCode_SetExtra',
	'_PyCode_Validate',
	'_PyCodecInfo_GetIncrementalDecoder',
	'_PyCodecInfo_GetIncrementalEncoder',
	'_PyCodec_DecodeText',
	'_PyCodec_EncodeText',
	'_PyCodec_Lookup',
	'_PyCodec_LookupTextEncoding',
	'_PyConfig_AsDict',
	'_PyConfig_FromDict',
	'_PyConfig_InitCompatConfig',
	'_PyContext_NewHamtForTests',
	'_PyCrossInterpreterData_Lookup',
	'_PyCrossInterpreterData_NewObject',
	'_PyCrossInterpreterData_RegisterClass',
	'_PyCrossInterpreterData_Release',
	'_PyDeadline_Get',
	'_PyDeadline_Init',
	'_PyDebugAllocatorStats',
	'_PyDictView_Intersect',
	'_PyDictView_New',
	'_PyDict_CheckConsistency',
	'_PyDict_ContainsId',
	'_PyDict_Contains_KnownHash',
	'_PyDict_DebugMallocStats',
	'_PyDict_DelItemId',
	'_PyDict_DelItemIf',
	'_PyDict_DelItem_KnownHash',
	'_PyDict_GetItemIdWithError',
	'_PyDict_GetItemStringWithError',
	'_PyDict_GetItemWithError',
	'_PyDict_GetItem_KnownHash',
	'_PyDict_HasOnlyStringKeys',
	'_PyDict_MaybeUntrack',
	'_PyDict_MergeEx',
	'_PyDict_NewPresized',
	'_PyDict_Next',
	'_PyDict_Pop',
	'_PyDict_SetItemId',
	'_PyDict_SetItem_KnownHash',
	'_PyDict_SizeOf',
	'_PyErr_BadInternalCall',
	'_PyErr_ChainExceptions',
	'_PyErr_ChainStackItem',
	'_PyErr_CheckSignals',
	'_PyErr_CheckSignalsTstate',
	'_PyErr_Clear',
	'_PyErr_Display',
	'_PyErr_ExceptionMatches',
	'_PyErr_Fetch',
	'_PyErr_Format',
	'_PyErr_FormatFromCause',
	'_PyErr_FormatFromCauseTstate',
	'_PyErr_GetExcInfo',
	'_PyErr_GetHandledException',
	'_PyErr_GetTopmostException',
	'_PyErr_NoMemory',
	'_PyErr_NormalizeException',
	'_PyErr_Print',
	'_PyErr_ProgramDecodedTextObject',
	'_PyErr_Restore',
	'_PyErr_SetHandledException',
	'_PyErr_SetKeyError',
	'_PyErr_SetNone',
	'_PyErr_SetObject',
	'_PyErr_SetString',
	'_PyErr_StackItemToExcInfoTuple',
	'_PyErr_TrySetFromCause',
	'_PyErr_WriteUnraisableMsg',
	'_PyEval_AddPendingCall',
	'_PyEval_EvalFrameDefault',
	'_PyEval_GetBuiltin',
	'_PyEval_GetBuiltinId',
	'_PyEval_GetSwitchInterval',
	'_PyEval_RequestCodeExtraIndex',
	'_PyEval_SetProfile',
	'_PyEval_SetSwitchInterval',
	'_PyEval_SetTrace',
	'_PyEval_SignalAsyncExc',
	'_PyEval_SignalReceived',
	'_PyEval_SliceIndex',
	'_PyEval_SliceIndexNotNone',
	'_PyFloat_DebugMallocStats',
	'_PyFloat_FormatAdvancedWriter',
	'_PyFrame_IsEntryFrame',
	'_PyFunction_Vectorcall',
	'_PyGILState_GetInterpreterStateUnsafe',
	'_PyGen_FetchStopIterationValue',
	'_PyGen_Finalize',
	'_PyGen_SetStopIterationValue',
	'_PyImport_AcquireLock',
	'_PyImport_FixupBuiltin',
	'_PyImport_FixupExtensionObject',
	'_PyImport_GetModuleAttr',
	'_PyImport_GetModuleAttrString',
	'_PyImport_GetModuleId',
	'_PyImport_IsInitialized',
	'_PyImport_ReleaseLock',
	'_PyImport_SetModule',
	'_PyImport_SetModuleString',
	'_PyInterpreterID_LookUp',
	'_PyInterpreterID_New',
	'_PyInterpreterState_Enable',
	'_PyInterpreterState_GetConfig',
	'_PyInterpreterState_GetConfigCopy',
	'_PyInterpreterState_GetEvalFrameFunc',
	'_PyInterpreterState_GetIDObject',
	'_PyInterpreterState_GetMainModule',
	'_PyInterpreterState_IDDecref',
	'_PyInterpreterState_IDIncref',
	'_PyInterpreterState_IDInitref',
	'_PyInterpreterState_LookUpID',
	'_PyInterpreterState_RequireIDRef',
	'_PyInterpreterState_RequiresIDRef',
	'_PyInterpreterState_SetConfig',
	'_PyInterpreterState_SetEvalFrameFunc',
	'_PyList_DebugMallocStats',
	'_PyList_Extend',
	'_PyLong_AsByteArray',
	'_PyLong_AsInt',
	'_PyLong_AsTime_t',
	'_PyLong_Copy',
	'_PyLong_DivmodNear',
	'_PyLong_FileDescriptor_Converter',
	'_PyLong_Format',
	'_PyLong_FormatAdvancedWriter',
	'_PyLong_FormatBytesWriter',
	'_PyLong_FormatWriter',
	'_PyLong_Frexp',
	'_PyLong_FromByteArray',
	'_PyLong_FromBytes',
	'_PyLong_FromGid',
	'_PyLong_FromTime_t',
	'_PyLong_FromUid',
	'_PyLong_GCD',
	'_PyLong_Lshift',
	'_PyLong_New',
	'_PyLong_NumBits',
	'_PyLong_Rshift',
	'_PyLong_Sign',
	'_PyLong_Size_t_Converter',
	'_PyLong_UnsignedInt_Converter',
	'_PyLong_UnsignedLongLong_Converter',
	'_PyLong_UnsignedLong_Converter',
	'_PyLong_UnsignedShort_Converter',
	'_PyMem_GetAllocatorName',
	'_PyMem_GetCurrentAllocatorName',
	'_PyMem_RawStrdup',
	'_PyMem_RawWcsdup',
	'_PyMem_SetDefaultAllocator',
	'_PyMem_SetupAllocators',
	'_PyMem_Strdup',
	'_PyModuleSpec_IsInitializing',
	'_PyModule_Clear',
	'_PyModule_ClearDict',
	'_PyModule_CreateInitialized',
	'_PyNamespace_New',
	'_PyNumber_Index',
	'_PyOS_InterruptOccurred',
	'_PyOS_IsMainThread',
	'_PyOS_URandom',
	'_PyOS_URandomNonblock',
	'_PyObject_AssertFailed',
	'_PyObject_Call',
	'_PyObject_CallFunction_SizeT',
	'_PyObject_CallMethod',
	'_PyObject_CallMethodId',
	'_PyObject_CallMethodIdObjArgs',
	'_PyObject_CallMethodId_SizeT',
	'_PyObject_CallMethod_SizeT',
	'_PyObject_Call_Prepend',
	'_PyObject_CheckConsistency',
	'_PyObject_CheckCrossInterpreterData',
	'_PyObject_DebugMallocStats',
	'_PyObject_DebugTypeStats',
	'_PyObject_Dump',
	'_PyObject_FastCall',
	'_PyObject_FastCallDictTstate',
	'_PyObject_FunctionStr',
	'_PyObject_GC_New',
	'_PyObject_GC_NewVar',
	'_PyObject_GC_Resize',
	'_PyObject_GenericGetAttrWithDict',
	'_PyObject_GenericSetAttrWithDict',
	'_PyObject_GetAttrId',
	'_PyObject_GetCrossInterpreterData',
	'_PyObject_GetDictPtr',
	'_PyObject_GetMethod',
	'_PyObject_GetState',
	'_PyObject_HasLen',
	'_PyObject_IsAbstract',
	'_PyObject_IsFreed',
	'_PyObject_LookupAttr',
	'_PyObject_LookupAttrId',
	'_PyObject_LookupSpecial',
	'_PyObject_LookupSpecialId',
	'_PyObject_MakeTpCall',
	'_PyObject_New',
	'_PyObject_NewVar',
	'_PyObject_NextNotImplemented',
	'_PyObject_RealIsInstance',
	'_PyObject_RealIsSubclass',
	'_PyObject_SetAttrId',
	'_PyPathConfig_ClearGlobal',
	'_PyPreConfig_InitCompatConfig',
	'_PyRun_AnyFileObject',
	'_PyRun_InteractiveLoopObject',
	'_PyRun_SimpleFileObject',
	'_PyRuntimeState_Fini',
	'_PyRuntimeState_Init',
	'_PyRuntime_Finalize',
	'_PyRuntime_Initialize',
	'_PySequence_BytesToCharpArray',
	'_PySequence_IterSearch',
	'_PySet_NextEntry',
	'_PySet_Update',
	'_PySlice_FromIndices',
	'_PySlice_GetLongIndices',
	'_PyStack_AsDict',
	'_PyState_AddModule',
	'_PyStructSequence_InitType',
	'_PyStructSequence_NewType',
	'_PySys_GetAttr',
	'_PySys_GetSizeOf',
	'_PyThreadState_DeleteCurrent',
	'_PyThreadState_DeleteExcept',
	'_PyThreadState_GetDict',
	'_PyThreadState_Init',
	'_PyThreadState_Prealloc',
	'_PyThreadState_SetCurrent',
	'_PyThreadState_Swap',
	'_PyThreadState_UncheckedGet',
	'_PyThread_CurrentExceptions',
	'_PyThread_CurrentFrames',
	'_PyThread_at_fork_reinit',
	'_PyTime_Add',
	'_PyTime_AsMicroseconds',
	'_PyTime_AsMilliseconds',
	'_PyTime_AsNanoseconds',
	'_PyTime_AsNanosecondsObject',
	'_PyTime_AsSecondsDouble',
	'_PyTime_AsTimespec',
	'_PyTime_AsTimespec_clamp',
	'_PyTime_AsTimeval',
	'_PyTime_AsTimevalTime_t',
	'_PyTime_AsTimeval_clamp',
	'_PyTime_FromMillisecondsObject',
	'_PyTime_FromNanoseconds',
	'_PyTime_FromNanosecondsObject',
	'_PyTime_FromSeconds',
	'_PyTime_FromSecondsObject',
	'_PyTime_FromTimespec',
	'_PyTime_FromTimeval',
	'_PyTime_GetMonotonicClock',
	'_PyTime_GetMonotonicClockWithInfo',
	'_PyTime_GetPerfCounter',
	'_PyTime_GetPerfCounterWithInfo',
	'_PyTime_GetSystemClock',
	'_PyTime_GetSystemClockWithInfo',
	'_PyTime_MulDiv',
	'_PyTime_ObjectToTime_t',
	'_PyTime_ObjectToTimespec',
	'_PyTime_ObjectToTimeval',
	'_PyTime_gmtime',
	'_PyTime_localtime',
	'_PyTraceBack_FromFrame',
	'_PyTraceBack_Print_Indented',
	'_PyTraceMalloc_GetTraceback',
	'_PyTraceback_Add',
	'_PyTrash_begin',
	'_PyTrash_cond',
	'_PyTrash_end',
	'_PyTuple_DebugMallocStats',
	'_PyTuple_MaybeUntrack',
	'_PyTuple_Resize',
	'_PyType_CalculateMetaclass',
	'_PyType_CheckConsistency',
	'_PyType_GetDocFromInternalDoc',
	'_PyType_GetTextSignatureFromInternalDoc',
	'_PyType_Lookup',
	'_PyType_LookupId',
	'_PyType_Name',
	'_PyUnicodeTranslateError_Create',
	'_PyUnicodeWriter_Dealloc',
	'_PyUnicodeWriter_Finish',
	'_PyUnicodeWriter_Init',
	'_PyUnicodeWriter_PrepareInternal',
	'_PyUnicodeWriter_PrepareKindInternal',
	'_PyUnicodeWriter_WriteASCIIString',
	'_PyUnicodeWriter_WriteChar',
	'_PyUnicodeWriter_WriteLatin1String',
	'_PyUnicodeWriter_WriteStr',
	'_PyUnicodeWriter_WriteSubstring',
	'_PyUnicode_AsASCIIString',
	'_PyUnicode_AsLatin1String',
	'_PyUnicode_AsUTF8String',
	'_PyUnicode_AsUnicode',
	'_PyUnicode_CheckConsistency',
	'_PyUnicode_Copy',
	'_PyUnicode_DecodeRawUnicodeEscapeStateful',
	'_PyUnicode_DecodeUnicodeEscapeInternal',
	'_PyUnicode_DecodeUnicodeEscapeStateful',
	'_PyUnicode_EQ',
	'_PyUnicode_EncodeCharmap',
	'_PyUnicode_EncodeUTF16',
	'_PyUnicode_EncodeUTF32',
	'_PyUnicode_EncodeUTF7',
	'_PyUnicode_Equal',
	'_PyUnicode_EqualToASCIIId',
	'_PyUnicode_EqualToASCIIString',
	'_PyUnicode_FastCopyCharacters',
	'_PyUnicode_FastFill',
	'_PyUnicode_FindMaxChar',
	'_PyUnicode_FormatAdvancedWriter',
	'_PyUnicode_FormatLong',
	'_PyUnicode_FromASCII',
	'_PyUnicode_FromId',
	'_PyUnicode_InsertThousandsGrouping',
	'_PyUnicode_IsAlpha',
	'_PyUnicode_IsCaseIgnorable',
	'_PyUnicode_IsCased',
	'_PyUnicode_IsDecimalDigit',
	'_PyUnicode_IsDigit',
	'_PyUnicode_IsLinebreak',
	'_PyUnicode_IsLowercase',
	'_PyUnicode_IsNumeric',
	'_PyUnicode_IsPrintable',
	'_PyUnicode_IsTitlecase',
	'_PyUnicode_IsUppercase',
	'_PyUnicode_IsWhitespace',
	'_PyUnicode_IsXidContinue',
	'_PyUnicode_IsXidStart',
	'_PyUnicode_JoinArray',
	'_PyUnicode_Ready',
	'_PyUnicode_ScanIdentifier',
	'_PyUnicode_ToDecimalDigit',
	'_PyUnicode_ToDigit',
	'_PyUnicode_ToFoldedFull',
	'_PyUnicode_ToLowerFull',
	'_PyUnicode_ToLowercase',
	'_PyUnicode_ToNumeric',
	'_PyUnicode_ToTitleFull',
	'_PyUnicode_ToTitlecase',
	'_PyUnicode_ToUpperFull',
	'_PyUnicode_ToUppercase',
	'_PyUnicode_TransformDecimalAndSpaceToASCII',
	'_PyUnicode_WideCharString_Converter',
	'_PyUnicode_WideCharString_Opt_Converter',
	'_PyUnicode_XStrip',
	'_PyWarnings_Init',
	'_PyWeakref_ClearRef',
	'_PyWeakref_GetWeakrefCount',
	'_PyWideStringList_AsList',
	'_PyWideStringList_Clear',
	'_PyWideStringList_Copy',
	'_PyWideStringList_Extend',
	'_Py_BreakPoint',
	'_Py_BuildValue_SizeT',
	'_Py_CheckFunctionResult',
	'_Py_CheckRecursiveCall',
	'_Py_ClearArgcArgv',
	'_Py_ClearStandardStreamEncoding',
	'_Py_CoerceLegacyLocale',
	'_Py_Dealloc',
	'_Py_DecRef',
	'_Py_DecodeLocaleEx',
	'_Py_DecodeUTF8Ex',
	'_Py_DecodeUTF8_surrogateescape',
	'_Py_DisplaySourceLine',
	'_Py_DumpASCII',
	'_Py_DumpDecimal',
	'_Py_DumpExtensionModules',
	'_Py_DumpHexadecimal',
	'_Py_DumpTraceback',
	'_Py_DumpTracebackThreads',
	'_Py_EncodeLocaleEx',
	'_Py_EncodeLocaleRaw',
	'_Py_EncodeUTF8Ex',
	'_Py_FatalErrorFormat',
	'_Py_FatalErrorFunc',
	'_Py_FatalError_TstateNULL',
	'_Py_FatalRefcountErrorFunc',
	'_Py_FdIsInteractive',
	'_Py_FreeCharPArray',
	'_Py_GetAllocatedBlocks',
	'_Py_GetConfig',
	'_Py_GetConfigsAsDict',
	'_Py_GetEnv',
	'_Py_GetErrorHandler',
	'_Py_GetForceASCII',
	'_Py_GetLocaleEncoding',
	'_Py_GetLocaleEncodingObject',
	'_Py_GetLocaleconvNumeric',
	'_Py_Get_Getpath_CodeObject',
	'_Py_Gid_Converter',
	'_Py_HandleSystemExit',
	'_Py_HashBytes',
	'_Py_HashDouble',
	'_Py_HashPointer',
	'_Py_HashPointerRaw',
	'_Py_IncRef',
	'_Py_InitializeMain',
	'_Py_IsCoreInitialized',
	'_Py_IsFinalizing',
	'_Py_IsLocaleCoercionTarget',
	'_Py_LegacyLocaleDetected',
	'_Py_NewInterpreter',
	'_Py_NewReference',
	'_Py_PreInitializeFromConfig',
	'_Py_PreInitializeFromPyArgv',
	'_Py_ResetForceASCII',
	'_Py_RestoreSignals',
	'_Py_SetLocaleFromEnv',
	'_Py_SetProgramFullPath',
	'_Py_Sigset_Converter',
	'_Py_SourceAsString',
	'_Py_UTF8_Edit_Cost',
	'_Py_Uid_Converter',
	'_Py_UniversalNewlineFgetsWithSize',
	'_Py_VaBuildStack',
	'_Py_VaBuildStack_SizeT',
	'_Py_VaBuildValue_SizeT',
	'_Py_WriteIndent',
	'_Py_WriteIndentedMargin',
	'_Py_add_one_to_index_C',
	'_Py_add_one_to_index_F',
	'_Py_c_abs',
	'_Py_c_diff',
	'_Py_c_neg',
	'_Py_c_pow',
	'_Py_c_prod',
	'_Py_c_quot',
	'_Py_c_sum',
	'_Py_closerange',
	'_Py_convert_optional_to_ssize_t',
	'_Py_device_encoding',
	'_Py_dg_dtoa',
	'_Py_dg_freedtoa',
	'_Py_dg_infinity',
	'_Py_dg_stdnan',
	'_Py_dg_strtod',
	'_Py_dup',
	'_Py_fopen_obj',
	'_Py_fstat',
	'_Py_fstat_noraise',
	'_Py_get_blocking',
	'_Py_get_env_flag',
	'_Py_get_inheritable',
	'_Py_get_xoption',
	'_Py_gitidentifier',
	'_Py_gitversion',
	'_Py_hashtable_clear',
	'_Py_hashtable_compare_direct',
	'_Py_hashtable_destroy',
	'_Py_hashtable_foreach',
	'_Py_hashtable_get',
	'_Py_hashtable_hash_ptr',
	'_Py_hashtable_new',
	'_Py_hashtable_new_full',
	'_Py_hashtable_set',
	'_Py_hashtable_size',
	'_Py_hashtable_steal',
	'_Py_normpath',
	'_Py_open',
	'_Py_open_noraise',
	'_Py_parse_inf_or_nan',
	'_Py_read',
	'_Py_set_blocking',
	'_Py_set_inheritable',
	'_Py_set_inheritable_async_safe',
	'_Py_stat',
	'_Py_str_to_int',
	'_Py_strhex',
	'_Py_strhex_bytes',
	'_Py_strhex_bytes_with_sep',
	'_Py_strhex_with_sep',
	'_Py_string_to_number_with_underscores',
	'_Py_wfopen',
	'_Py_wgetcwd',
	'_Py_wreadlink',
	'_Py_wrealpath',
	'_Py_write',
	'_Py_write_noraise',
)))