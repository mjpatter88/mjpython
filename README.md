# mjpython
[![Build Status](https://travis-ci.org/mjpatter88/mjpython.svg?branch=master)](https://travis-ci.org/mjpatter88/mjpython)
[![codecov](https://codecov.io/gh/mjpatter88/mjpython/branch/master/graph/badge.svg)](https://codecov.io/gh/mjpatter88/mjpython)

Michael's Python - A virtual machine for Python 3.6 bytecode

Execute a python script (from project directory): `./mjpython path_to_script.py`

Test runner: `./run_tests.sh`

Test watcher: `./watch_tests.sh -c -- test/unit`

https://docs.python.org/3.6/library/dis.html

Supported Instructions:

| Binary Instructions  | In-place              | Misc                | Build Data Structures |
|----------------------|-----------------------|---------------------|-----------------------|
| `BINARY_POWER`       | `INPLACE_POWER`       | `RETURN_VALUE`      | `BUILD_CONST_KEY_MAP` |
| `BINARY_MULTIPLY`    | `INPLACE_MULTIPLY`    | `LOAD_CONST`        | `LOAD_BUILD_CLASS`    |
| `BINARY_FLOOR_DIVIDE`| `INPLACE_FLOOR_DIVIDE`| `LOAD_FAST`         |                       |
| `BINARY_TRUE_DIVIDE` | `INPLACE_TRUE_DIVIDE` | `STORE_FAST`        |                       |
| `BINARY_MODULO`      | `INPLACE_MODULO`      | `POP_JUMP_IF_FALSE` |                       |
| `BINARY_ADD`         | `INPLACE_ADD`         | `JUMP_ABSOLUTE`     |                       |
| `BINARY_SUBTRACT`    | `INPLACE_SUBTRACT`    | `BREAK_LOOP`        |                       |
| `BINARY_SUBSCR`      | `INPLACE_LSHIFT`      | `SETUP_LOOP`        |                       |
| `BINARY_LSHIFT`      | `INPLACE_RSHIFT`      | `CALL_FUNCTION`     |                       |
| `BINARY_RSHIFT`      | `INPLACE_AND`         | `CALL_FUNCTION_KW`  |                       |
| `BINARY_AND`         | `INPLACE_XOR`         | `LOAD_NAME`         |                       |
| `BINARY_XOR`         | `INPLACE_OR`          | `POP_TOP`           |                       |
| `BINARY_OR`          |                       | `STORE_NAME`        |                       |


| Imports       |
|---------------|
| `IMPORT_FROM` |
| `IMPORT_NAME` |
| `IMPORT_STAR` |

Unsupported Instructions:
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
- 'GET_AITER'
- 'GET_ANEXT'
- 'BEFORE_ASYNC_WITH'
- 'STORE_SUBSCR'
- 'DELETE_SUBSCR'
- 'GET_ITER'
- 'GET_YIELD_FROM_ITER'
- 'PRINT_EXPR'
- 'YIELD_FROM'
- 'GET_AWAITABLE'
- 'WITH_CLEANUP_START'
- 'WITH_CLEANUP_FINISH'
- 'SETUP_ANNOTATIONS'
- 'YIELD_VALUE'
- 'END_FINALLY'
- 'POP_EXCEPT'
- 'DELETE_NAME'
- 'UNPACK_SEQUENCE'
- 'FOR_ITER'
- 'UNPACK_EX'
- 'STORE_ATTR'
- 'DELETE_ATTR'
- 'STORE_GLOBAL'
- 'DELETE_GLOBAL'
- 'BUILD_TUPLE'
- 'BUILD_LIST'
- 'BUILD_SET'
- 'BUILD_MAP'
- 'LOAD_ATTR'
- 'COMPARE_OP'
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
- 'MAKE_FUNCTION'
- 'BUILD_SLICE'
- 'LOAD_CLOSURE'
- 'LOAD_DEREF'
- 'STORE_DEREF'
- 'DELETE_DEREF'
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
- 'BUILD_STRING'
- 'BUILD_TUPLE_UNPACK_WITH_CALL'
