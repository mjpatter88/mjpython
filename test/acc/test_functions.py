
import os
import subprocess

class TestPrinting:
    def setup_method(self):
        self.test_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "scripts")

    def test_functions(self):
        test_file_name = "functions.py"
        test_target = os.path.join(self.test_dir, test_file_name)

        output = subprocess.check_output(["python", test_target])
        my_output = subprocess.check_output(["python", "mjpython.py", test_target])

        assert my_output == output
