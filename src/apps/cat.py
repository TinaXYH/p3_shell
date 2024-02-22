from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import *
from glob import glob


class Cat(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super(Cat, self).__init__(args, input_interface, output_interface)
        self.contents = []

    def eval(self) -> OutputInterface:
        if len(self.args) == 0:
            self.contents = [self.input_interface.read()]
        else:
            for arg in self.args:
                lst_of_files = glob(arg)
                lst_of_files.sort()
                if len(lst_of_files) == 0:
                    raise InvalidArgumentError(f"No matches found: {arg}")
                for file in lst_of_files:
                    self.contents.append(File(file).read())
        self.output_interface.set_content(self.contents)
        return self.output_interface
