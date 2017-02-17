from virtual_machine import VirtualMachine
from frame import Frame

class TestVirtualMachine:
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_init__frames_empty_list(self):
        assert self.vm.frames == []

    def test_init__no_current_frame(self):
        assert self.vm.current_frame == None

    def test_init__no_return_value(self):
        assert self.vm.return_value == None

    def test_push_frame__adds_frame_to_frame_stack(self):
        frame = Frame("foo")
        self.vm.push_frame(frame)
        assert self.vm.frames[0] == frame

    def test_push_frame__sets_current_frame(self):
        frame = Frame("foo")
        self.vm.push_frame(frame)
        assert self.vm.frames[0] == self.vm.current_frame

    def test_run_code__creates_a_new_frame(self):
        code = compile("None", "<string", 'eval')
        self.vm.run_code(code,)
        assert len(self.vm.frames) == 1

    def test_run_code__sets_current_frame_to_the_new_frame(self):
        code = compile("None", "<string", 'eval')
        self.vm.run_code(code,)
        assert self.vm.frames[0] == self.vm.current_frame

    def test_run_code__assigns_given_code_to_the_new_frame(self):
        code = compile("None", "<string>", "eval")
        self.vm.run_code(code,)
        assert self.vm.frames[0].code == code

    def test_run_code__returns_the_result_of_execution(self):
        code = compile("None", "<string>", "eval")
        self.vm.return_value = 10
        assert self.vm.run_code(code) == 10
