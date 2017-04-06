import dis


class Frame:
    def __init__(self, code, name=None):
        self.code = code
        self.stack = []
        self.instr_pointer = 0
        self.locals = {"__name__": name}
        self.blocks = []
        self.built_ins = __builtins__

    def set_local(self, name, value):
        self.locals[name] = value

    def get_next_instr(self):
        # Python 3.6 moved to a constant instruction size of 2 bytes.
        # https://docs.python.org/3/whatsnew/3.6.html#cpython-bytecode-changes
        byte_code = self.code.co_code[self.instr_pointer]
        arg = self.code.co_code[self.instr_pointer + 1]
        self.instr_pointer += 2
        if byte_code in dis.hasconst:
            arg = self.code.co_consts[arg]
        elif byte_code in dis.haslocal:
            arg = self.code.co_varnames[arg]
        elif byte_code in dis.hasname:
            arg = self.code.co_names[arg]
        return dis.opname[byte_code], arg
