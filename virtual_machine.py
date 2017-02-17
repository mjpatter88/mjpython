from frame import Frame

class VirtualMachineError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self):
        self.frames = []
        self.current_frame = None
        self.return_value = None

    def run_code(self, code):
        self.frames.append(Frame(code))
