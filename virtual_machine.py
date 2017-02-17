from frame import Frame

class VirtualMachineError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self):
        self.frames = []
        self.current_frame = None
        self.return_value = None

    def push_frame(self, frame):
        self.frames.append(frame)
        self.current_frame = self.frames[-1]

    def run_code(self, code):
        self.push_frame(Frame(code))

        return self.return_value
