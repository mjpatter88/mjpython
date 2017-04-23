from frame import Frame
from block import Block

from types import FunctionType
import operator

# Comparison operators are defined in cpython/Include/object.h
CMP_OPS = [
    operator.lt,
    operator.le,
    operator.eq,
    operator.ne,
    operator.gt,
    operator.ge,
    lambda x, y: x in y,
    lambda x, y: x not in y,
    lambda x, y: x is y,
    lambda x, y: x is not y,
    lambda x, y: issubclass(x, y)
]

BIN_OPS = {
    "ADD": operator.add,
    "SUBTRACT": operator.sub,
    "MULTIPLY": operator.mul,
    "POWER": operator.pow,
    "FLOOR_DIVIDE": operator.floordiv,
    "TRUE_DIVIDE": operator.truediv,
    "MODULO": operator.mod,
    "SUBSCR": operator.getitem,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "AND": operator.and_,
    "XOR": operator.xor,
    "OR": operator.or_
}

HAS_POS_ARG_DEFS = 1
HAS_KW_ARG_DEFS = 2


class VirtualMachineError(Exception):
    pass


class VirtualMachine():
    def __init__(self):
        self.frames = []
        self.current_frame = None
        self.return_value = None

    def push_frame(self, frame):
        self.frames.append(frame)
        self.current_frame = self.frames[-1]

    def run_code(self, code):
        self.set_code(code)
        self.run()
        return self.return_value

    def set_code(self, code):
        self.push_frame(Frame(code, "__main__"))

    def step(self):
        instr, arg = self.current_frame.get_next_instr()
        func, arg = self.get_func_and_arg(instr, arg)
        # print(instr, arg)
        if func:
            control_code = func(arg)
        else:
            print(instr, arg)
            print(self.current_frame.stack)
            raise VirtualMachineError("Unsupported Instruction: " + instr)
        return control_code

    def run(self):
        control_code = None
        while not control_code:
            control_code = self.step()
        return control_code

    def get_func_and_arg(self, instr, arg):
        if instr.startswith("INPLACE") or instr.startswith("BINARY"):
            func = self.binary_operation
            op = "_".join(instr.split("_")[1:])
            arg = BIN_OPS[op]
            return func, arg
        else:
            return getattr(self, "instr_{}".format(instr), None), arg

    ############################################################################
    def instr_RETURN_VALUE(self, arg):
        self.return_value = self.current_frame.stack.pop()
        return "RETURN"

    def instr_STORE_FAST(self, arg):
        val = self.current_frame.stack.pop()
        self.current_frame.locals[arg] = val

    def instr_LOAD_FAST(self, arg):
        val = self.current_frame.locals[arg]
        self.current_frame.stack.append(val)

    def instr_STORE_NAME(self, arg):
        val = self.current_frame.stack.pop()
        self.current_frame.locals[arg] = val

    def instr_LOAD_NAME(self, arg):
        if arg in self.current_frame.locals:
            val = self.current_frame.locals[arg]
        elif arg in self.current_frame.built_ins:
            val = self.current_frame.built_ins[arg]
        else:
            raise VirtualMachineError("instr_LOAD_NAME name not found: " + arg)
        self.current_frame.stack.append(val)

    def instr_LOAD_GLOBAL(self, arg):
        if arg in self.current_frame.built_ins:
            val = self.current_frame.built_ins[arg]
        else:
            raise VirtualMachineError("instr_LOAD_GLOBAL name not found: " + arg)
        self.current_frame.stack.append(val)

    def instr_LOAD_CONST(self, arg):
        self.current_frame.stack.append(arg)

    def instr_LOAD_ATTR(self, arg):
        obj = self.current_frame.stack.pop()
        self.current_frame.stack.append(getattr(obj, arg))

    def instr_IMPORT_NAME(self, arg):
        from_list = self.current_frame.stack.pop()
        level = self.current_frame.stack.pop()

        # TODO: Implement my own import functionality?
        mod = __import__(arg, globals=globals(), locals=locals(), fromlist=from_list, level=level)
        self.current_frame.stack.append(mod)

    def instr_IMPORT_FROM(self, arg):
        module = self.current_frame.stack[-1]
        attr = getattr(module, arg)
        self.current_frame.stack.append(attr)

    def instr_IMPORT_STAR(self, arg):
        module = self.current_frame.stack[-1]
        symbols = [symbol for symbol in dir(module) if not symbol.startswith('_')]
        for symbol in symbols:
            member = getattr(module, symbol)
            self.current_frame.locals[symbol] = member

    def instr_LOAD_BUILD_CLASS(self, arg):
        class_builder = __builtins__['__build_class__']
        self.current_frame.stack.append(class_builder)

    def instr_COMPARE_OP(self, arg):
        func = CMP_OPS[arg]
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(a, b))

    def instr_POP_JUMP_IF_FALSE(self, arg):
        if not self.current_frame.stack.pop():
            self.current_frame.instr_pointer = arg

    def instr_SETUP_LOOP(self, arg):
        start = self.current_frame.instr_pointer
        end = self.current_frame.instr_pointer + arg
        self.current_frame.blocks.append(Block(start, end))

    def instr_BREAK_LOOP(self, arg):
        end = self.current_frame.blocks[-1].end
        self.current_frame.instr_pointer = end

    def instr_POP_BLOCK(self, arg):
        self.current_frame.blocks.pop()

    def instr_POP_TOP(self, arg):
        self.current_frame.stack.pop()

    def instr_JUMP_ABSOLUTE(self, arg):
        self.current_frame.instr_pointer = arg

    def instr_BUILD_CONST_KEY_MAP(self, arg):
        key_map = {}
        keys = self.current_frame.stack.pop()
        for key in reversed(keys):
            key_map[key] = self.current_frame.stack.pop()
        self.current_frame.stack.append(key_map)

    def instr_MAKE_FUNCTION(self, arg):
        name = self.current_frame.stack.pop()
        code = self.current_frame.stack.pop()

        arg_defs = None
        if arg & HAS_POS_ARG_DEFS:
            arg_defs = self.current_frame.stack.pop()

        # TODO: Replace with custom function creation/execution, create new frame, etc.
        func = FunctionType(code, self.current_frame.built_ins, name=name, argdefs=arg_defs)

        if arg & HAS_KW_ARG_DEFS:
            kw_arg_defs = self.current_frame.stack.pop()
            # TODO: Fix this hack
            func.__kwdefaults__ = kw_arg_defs
        self.current_frame.stack.append(func)

    def instr_CALL_FUNCTION(self, arg):
        pos_args = self._parse_pos_args(arg)
        func = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(*pos_args))

    def instr_CALL_FUNCTION_KW(self, arg):
        kw_args = {}
        kws = self.current_frame.stack.pop()
        num_kws = len(kws)
        for kw in reversed(kws):
            kw_args[kw] = self.current_frame.stack.pop()

        num_pos_args = arg - num_kws
        pos_args = self._parse_pos_args(num_pos_args)

        func = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(*pos_args, **kw_args))

    def _parse_pos_args(self, num):
        # Quote from docs: "The positional arguments are on the stack, with the right-most argument on top."
        args = []
        for i in range(num):
            args.append(self.current_frame.stack.pop())
        return reversed(args)

    # The following method handles all binary operations.
    # It also handles all inplace operations, as they are basically just
    # a special case of the binary operations
    def binary_operation(self, func):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(a, b))
