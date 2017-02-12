from virtual_machine import VirtualMachine

def test_virtual_machine_init__frames_empty_list():
    vm = VirtualMachine()
    assert vm.frames == []

def test_virtual_machine_init__no_current_frame():
    vm = VirtualMachine()
    assert vm.current_frame == None

def test_virtual_machine_init__no_return_value():
    vm = VirtualMachine()
    assert vm.return_value == None

