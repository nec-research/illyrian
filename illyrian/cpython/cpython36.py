CPYTHON36 = ('cp36-cp36m', set((
	'PyAST_Check',
	'PyAST_Compile',
	'PyAST_CompileEx',
	'PyAST_CompileObject',
	'PyAST_FromNode',
	'PyAST_FromNodeObject',
	'PyAST_Validate',
	'PyAST_mod2obj',
	'PyAST_obj2mod',
	'PyArena_AddPyObject',
	'PyArena_Free',
	'PyArena_Malloc',
	'PyArena_New',
	'PyArg_Parse',
	'PyArg_ParseTuple',
	'PyArg_ParseTupleAndKeywords',
	'PyArg_UnpackTuple',
	'PyArg_VaParse',
	'PyArg_VaParseTupleAndKeywords',
	'PyArg_ValidateKeywordArguments',
	'PyAsyncGen_ClearFreeLists',
	'PyAsyncGen_Fini',
	'PyAsyncGen_New',
	'PyBool_FromLong',
	'PyBuffer_FillContiguousStrides',
	'PyBuffer_FillInfo',
	'PyBuffer_FromContiguous',
	'PyBuffer_GetPointer',
	'PyBuffer_IsContiguous',
	'PyBuffer_Release',
	'PyBuffer_ToContiguous',
	'PyByteArray_AsString',
	'PyByteArray_Concat',
	'PyByteArray_Fini',
	'PyByteArray_FromObject',
	'PyByteArray_FromStringAndSize',
	'PyByteArray_Init',
	'PyByteArray_Resize',
	'PyByteArray_Size',
	'PyBytes_AsString',
	'PyBytes_AsStringAndSize',
	'PyBytes_Concat',
	'PyBytes_ConcatAndDel',
	'PyBytes_DecodeEscape',
	'PyBytes_Fini',
	'PyBytes_FromFormat',
	'PyBytes_FromFormatV',
	'PyBytes_FromObject',
	'PyBytes_FromString',
	'PyBytes_FromStringAndSize',
	'PyBytes_Repr',
	'PyBytes_Size',
	'PyCFunction_Call',
	'PyCFunction_ClearFreeList',
	'PyCFunction_Fini',
	'PyCFunction_GetFlags',
	'PyCFunction_GetFunction',
	'PyCFunction_GetSelf',
	'PyCFunction_New',
	'PyCFunction_NewEx',
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
	'PyCode_New',
	'PyCode_NewEmpty',
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
	'PyCodec_XMLCharRefReplaceErrors',
	'PyCompileString',
	'PyCompile_OpcodeStackEffect',
	'PyComplex_AsCComplex',
	'PyComplex_FromCComplex',
	'PyComplex_FromDoubles',
	'PyComplex_ImagAsDouble',
	'PyComplex_RealAsDouble',
	'PyCoro_New',
	'PyDescr_NewClassMethod',
	'PyDescr_NewGetSet',
	'PyDescr_NewMember',
	'PyDescr_NewMethod',
	'PyDescr_NewWrapper',
	'PyDictProxy_New',
	'PyDict_Clear',
	'PyDict_ClearFreeList',
	'PyDict_Contains',
	'PyDict_Copy',
	'PyDict_DelItem',
	'PyDict_DelItemString',
	'PyDict_Fini',
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
	'PyErr_ResourceWarning',
	'PyErr_Restore',
	'PyErr_SetExcInfo',
	'PyErr_SetFromErrno',
	'PyErr_SetFromErrnoWithFilename',
	'PyErr_SetFromErrnoWithFilenameObject',
	'PyErr_SetFromErrnoWithFilenameObjects',
	'PyErr_SetImportError',
	'PyErr_SetImportErrorSubclass',
	'PyErr_SetInterrupt',
	'PyErr_SetNone',
	'PyErr_SetObject',
	'PyErr_SetString',
	'PyErr_SyntaxLocation',
	'PyErr_SyntaxLocationEx',
	'PyErr_SyntaxLocationObject',
	'PyErr_Warn',
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
	'PyEval_GetCallStats',
	'PyEval_GetFrame',
	'PyEval_GetFuncDesc',
	'PyEval_GetFuncName',
	'PyEval_GetGlobals',
	'PyEval_GetLocals',
	'PyEval_InitThreads',
	'PyEval_MergeCompilerFlags',
	'PyEval_ReInitThreads',
	'PyEval_ReleaseLock',
	'PyEval_ReleaseThread',
	'PyEval_RestoreThread',
	'PyEval_SaveThread',
	'PyEval_SetProfile',
	'PyEval_SetTrace',
	'PyEval_ThreadsInitialized',
	'PyException_GetCause',
	'PyException_GetContext',
	'PyException_GetTraceback',
	'PyException_SetCause',
	'PyException_SetContext',
	'PyException_SetTraceback',
	'PyFile_FromFd',
	'PyFile_GetLine',
	'PyFile_NewStdPrinter',
	'PyFile_WriteObject',
	'PyFile_WriteString',
	'PyFloat_AsDouble',
	'PyFloat_ClearFreeList',
	'PyFloat_Fini',
	'PyFloat_FromDouble',
	'PyFloat_FromString',
	'PyFloat_GetInfo',
	'PyFloat_GetMax',
	'PyFloat_GetMin',
	'PyFrame_BlockPop',
	'PyFrame_BlockSetup',
	'PyFrame_ClearFreeList',
	'PyFrame_FastToLocals',
	'PyFrame_FastToLocalsWithError',
	'PyFrame_Fini',
	'PyFrame_GetLineNumber',
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
	'PyFuture_FromAST',
	'PyFuture_FromASTObject',
	'PyGC_Collect',
	'PyGILState_Check',
	'PyGILState_Ensure',
	'PyGILState_GetThisThreadState',
	'PyGILState_Release',
	'PyGen_NeedsFinalizing',
	'PyGen_New',
	'PyGen_NewWithQualName',
	'PyGrammar_AddAccelerators',
	'PyGrammar_FindDFA',
	'PyGrammar_LabelRepr',
	'PyGrammar_RemoveAccelerators',
	'PyHash_GetFuncDef',
	'PyImport_AddModule',
	'PyImport_AddModuleObject',
	'PyImport_AppendInittab',
	'PyImport_Cleanup',
	'PyImport_ExecCodeModule',
	'PyImport_ExecCodeModuleEx',
	'PyImport_ExecCodeModuleObject',
	'PyImport_ExecCodeModuleWithPathnames',
	'PyImport_ExtendInittab',
	'PyImport_GetImporter',
	'PyImport_GetMagicNumber',
	'PyImport_GetMagicTag',
	'PyImport_GetModuleDict',
	'PyImport_Import',
	'PyImport_ImportFrozenModule',
	'PyImport_ImportFrozenModuleObject',
	'PyImport_ImportModule',
	'PyImport_ImportModuleLevel',
	'PyImport_ImportModuleLevelObject',
	'PyImport_ImportModuleNoBlock',
	'PyImport_ReloadModule',
	'PyInit__ast',
	'PyInit__codecs',
	'PyInit__collections',
	'PyInit__functools',
	'PyInit__io',
	'PyInit__locale',
	'PyInit__operator',
	'PyInit__signal',
	'PyInit__sre',
	'PyInit__stat',
	'PyInit__string',
	'PyInit__symtable',
	'PyInit__thread',
	'PyInit__tracemalloc',
	'PyInit__weakref',
	'PyInit_atexit',
	'PyInit_errno',
	'PyInit_faulthandler',
	'PyInit_gc',
	'PyInit_imp',
	'PyInit_itertools',
	'PyInit_posix',
	'PyInit_pwd',
	'PyInit_time',
	'PyInit_xxsubtype',
	'PyInit_zipimport',
	'PyInstanceMethod_Function',
	'PyInstanceMethod_New',
	'PyInterpreterState_Clear',
	'PyInterpreterState_Delete',
	'PyInterpreterState_Head',
	'PyInterpreterState_New',
	'PyInterpreterState_Next',
	'PyInterpreterState_ThreadHead',
	'PyIter_Next',
	'PyList_Append',
	'PyList_AsTuple',
	'PyList_ClearFreeList',
	'PyList_Fini',
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
	'PyLong_Fini',
	'PyLong_FromDouble',
	'PyLong_FromLong',
	'PyLong_FromLongLong',
	'PyLong_FromSize_t',
	'PyLong_FromSsize_t',
	'PyLong_FromString',
	'PyLong_FromUnicode',
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
	'PyMethod_ClearFreeList',
	'PyMethod_Fini',
	'PyMethod_Function',
	'PyMethod_New',
	'PyMethod_Self',
	'PyModuleDef_Init',
	'PyModule_AddFunctions',
	'PyModule_AddIntConstant',
	'PyModule_AddObject',
	'PyModule_AddStringConstant',
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
	'PyModule_GetWarningsModule',
	'PyModule_New',
	'PyModule_NewObject',
	'PyModule_SetDocString',
	'PyNode_AddChild',
	'PyNode_Compile',
	'PyNode_Free',
	'PyNode_New',
	'PyNumber_Absolute',
	'PyNumber_Add',
	'PyNumber_And',
	'PyNumber_AsOff_t',
	'PyNumber_AsSsize_t',
	'PyNumber_Check',
	'PyNumber_Divmod',
	'PyNumber_Float',
	'PyNumber_FloorDivide',
	'PyNumber_InMatrixMultiply',
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
	'PyOS_FSPath',
	'PyOS_FiniInterrupts',
	'PyOS_InitInterrupts',
	'PyOS_InterruptOccurred',
	'PyOS_Readline',
	'PyOS_StdioReadline',
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
	'PyObject_CallObject',
	'PyObject_Calloc',
	'PyObject_CheckReadBuffer',
	'PyObject_ClearWeakRefs',
	'PyObject_CopyData',
	'PyObject_DelItem',
	'PyObject_DelItemString',
	'PyObject_Dir',
	'PyObject_Format',
	'PyObject_Free',
	'PyObject_GC_Del',
	'PyObject_GC_Track',
	'PyObject_GC_UnTrack',
	'PyObject_GenericGetAttr',
	'PyObject_GenericGetDict',
	'PyObject_GenericSetAttr',
	'PyObject_GenericSetDict',
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
	'PyParser_ASTFromFile',
	'PyParser_ASTFromFileObject',
	'PyParser_ASTFromString',
	'PyParser_ASTFromStringObject',
	'PyParser_AddToken',
	'PyParser_ClearError',
	'PyParser_Delete',
	'PyParser_New',
	'PyParser_ParseFile',
	'PyParser_ParseFileFlags',
	'PyParser_ParseFileFlagsEx',
	'PyParser_ParseFileObject',
	'PyParser_ParseString',
	'PyParser_ParseStringFlags',
	'PyParser_ParseStringFlagsFilename',
	'PyParser_ParseStringFlagsFilenameEx',
	'PyParser_ParseStringObject',
	'PyParser_SetError',
	'PyParser_SimpleParseFile',
	'PyParser_SimpleParseFileFlags',
	'PyParser_SimpleParseString',
	'PyParser_SimpleParseStringFilename',
	'PyParser_SimpleParseStringFlags',
	'PyParser_SimpleParseStringFlagsFilename',
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
	'PyST_GetScope',
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
	'PySet_ClearFreeList',
	'PySet_Contains',
	'PySet_Discard',
	'PySet_Fini',
	'PySet_New',
	'PySet_Pop',
	'PySet_Size',
	'PySignal_SetWakeupFd',
	'PySlice_AdjustIndices',
	'PySlice_Fini',
	'PySlice_GetIndices',
	'PySlice_GetIndicesEx',
	'PySlice_New',
	'PySlice_Unpack',
	'PyState_AddModule',
	'PyState_FindModule',
	'PyState_RemoveModule',
	'PyStaticMethod_New',
	'PyStructSequence_GetItem',
	'PyStructSequence_InitType',
	'PyStructSequence_InitType2',
	'PyStructSequence_New',
	'PyStructSequence_NewType',
	'PyStructSequence_SetItem',
	'PySymtable_Build',
	'PySymtable_BuildObject',
	'PySymtable_Free',
	'PySymtable_Lookup',
	'PySys_AddWarnOption',
	'PySys_AddWarnOptionUnicode',
	'PySys_AddXOption',
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
	'PyThreadState_Get',
	'PyThreadState_GetDict',
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
	'PyThread_init_thread',
	'PyThread_release_lock',
	'PyThread_set_key_value',
	'PyThread_set_stacksize',
	'PyThread_start_new_thread',
	'PyToken_OneChar',
	'PyToken_ThreeChars',
	'PyToken_TwoChars',
	'PyTokenizer_FindEncoding',
	'PyTokenizer_FindEncodingFilename',
	'PyTokenizer_Free',
	'PyTokenizer_FromFile',
	'PyTokenizer_FromString',
	'PyTokenizer_FromUTF8',
	'PyTokenizer_Get',
	'PyTraceBack_Here',
	'PyTraceBack_Print',
	'PyTuple_ClearFreeList',
	'PyTuple_Fini',
	'PyTuple_GetItem',
	'PyTuple_GetSlice',
	'PyTuple_New',
	'PyTuple_Pack',
	'PyTuple_SetItem',
	'PyTuple_Size',
	'PyType_ClearCache',
	'PyType_FromSpec',
	'PyType_FromSpecWithBases',
	'PyType_GenericAlloc',
	'PyType_GenericNew',
	'PyType_GetFlags',
	'PyType_GetSlot',
	'PyType_IsSubtype',
	'PyType_Modified',
	'PyType_Ready',
	'PyUnicodeDecodeError_Create',
	'PyUnicodeDecodeError_GetEncoding',
	'PyUnicodeDecodeError_GetEnd',
	'PyUnicodeDecodeError_GetObject',
	'PyUnicodeDecodeError_GetReason',
	'PyUnicodeDecodeError_GetStart',
	'PyUnicodeDecodeError_SetEnd',
	'PyUnicodeDecodeError_SetReason',
	'PyUnicodeDecodeError_SetStart',
	'PyUnicodeEncodeError_Create',
	'PyUnicodeEncodeError_GetEncoding',
	'PyUnicodeEncodeError_GetEnd',
	'PyUnicodeEncodeError_GetObject',
	'PyUnicodeEncodeError_GetReason',
	'PyUnicodeEncodeError_GetStart',
	'PyUnicodeEncodeError_SetEnd',
	'PyUnicodeEncodeError_SetReason',
	'PyUnicodeEncodeError_SetStart',
	'PyUnicodeTranslateError_Create',
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
	'PyUnicode_AsUnicodeCopy',
	'PyUnicode_AsUnicodeEscapeString',
	'PyUnicode_AsWideChar',
	'PyUnicode_AsWideCharString',
	'PyUnicode_BuildEncodingMap',
	'PyUnicode_ClearFreeList',
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
	'PyUnicode_Encode',
	'PyUnicode_EncodeASCII',
	'PyUnicode_EncodeCharmap',
	'PyUnicode_EncodeDecimal',
	'PyUnicode_EncodeFSDefault',
	'PyUnicode_EncodeLatin1',
	'PyUnicode_EncodeLocale',
	'PyUnicode_EncodeRawUnicodeEscape',
	'PyUnicode_EncodeUTF16',
	'PyUnicode_EncodeUTF32',
	'PyUnicode_EncodeUTF7',
	'PyUnicode_EncodeUTF8',
	'PyUnicode_EncodeUnicodeEscape',
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
	'PyUnicode_GetMax',
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
	'PyUnicode_TransformDecimalToASCII',
	'PyUnicode_Translate',
	'PyUnicode_TranslateCharmap',
	'PyUnicode_WriteChar',
	'PyWeakref_GetObject',
	'PyWeakref_NewProxy',
	'PyWeakref_NewRef',
	'PyWrapper_New',
	'Py_AddPendingCall',
	'Py_AtExit',
	'Py_BuildValue',
	'Py_CompileString',
	'Py_CompileStringExFlags',
	'Py_CompileStringFlags',
	'Py_CompileStringObject',
	'Py_DecRef',
	'Py_DecodeLocale',
	'Py_EncodeLocale',
	'Py_EndInterpreter',
	'Py_Exit',
	'Py_FatalError',
	'Py_FdIsInteractive',
	'Py_Finalize',
	'Py_FinalizeEx',
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
	'Py_IsInitialized',
	'Py_Main',
	'Py_MakePendingCalls',
	'Py_NewInterpreter',
	'Py_ReprEnter',
	'Py_ReprLeave',
	'Py_SetPath',
	'Py_SetProgramName',
	'Py_SetPythonHome',
	'Py_SetRecursionLimit',
	'Py_SetStandardStreamEncoding',
	'Py_SymtableString',
	'Py_SymtableStringObject',
	'Py_UNICODE_strcat',
	'Py_UNICODE_strchr',
	'Py_UNICODE_strcmp',
	'Py_UNICODE_strcpy',
	'Py_UNICODE_strlen',
	'Py_UNICODE_strncmp',
	'Py_UNICODE_strncpy',
	'Py_UNICODE_strrchr',
	'Py_UniversalNewlineFgets',
	'Py_VaBuildValue',
	'_PyAIterWrapper_New',
	'_PyAccu_Accumulate',
	'_PyAccu_Destroy',
	'_PyAccu_Finish',
	'_PyAccu_FinishAsList',
	'_PyAccu_Init',
	'_PyArg_Fini',
	'_PyArg_NoKeywords',
	'_PyArg_NoPositional',
	'_PyArg_ParseStack',
	'_PyArg_ParseStack_SizeT',
	'_PyArg_ParseTupleAndKeywordsFast',
	'_PyArg_ParseTupleAndKeywordsFast_SizeT',
	'_PyArg_ParseTupleAndKeywords_SizeT',
	'_PyArg_ParseTuple_SizeT',
	'_PyArg_Parse_SizeT',
	'_PyArg_VaParseTupleAndKeywordsFast',
	'_PyArg_VaParseTupleAndKeywordsFast_SizeT',
	'_PyArg_VaParseTupleAndKeywords_SizeT',
	'_PyArg_VaParse_SizeT',
	'_PyAsyncGenValueWrapperNew',
	'_PyBuiltin_Init',
	'_PyBytesWriter_Alloc',
	'_PyBytesWriter_Dealloc',
	'_PyBytesWriter_Finish',
	'_PyBytesWriter_Init',
	'_PyBytesWriter_Prepare',
	'_PyBytesWriter_Resize',
	'_PyBytesWriter_WriteBytes',
	'_PyBytes_DecodeEscape',
	'_PyBytes_FormatEx',
	'_PyBytes_FromHex',
	'_PyBytes_Join',
	'_PyBytes_Resize',
	'_PyCFunction_DebugMallocStats',
	'_PyCFunction_FastCallDict',
	'_PyCFunction_FastCallKeywords',
	'_PyCode_CheckLineNumber',
	'_PyCode_ConstantKey',
	'_PyCode_GetExtra',
	'_PyCode_SetExtra',
	'_PyCodecInfo_GetIncrementalDecoder',
	'_PyCodecInfo_GetIncrementalEncoder',
	'_PyCodec_DecodeText',
	'_PyCodec_EncodeText',
	'_PyCodec_Forget',
	'_PyCodec_Lookup',
	'_PyCodec_LookupTextEncoding',
	'_PyComplex_FormatAdvancedWriter',
	'_PyCoro_GetAwaitableIter',
	'_PyDebugAllocatorStats',
	'_PyDictKeys_DecRef',
	'_PyDictView_Intersect',
	'_PyDictView_New',
	'_PyDict_Contains',
	'_PyDict_DebugMallocStats',
	'_PyDict_DelItemId',
	'_PyDict_DelItemIf',
	'_PyDict_DelItem_KnownHash',
	'_PyDict_FromKeys',
	'_PyDict_GetItemId',
	'_PyDict_GetItemIdWithError',
	'_PyDict_GetItem_KnownHash',
	'_PyDict_HasOnlyStringKeys',
	'_PyDict_KeysSize',
	'_PyDict_LoadGlobal',
	'_PyDict_MaybeUntrack',
	'_PyDict_MergeEx',
	'_PyDict_NewKeysForClass',
	'_PyDict_NewPresized',
	'_PyDict_Next',
	'_PyDict_Pop',
	'_PyDict_Pop_KnownHash',
	'_PyDict_SetItemId',
	'_PyDict_SetItem_KnownHash',
	'_PyDict_SizeOf',
	'_PyErr_BadInternalCall',
	'_PyErr_ChainExceptions',
	'_PyErr_FormatFromCause',
	'_PyErr_SetKeyError',
	'_PyErr_TrySetFromCause',
	'_PyEval_CallTracing',
	'_PyEval_EvalFrameDefault',
	'_PyEval_FiniThreads',
	'_PyEval_GetAsyncGenFinalizer',
	'_PyEval_GetAsyncGenFirstiter',
	'_PyEval_GetBuiltinId',
	'_PyEval_GetCoroutineWrapper',
	'_PyEval_GetSwitchInterval',
	'_PyEval_RequestCodeExtraIndex',
	'_PyEval_SetAsyncGenFinalizer',
	'_PyEval_SetAsyncGenFirstiter',
	'_PyEval_SetCoroutineWrapper',
	'_PyEval_SetSwitchInterval',
	'_PyEval_SignalAsyncExc',
	'_PyEval_SignalReceived',
	'_PyEval_SliceIndex',
	'_PyEval_SliceIndexNotNone',
	'_PyExc_Fini',
	'_PyExc_Init',
	'_PyFaulthandler_Fini',
	'_PyFaulthandler_Init',
	'_PyFileIO_closed',
	'_PyFloat_DebugMallocStats',
	'_PyFloat_FormatAdvancedWriter',
	'_PyFloat_Init',
	'_PyFloat_Pack2',
	'_PyFloat_Pack4',
	'_PyFloat_Pack8',
	'_PyFloat_Unpack2',
	'_PyFloat_Unpack4',
	'_PyFloat_Unpack8',
	'_PyFrame_DebugMallocStats',
	'_PyFrame_Init',
	'_PyFunction_FastCallDict',
	'_PyFunction_FastCallKeywords',
	'_PyGC_CollectIfEnabled',
	'_PyGC_CollectNoFail',
	'_PyGC_Dump',
	'_PyGC_DumpShutdownStats',
	'_PyGC_Fini',
	'_PyGILState_Fini',
	'_PyGILState_GetInterpreterStateUnsafe',
	'_PyGILState_Init',
	'_PyGILState_Reinit',
	'_PyGen_FetchStopIterationValue',
	'_PyGen_Finalize',
	'_PyGen_Send',
	'_PyGen_SetStopIterationValue',
	'_PyGen_yf',
	'_PyHash_Fini',
	'_PyIOBase_check_closed',
	'_PyIOBase_check_readable',
	'_PyIOBase_check_seekable',
	'_PyIOBase_check_writable',
	'_PyIOBase_finalize',
	'_PyIO_ConvertSsize_t',
	'_PyIO_find_line_ending',
	'_PyIO_get_locale_module',
	'_PyIO_get_module_state',
	'_PyIO_trap_eintr',
	'_PyImportHooks_Init',
	'_PyImportZip_Init',
	'_PyImport_AcquireLock',
	'_PyImport_FindBuiltin',
	'_PyImport_FindExtensionObject',
	'_PyImport_FindSharedFuncptr',
	'_PyImport_Fini',
	'_PyImport_FixupBuiltin',
	'_PyImport_FixupExtensionObject',
	'_PyImport_Init',
	'_PyImport_LoadDynamicModuleWithSpec',
	'_PyImport_ReInitLock',
	'_PyImport_ReleaseLock',
	'_PyIncrementalNewlineDecoder_decode',
	'_PyList_DebugMallocStats',
	'_PyList_Extend',
	'_PyLong_AsByteArray',
	'_PyLong_AsInt',
	'_PyLong_AsTime_t',
	'_PyLong_Copy',
	'_PyLong_DivmodNear',
	'_PyLong_Format',
	'_PyLong_FormatAdvancedWriter',
	'_PyLong_FormatBytesWriter',
	'_PyLong_FormatWriter',
	'_PyLong_Frexp',
	'_PyLong_FromByteArray',
	'_PyLong_FromBytes',
	'_PyLong_FromGid',
	'_PyLong_FromNbInt',
	'_PyLong_FromTime_t',
	'_PyLong_FromUid',
	'_PyLong_GCD',
	'_PyLong_Init',
	'_PyLong_New',
	'_PyLong_NumBits',
	'_PyLong_Sign',
	'_PyMem_DumpTraceback',
	'_PyMem_IsFreed',
	'_PyMem_PymallocEnabled',
	'_PyMem_RawStrdup',
	'_PyMem_SetupAllocators',
	'_PyMem_Strdup',
	'_PyMethod_DebugMallocStats',
	'_PyModule_Clear',
	'_PyModule_ClearDict',
	'_PyNamespace_New',
	'_PyNode_SizeOf',
	'_PyOS_GetOpt',
	'_PyOS_IsMainThread',
	'_PyOS_ResetGetOpt',
	'_PyOS_URandom',
	'_PyOS_URandomNonblock',
	'_PyObjectDict_SetItem',
	'_PyObject_CallFunction_SizeT',
	'_PyObject_CallMethodId',
	'_PyObject_CallMethodIdObjArgs',
	'_PyObject_CallMethodId_SizeT',
	'_PyObject_CallMethod_SizeT',
	'_PyObject_Call_Prepend',
	'_PyObject_DebugMallocStats',
	'_PyObject_DebugTypeStats',
	'_PyObject_Dump',
	'_PyObject_FastCallDict',
	'_PyObject_FastCallKeywords',
	'_PyObject_GC_Calloc',
	'_PyObject_GC_Malloc',
	'_PyObject_GC_New',
	'_PyObject_GC_NewVar',
	'_PyObject_GC_Resize',
	'_PyObject_GenericGetAttrWithDict',
	'_PyObject_GenericSetAttrWithDict',
	'_PyObject_GetAttrId',
	'_PyObject_GetBuiltin',
	'_PyObject_GetDictPtr',
	'_PyObject_HasAttrId',
	'_PyObject_HasLen',
	'_PyObject_IsAbstract',
	'_PyObject_IsFreed',
	'_PyObject_LookupSpecial',
	'_PyObject_New',
	'_PyObject_NewVar',
	'_PyObject_NextNotImplemented',
	'_PyObject_RealIsInstance',
	'_PyObject_RealIsSubclass',
	'_PyObject_SetAttrId',
	'_PyRandom_Fini',
	'_PyRandom_Init',
	'_PySequence_BytesToCharpArray',
	'_PySequence_IterSearch',
	'_PySet_NextEntry',
	'_PySet_Update',
	'_PySlice_FromIndices',
	'_PySlice_GetLongIndices',
	'_PyStack_AsDict',
	'_PyStack_AsTuple',
	'_PyStack_UnpackDict',
	'_PyState_AddModule',
	'_PyState_ClearModules',
	'_PyStructSequence_Init',
	'_PySys_GetObjectId',
	'_PySys_GetSizeOf',
	'_PySys_Init',
	'_PySys_SetObjectId',
	'_PyThreadState_DeleteExcept',
	'_PyThreadState_Init',
	'_PyThreadState_Prealloc',
	'_PyThreadState_UncheckedGet',
	'_PyThread_CurrentFrames',
	'_PyTime_AsMicroseconds',
	'_PyTime_AsMilliseconds',
	'_PyTime_AsNanosecondsObject',
	'_PyTime_AsSecondsDouble',
	'_PyTime_AsTimespec',
	'_PyTime_AsTimeval',
	'_PyTime_AsTimevalTime_t',
	'_PyTime_AsTimeval_noraise',
	'_PyTime_FromMillisecondsObject',
	'_PyTime_FromNanoseconds',
	'_PyTime_FromSeconds',
	'_PyTime_FromSecondsObject',
	'_PyTime_GetMonotonicClock',
	'_PyTime_GetMonotonicClockWithInfo',
	'_PyTime_GetSystemClock',
	'_PyTime_GetSystemClockWithInfo',
	'_PyTime_Init',
	'_PyTime_ObjectToTime_t',
	'_PyTime_ObjectToTimespec',
	'_PyTime_ObjectToTimeval',
	'_PyTime_gmtime',
	'_PyTime_localtime',
	'_PyTraceMalloc_Fini',
	'_PyTraceMalloc_GetTraceback',
	'_PyTraceMalloc_Init',
	'_PyTraceMalloc_Track',
	'_PyTraceMalloc_Untrack',
	'_PyTraceback_Add',
	'_PyTrash_deposit_object',
	'_PyTrash_destroy_chain',
	'_PyTrash_thread_deposit_object',
	'_PyTrash_thread_destroy_chain',
	'_PyTuple_DebugMallocStats',
	'_PyTuple_MaybeUntrack',
	'_PyTuple_Resize',
	'_PyType_CalculateMetaclass',
	'_PyType_Fini',
	'_PyType_GetDocFromInternalDoc',
	'_PyType_GetTextSignatureFromInternalDoc',
	'_PyType_Lookup',
	'_PyType_LookupId',
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
	'_PyUnicode_AsKind',
	'_PyUnicode_AsLatin1String',
	'_PyUnicode_AsUTF8String',
	'_PyUnicode_AsUnicode',
	'_PyUnicode_AsWideCharString',
	'_PyUnicode_ClearStaticStrings',
	'_PyUnicode_Copy',
	'_PyUnicode_DecodeUnicodeEscape',
	'_PyUnicode_DecodeUnicodeInternal',
	'_PyUnicode_EQ',
	'_PyUnicode_EncodeCharmap',
	'_PyUnicode_EncodeUTF16',
	'_PyUnicode_EncodeUTF32',
	'_PyUnicode_EncodeUTF7',
	'_PyUnicode_EqualToASCIIId',
	'_PyUnicode_EqualToASCIIString',
	'_PyUnicode_FastCopyCharacters',
	'_PyUnicode_FastFill',
	'_PyUnicode_FindMaxChar',
	'_PyUnicode_Fini',
	'_PyUnicode_FormatAdvancedWriter',
	'_PyUnicode_FormatLong',
	'_PyUnicode_FromASCII',
	'_PyUnicode_FromId',
	'_PyUnicode_Init',
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
	'_PyUnicode_XStrip',
	'_PyWarnings_Init',
	'_PyWeakref_ClearRef',
	'_PyWeakref_GetWeakrefCount',
	'_Py_AnnAssign',
	'_Py_Assert',
	'_Py_Assign',
	'_Py_AsyncFor',
	'_Py_AsyncFunctionDef',
	'_Py_AsyncWith',
	'_Py_Attribute',
	'_Py_AugAssign',
	'_Py_Await',
	'_Py_BinOp',
	'_Py_BoolOp',
	'_Py_Break',
	'_Py_BreakPoint',
	'_Py_BuildValue_SizeT',
	'_Py_Bytes',
	'_Py_Call',
	'_Py_CheckFunctionResult',
	'_Py_CheckRecursiveCall',
	'_Py_ClassDef',
	'_Py_Compare',
	'_Py_Constant',
	'_Py_Continue',
	'_Py_Dealloc',
	'_Py_DecodeLocaleEx',
	'_Py_Delete',
	'_Py_Dict',
	'_Py_DictComp',
	'_Py_DisplaySourceLine',
	'_Py_DumpASCII',
	'_Py_DumpDecimal',
	'_Py_DumpHexadecimal',
	'_Py_DumpTraceback',
	'_Py_DumpTracebackThreads',
	'_Py_Ellipsis',
	'_Py_EncodeLocaleEx',
	'_Py_ExceptHandler',
	'_Py_Expr',
	'_Py_Expression',
	'_Py_ExtSlice',
	'_Py_For',
	'_Py_FormattedValue',
	'_Py_FreeCharPArray',
	'_Py_FunctionDef',
	'_Py_GeneratorExp',
	'_Py_GetAllocatedBlocks',
	'_Py_GetLocaleconvNumeric',
	'_Py_Gid_Converter',
	'_Py_Global',
	'_Py_HashBytes',
	'_Py_HashDouble',
	'_Py_HashPointer',
	'_Py_If',
	'_Py_IfExp',
	'_Py_Import',
	'_Py_ImportFrom',
	'_Py_Index',
	'_Py_InitializeEx_Private',
	'_Py_Interactive',
	'_Py_JoinedStr',
	'_Py_Lambda',
	'_Py_List',
	'_Py_ListComp',
	'_Py_Mangle',
	'_Py_Module',
	'_Py_Name',
	'_Py_NameConstant',
	'_Py_Nonlocal',
	'_Py_Num',
	'_Py_Pass',
	'_Py_PyAtExit',
	'_Py_Raise',
	'_Py_ReadyTypes',
	'_Py_ReleaseInternedUnicodeStrings',
	'_Py_RestoreSignals',
	'_Py_Return',
	'_Py_Set',
	'_Py_SetComp',
	'_Py_Slice',
	'_Py_Starred',
	'_Py_Str',
	'_Py_Subscript',
	'_Py_Suite',
	'_Py_Try',
	'_Py_Tuple',
	'_Py_Uid_Converter',
	'_Py_UnaryOp',
	'_Py_VaBuildValue_SizeT',
	'_Py_While',
	'_Py_With',
	'_Py_Yield',
	'_Py_YieldFrom',
	'_Py_add_one_to_index_C',
	'_Py_add_one_to_index_F',
	'_Py_alias',
	'_Py_arg',
	'_Py_arguments',
	'_Py_asdl_int_seq_new',
	'_Py_asdl_seq_new',
	'_Py_bytes_capitalize',
	'_Py_bytes_contains',
	'_Py_bytes_count',
	'_Py_bytes_endswith',
	'_Py_bytes_find',
	'_Py_bytes_index',
	'_Py_bytes_isalnum',
	'_Py_bytes_isalpha',
	'_Py_bytes_isdigit',
	'_Py_bytes_islower',
	'_Py_bytes_isspace',
	'_Py_bytes_istitle',
	'_Py_bytes_isupper',
	'_Py_bytes_lower',
	'_Py_bytes_maketrans',
	'_Py_bytes_rfind',
	'_Py_bytes_rindex',
	'_Py_bytes_startswith',
	'_Py_bytes_swapcase',
	'_Py_bytes_title',
	'_Py_bytes_upper',
	'_Py_c_abs',
	'_Py_c_diff',
	'_Py_c_neg',
	'_Py_c_pow',
	'_Py_c_prod',
	'_Py_c_quot',
	'_Py_c_sum',
	'_Py_comprehension',
	'_Py_device_encoding',
	'_Py_dg_dtoa',
	'_Py_dg_freedtoa',
	'_Py_dg_infinity',
	'_Py_dg_stdnan',
	'_Py_dg_strtod',
	'_Py_dup',
	'_Py_fopen',
	'_Py_fopen_obj',
	'_Py_fstat',
	'_Py_fstat_noraise',
	'_Py_get_387controlword',
	'_Py_get_blocking',
	'_Py_get_inheritable',
	'_Py_gitidentifier',
	'_Py_gitversion',
	'_Py_hashtable_clear',
	'_Py_hashtable_compare_direct',
	'_Py_hashtable_copy',
	'_Py_hashtable_destroy',
	'_Py_hashtable_foreach',
	'_Py_hashtable_get',
	'_Py_hashtable_get_entry',
	'_Py_hashtable_hash_ptr',
	'_Py_hashtable_new',
	'_Py_hashtable_new_full',
	'_Py_hashtable_pop',
	'_Py_hashtable_set',
	'_Py_hashtable_size',
	'_Py_keyword',
	'_Py_normalize_encoding',
	'_Py_open',
	'_Py_open_noraise',
	'_Py_parse_inf_or_nan',
	'_Py_read',
	'_Py_set_387controlword',
	'_Py_set_blocking',
	'_Py_set_inheritable',
	'_Py_set_inheritable_async_safe',
	'_Py_stat',
	'_Py_strhex',
	'_Py_strhex_bytes',
	'_Py_string_to_number_with_underscores',
	'_Py_wfopen',
	'_Py_wgetcwd',
	'_Py_withitem',
	'_Py_wreadlink',
	'_Py_wrealpath',
	'_Py_write',
	'_Py_write_noraise',
	'__PyCodeExtraState_Get',
)))