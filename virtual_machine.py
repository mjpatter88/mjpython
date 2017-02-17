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
        instr, args = frame.get_next_instr()
        getattr(self, "instr_{}".format(instr), None)([10])

        instr, args = frame.get_next_instr()
        getattr(self, "instr_{}".format(instr), None)()


    def instr_LOAD_CONST(self, args):
        self.current_frame.stack.append(args[0])

    def instr_RETURN_VALUE(self):
        self.return_value = self.current_frame.stack.pop()
