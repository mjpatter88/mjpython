from frame import Frame

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
    "BINARY_ADD": operator.add,
    "BINARY_SUBTRACT": operator.sub,
    "BINARY_MULTIPLY": operator.mul,
    "BINARY_POWER": operator.pow,
    "BINARY_FLOOR_DIVIDE": operator.floordiv,
    "BINARY_TRUE_DIVIDE": operator.truediv,
    "BINARY_MODULO": operator.mod,
    "BINARY_SUBSCR": operator.getitem,
    "BINARY_LSHIFT": operator.lshift,
    "BINARY_RSHIFT": operator.rshift,
    "BINARY_AND": operator.and_,
    "BINARY_XOR": operator.xor,
    "BINARY_OR": operator.or_
}

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
        self.push_frame(Frame(code))
        self.run_frame(self.current_frame)
        return self.return_value

    def run_frame(self, frame):
        control_code = None
        while not control_code:
            instr, arg = frame.get_next_instr()
            print(instr, arg)
            func, arg = self.get_func_and_arg(instr, arg)
            if func:
                control_code = func(arg)
            else:
                control_code = "UNSUPPORTED_INSTRUCTION"
        return control_code

    def get_func_and_arg(self, instr, arg):
        if instr.startswith("BINARY"):
            func = self.binary_operation
            arg = BIN_OPS[instr]
            return func, arg
        else:
            return getattr(self, "instr_{}".format(instr), None), arg


    ############################################################################
    def instr_LOAD_CONST(self, arg):
        self.current_frame.stack.append(arg)

    def instr_RETURN_VALUE(self, arg):
        self.return_value = self.current_frame.stack.pop()
        return "RETURN"

    def instr_STORE_FAST(self, arg):
        val = self.current_frame.stack.pop()
        self.current_frame.locals[arg] = val

    def instr_LOAD_FAST(self, arg):
        val = self.current_frame.locals[arg]
        self.current_frame.stack.append(val)
    def instr_INPLACE_ADD(self, arg):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(a+b)

    def instr_COMPARE_OP(self, arg):
        func = CMP_OPS[arg]
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(a, b))

    def instr_POP_JUMP_IF_FALSE(self, arg):
        if not self.current_frame.stack.pop():
            self.current_frame.instr_pointer = arg

    def instr_SETUP_LOOP(self, arg):
        self.current_frame.end_of_loop = arg + self.current_frame.instr_pointer

    def instr_BREAK_LOOP(self, arg):
        self.current_frame.instr_pointer = self.current_frame.end_of_loop

    def instr_POP_BLOCK(self, arg):
        pass

    def instr_JUMP_ABSOLUTE(self, arg):
        self.current_frame.instr_pointer = arg

    # The following method handles all binary operations
    def binary_operation(self, func):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(a, b))
