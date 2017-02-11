prog = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None),
    ],
    "numbers": [7, 5]
}

prog2 = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("LOAD_VALUE", 1),
        ("ADD_TWO_VALUES", None),
        ("LOAD_VALUE", 2),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None),
    ],
    "numbers": [7, 5, 8]
}

class Interpreter:
    def __init__(self):
        self.stack = []

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def ADD_TWO_VALUES(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a+b)

    def run_code(self, code):
        instructions = code["instructions"]
        numbers = code["numbers"]
        for step in instructions:
            instr, arg = step

            if instr == "LOAD_VALUE":
                number = numbers[arg]
                self.LOAD_VALUE(number)
            elif instr == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instr == "PRINT_ANSWER":
                self.PRINT_ANSWER()

if __name__ == '__main__':
    i = Interpreter()
    i.run_code(prog2)
