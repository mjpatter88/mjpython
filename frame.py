import dis

class Frame():
    def __init__(self, code):
        self.code = code
        self.stack = []
        self.instr_pointer = 0

    def get_next_instr(self):
        byte_code = self.code.co_code[self.instr_pointer]
        self.instr_pointer += 1
        if byte_code in dis.hasconst:
            index = self.code.co_code[self.instr_pointer]
            self.instr_pointer += 1
            args = [self.code.co_consts[index]]
        else:
            args = []
        return dis.opname[byte_code], args
