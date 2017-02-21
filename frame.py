import dis

class Frame():
    def __init__(self, code):
        self.code = code
        self.stack = []
        self.instr_pointer = 0
        self.locals = {}

    def set_local(self, name, value):
        self.locals[name] = value

    def get_next_instr(self):
        byte_code = self.code.co_code[self.instr_pointer]
        self.instr_pointer += 1
        if byte_code in dis.hasconst:
            index = self.code.co_code[self.instr_pointer]
            args = [self.code.co_consts[index]]
        elif byte_code in dis.haslocal:
            index = self.code.co_code[self.instr_pointer]
            args = [self.code.co_varnames[index]]
        elif byte_code in dis.hascompare:
            index = self.code.co_code[self.instr_pointer]
            args = [index]
        elif byte_code in dis.hasjabs:
            index = self.code.co_code[self.instr_pointer]
            args = [index]
        else:
            args = []
        # Python 3.6 moved to a constant instruction size of 2 bytes.
        # https://docs.python.org/3/whatsnew/3.6.html#cpython-bytecode-changes
        self.instr_pointer += 1
        return dis.opname[byte_code], args
