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
            instr, args = frame.get_next_instr()
            print(instr, args)
            func = getattr(self, "instr_{}".format(instr), None)
            if func:
                if args:
                    control_code = func(args)
                else:
                    control_code = func()
            else:
                control_code = "UNSUPPORTED_INSTRUCTION"
        return control_code

    ############################################################################
    def instr_LOAD_CONST(self, args):
        self.current_frame.stack.append(args[0])

    def instr_RETURN_VALUE(self):
        self.return_value = self.current_frame.stack.pop()
        return "RETURN"

    def instr_STORE_FAST(self, args):
        key = args[0]
        val = self.current_frame.stack.pop()
        self.current_frame.locals[key] = val

    def instr_LOAD_FAST(self, args):
        key = args[0]
        val = self.current_frame.locals[key]
        self.current_frame.stack.append(val)

    def instr_BINARY_ADD(self):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(a+b)

    def instr_BINARY_SUBTRACT(self):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(a-b)

    def instr_BINARY_MULTIPLY(self):
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(a*b)

    def instr_COMPARE_OP(self, args):
        func = CMP_OPS[args[0]]
        b = self.current_frame.stack.pop()
        a = self.current_frame.stack.pop()
        self.current_frame.stack.append(func(a, b))

    def instr_POP_JUMP_IF_FALSE(self, args):
        if not self.current_frame.stack.pop():
            self.current_frame.instr_pointer = args[0]

    def instr_SETUP_LOOP(self, args):
        self.current_frame.end_of_loop = args[0] + self.current_frame.instr_pointer

    def instr_BREAK_LOOP(self):
        self.current_frame.instr_pointer = self.current_frame.end_of_loop

    def instr_POP_BLOCK(self):
        pass

    def instr_JUMP_ABSOLUTE(self, args):
        self.current_frame.instr_pointer = args[0]
