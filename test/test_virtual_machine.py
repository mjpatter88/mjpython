from virtual_machine import VirtualMachine

class TestVirtualMachine:
    def setup_method(self):
        self.vm = VirtualMachine()

    def test_init__frames_empty_list(self):
        assert self.vm.frames == []

    def test_init__no_current_frame(self):
        assert self.vm.current_frame == None

    def test_init__no_return_value(self):
        assert self.vm.return_value == None

