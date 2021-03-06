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

    def test_in_place_add(self):
        def test_func():
            a = 15
            a += 5
            return a
        assert self.vm.run_code(test_func.__code__) == 20

    def test_in_place_floor_division(self):
        def test_func():
            a = 10
            a //= 3
            return a
        assert self.vm.run_code(test_func.__code__) == 3

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

    def test_nested_while_loop(self):
        def test_func():
            a = 0
            x = 0
            y = 0
            while x < 10:
                y = 0
                while y < 11:
                    a += 1
                    y += 1
                x += 1
            return a
        assert self.vm.run_code(test_func.__code__) == 110

    def test_built_in_functions(self):
        def test_func():
            return abs(-5)
        assert self.vm.run_code(test_func.__code__) == 5

    def test_built_in_sum_function(self):
        def test_func():
            return sum((1,2,3,4))
        assert self.vm.run_code(test_func.__code__) == 10

    def test_make_and_call_function(self):
        def test_func():
            def test_inner_func():
                return 7
            return test_inner_func()
        assert self.vm.run_code(test_func.__code__) == 7

    def test_make_and_call_function_pos_args(self):
        def test_func():
            def test_inner_func(a, b):
                return a + b
            return test_inner_func(10, 15)
        assert self.vm.run_code(test_func.__code__) == 25

    def test_make_and_call_function_pos_args_ordering(self):
        def test_func():
            def test_inner_func(a, b):
                return a - b
            return test_inner_func(15, 10)
        assert self.vm.run_code(test_func.__code__) == 5

    def test_make_and_call_function_keyword_args(self):
        def test_func():
            def test_inner_func(a=0, b=0):
                return a + b
            return test_inner_func(a=10, b=15)
        assert self.vm.run_code(test_func.__code__) == 25

    def test_make_and_call_function_keyword_args_reverse_order(self):
        def test_func():
            def test_inner_func(a=0, b=0):
                return a - b
            return test_inner_func(b=15, a=10)
        assert self.vm.run_code(test_func.__code__) == -5

    def test_make_and_call_function_keyword_args_and_pos_args(self):
        def test_func():
            def test_inner_func(a, b, c=100, d=200):
                return a + b - (c + d)
            return test_inner_func(14, 13, c=4, d=3)
        assert self.vm.run_code(test_func.__code__) == 20

    def test_make_and_call_function_with_var_args(self):
        def test_func():
            def test_inner_func(*args):
                a = sum(args)
                return a
            return test_inner_func(1, 2, 3, 4)
        assert self.vm.run_code(test_func.__code__) == 10

    def test_make_and_call_function_with_var_args_and_var_kw_args(self):
        def test_func():
            def test_inner_func(*args, **kwargs):
                a = sum(args)
                a += kwargs['bonus']
                return a
            return test_inner_func(1, 2, 3, 4, bonus=10)
        assert self.vm.run_code(test_func.__code__) == 20

    def test_make_and_call_function_pos_args_defaul_values(self):
        def test_func():
            def test_inner_func(a=4, b=7, c=1):
                return a + b - c
            return test_inner_func()
        assert self.vm.run_code(test_func.__code__) == 10

    def test_make_and_call_function_keyword_args_defaul_values(self):
        def test_func():
            def test_inner_func(a, *args, b=6, c=1):
                return a + b - c
            return test_inner_func(14, b=7)
        assert self.vm.run_code(test_func.__code__) == 20

#    def test_make_and_call_function_closure(self):
#        def test_func():
#            a = 3
#            def test_inner_func():
#                return 7 + a
#            return test_inner_func()
#        assert self.vm.run_code(test_func.__code__) == 10

    def test_import_a_std_lib(self):
        def test_func():
            import math
            return math
        import math
        assert self.vm.run_code(test_func.__code__) == math

    def test_import_attr_from_a_std_lib(self):
        def test_func():
            from random import shuffle
            return shuffle
        from random import shuffle
        assert self.vm.run_code(test_func.__code__) == shuffle

    def test_import_multiple_attr_from_a_std_lib(self):
        def test_func():
            from math import pi, e, tau
            return pi + e + tau
        from math import pi, e, tau
        assert self.vm.run_code(test_func.__code__) == pi + e + tau

    def test_import_mod_from_a_std_lib(self):
        def test_func():
            from test import support
            return support
        from test import support
        assert self.vm.run_code(test_func.__code__) == support

    def test_build_class(self):
        def test_func():
            class Foo:
                pass
            return Foo
        assert type(self.vm.run_code(test_func.__code__)) == type(type)

    def test_load_attribute(self):
        def test_func():
            import math
            a = math.pi
            return a
        import math
        assert self.vm.run_code(test_func.__code__) == math.pi
