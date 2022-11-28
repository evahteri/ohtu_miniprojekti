from app import CommandLineUI

class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def read(self, prompt):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""
    
    def write(self, prompt):
        self.outputs.append(prompt)

    def add_input(self, value):
        self.inputs.append(value)

class AppLibrary:
    def __init__(self):
        self._io = StubIO()
        self._app = CommandLineUI(self._io)

    def input(self, value):
        self._io.add_input(value)

    def run_app(self):
        self._app.start_app()

    def output_should_contain(self, value):
        if not value in self._io.outputs:
            raise AssertionError(f"Output \"{value}\" is not in {str(self._io.outputs)}")
