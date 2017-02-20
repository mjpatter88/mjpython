from frame import Frame

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
