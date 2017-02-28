from virtual_machine import VirtualMachine

class TestByteCodeObjectExecution():
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_returning_const(self):
        def test_func():
            return 10
        assert self.vm.run_code(test_func.__code__) == 10

    def test_returning_a_large_const(self):
        def test_func():
            return 100000000
        assert self.vm.run_code(test_func.__code__) == 100000000

    def test_adding_two_constants(self):
        def test_func():
            return 10 + 20
        assert self.vm.run_code(test_func.__code__) == 30

    def test_adding_a_constant_and_a_variable(self):
        def test_func():
            a = 15
            return a + 20
        assert self.vm.run_code(test_func.__code__) == 35

    def test_adding_two_variables(self):
        def test_func():
            a = 15
            b = 27
            return a + b
        assert self.vm.run_code(test_func.__code__) == 42

    def test_subtracting_two_variables(self):
        def test_func():
            a = 15
            b = 27
            return b - a
        assert self.vm.run_code(test_func.__code__) == 12

    def test_multiplying_two_variables(self):
        def test_func():
            a = 15
            b = 27
            return a * b
        assert self.vm.run_code(test_func.__code__) == 405

    def test_if_else__takes_if_branch(self):
        def test_func():
            x = 3
            if x < 5:
                return 'yes'
            else:
                return 'no'
        assert self.vm.run_code(test_func.__code__) == 'yes'

    def test_if_else__takes_else_branch(self):
        def test_func():
            x = 8
            if x < 5:
                return 'yes'
            else:
                return 'no'
        assert self.vm.run_code(test_func.__code__) == 'no'

    def test_while_loop(self):
        def test_func():
            x = 10
            while x < 20:
                x = x + 1
            return x
        assert self.vm.run_code(test_func.__code__) == 20

    def test_while_loop_break(self):
        def test_func():
            x = 10
            while x < 20:
                x = x + 1
                break
            return x
        assert self.vm.run_code(test_func.__code__) == 11

    def test_while_loop_continue(self):
        def test_func():
            x = 10
            y = 0
            while y < 5:
                y = y + 1
                if True:
                    continue
                x += 10
            return x
        assert self.vm.run_code(test_func.__code__) == 10
