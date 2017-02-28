# mjpython
[![Build Status](https://travis-ci.org/mjpatter88/mjpython.svg?branch=master)](https://travis-ci.org/mjpatter88/mjpython)
[![codecov](https://codecov.io/gh/mjpatter88/mjpython/branch/master/graph/badge.svg)](https://codecov.io/gh/mjpatter88/mjpython)

Michael's Python - A virtual machine for Python 3.6 bytecode

To execute tests: `./run_tests.sh`

https://docs.python.org/3.6/library/dis.html

Supported Instructions:
- RETURN_VALUE
- LOAD_CONST
- LOAD_FAST
- STORE_FAST
- BINARY_ADD
- BINARY_SUBTRACT
- BINARY_MULTIPLY
- POP_JUMP_IF_FALSE
- JUMP_ABSOLUTE
- BREAK_LOOP
- SETUP_LOOP
- INPLACE_ADD

Unsupported Instructions:
- 'POP_TOP'
- 'ROT_TWO'
- 'ROT_THREE'
- 'DUP_TOP'
- 'DUP_TOP_TWO'
- 'NOP'
- 'UNARY_POSITIVE'
- 'UNARY_NEGATIVE'
- 'UNARY_NOT'
- 'UNARY_INVERT'
- 'BINARY_MATRIX_MULTIPLY'
- 'INPLACE_MATRIX_MULTIPLY'
- 'BINARY_POWER'
- 'BINARY_MODULO'
- 'BINARY_SUBSCR'
- 'BINARY_FLOOR_DIVIDE'
- 'BINARY_TRUE_DIVIDE'
- 'INPLACE_FLOOR_DIVIDE'
- 'INPLACE_TRUE_DIVIDE'
- 'GET_AITER'
- 'GET_ANEXT'
- 'BEFORE_ASYNC_WITH'
- 'INPLACE_SUBTRACT'
- 'INPLACE_MULTIPLY'
- 'INPLACE_MODULO'
- 'STORE_SUBSCR'
- 'DELETE_SUBSCR'
- 'BINARY_LSHIFT'
- 'BINARY_RSHIFT'
- 'BINARY_AND'
- 'BINARY_XOR'
- 'BINARY_OR'
- 'INPLACE_POWER'
- 'GET_ITER'
- 'GET_YIELD_FROM_ITER'
- 'PRINT_EXPR'
- 'LOAD_BUILD_CLASS'
- 'YIELD_FROM'
- 'GET_AWAITABLE'
- 'INPLACE_LSHIFT'
- 'INPLACE_RSHIFT'
- 'INPLACE_AND'
- 'INPLACE_XOR'
- 'INPLACE_OR'
- 'WITH_CLEANUP_START'
- 'WITH_CLEANUP_FINISH'
- 'IMPORT_STAR'
- 'SETUP_ANNOTATIONS'
- 'YIELD_VALUE'
- 'POP_BLOCK'
- 'END_FINALLY'
- 'POP_EXCEPT'
- 'STORE_NAME'
- 'DELETE_NAME'
- 'UNPACK_SEQUENCE'
- 'FOR_ITER'
- 'UNPACK_EX'
- 'STORE_ATTR'
- 'DELETE_ATTR'
- 'STORE_GLOBAL'
- 'DELETE_GLOBAL'
- 'LOAD_NAME'
- 'BUILD_TUPLE'
- 'BUILD_LIST'
- 'BUILD_SET'
- 'BUILD_MAP'
- 'LOAD_ATTR'
- 'COMPARE_OP'
- 'IMPORT_NAME'
- 'IMPORT_FROM'
- 'JUMP_FORWARD'
- 'JUMP_IF_FALSE_OR_POP'
- 'JUMP_IF_TRUE_OR_POP'
- 'POP_JUMP_IF_TRUE'
- 'LOAD_GLOBAL'
- 'CONTINUE_LOOP'
- 'SETUP_EXCEPT'
- 'SETUP_FINALLY'
- 'DELETE_FAST'
- 'STORE_ANNOTATION'
- 'RAISE_VARARGS'
- 'CALL_FUNCTION'
- 'MAKE_FUNCTION'
- 'BUILD_SLICE'
- 'LOAD_CLOSURE'
- 'LOAD_DEREF'
- 'STORE_DEREF'
- 'DELETE_DEREF'
- 'CALL_FUNCTION_KW'
- 'CALL_FUNCTION_EX'
- 'SETUP_WITH'
- 'LIST_APPEND'
- 'SET_ADD'
- 'MAP_ADD'
- 'LOAD_CLASSDEREF'
- 'EXTENDED_ARG'
- 'BUILD_LIST_UNPACK'
- 'BUILD_MAP_UNPACK'
- 'BUILD_MAP_UNPACK_WITH_CALL'
- 'BUILD_TUPLE_UNPACK'
- 'BUILD_SET_UNPACK'
- 'SETUP_ASYNC_WITH'
- 'FORMAT_VALUE'
- 'BUILD_CONST_KEY_MAP'
- 'BUILD_STRING'
- 'BUILD_TUPLE_UNPACK_WITH_CALL'
