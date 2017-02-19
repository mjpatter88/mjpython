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
