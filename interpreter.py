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

#def s():
#    a = 1
#    b = 2
#    print(a + b)
prog3 = {
    "instructions": [
        ("LOAD_VALUE", 0),
        ("STORE_NAME", 0),
        ("LOAD_VALUE", 1),
        ("STORE_NAME", 1),
        ("LOAD_NAME", 0),
        ("LOAD_NAME", 1),
        ("ADD_TWO_VALUES", None),
        ("PRINT_ANSWER", None),
    ],
    "numbers": [1, 2],
    "names": ["a", "b"]
}

class Interpreter:
    def __init__(self):
        self.stack = []
        self.names = {}

    def LOAD_VALUE(self, number):
        self.stack.append(number)

    def PRINT_ANSWER(self):
        print(self.stack.pop())

    def ADD_TWO_VALUES(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a+b)

    def STORE_NAME(self, name):
        self.names[name] = self.stack.pop()

    def LOAD_NAME(self, name):
        self.stack.append(self.names[name])


    def run_code(self, code):
        instructions = code["instructions"]
        numbers = code["numbers"]
        names = code["names"]
        for step in instructions:
            instr, arg = step

            if instr == "LOAD_VALUE":
                number = numbers[arg]
                self.LOAD_VALUE(number)
            elif instr == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()
            elif instr == "PRINT_ANSWER":
                self.PRINT_ANSWER()
            elif instr == "STORE_NAME":
                name = names[arg]
                self.STORE_NAME(name)
            elif instr == "LOAD_NAME":
                name = names[arg]
                self.LOAD_NAME(name)

if __name__ == '__main__':
    i = Interpreter()
    i.run_code(prog3)
