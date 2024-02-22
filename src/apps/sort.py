from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import *


class Sort(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super(Sort, self).__init__(args, input_interface, output_interface)
        self.contents: list[str] = []
        self.is_reversed = False

    @staticmethod
    def is_legal_option(arg):
        return arg == '-r'

    @staticmethod
    def is_legal_file(arg):
        return len(arg) > 0 and arg[0] != '-'

    def is_legal_args(self):
        if len(self.args) == 0:
            return True
        elif len(self.args) == 1:
            return self.is_legal_option(self.args[0]) or self.is_legal_file(self.args[0])
        elif len(self.args) == 2:
            return self.is_legal_option(self.args[0]) and self.is_legal_file(self.args[1])

    def eval(self) -> OutputInterface:
        if not self.is_legal_args():
            raise InvalidArgumentError(f"Illegal arguments: {self.args}")
        handle = None
        match len(self.args):
            case 0:
                handle = self.input_interface
            case 1:
                if self.is_legal_option(self.args[0]):
                    self.is_reversed = True
                    handle = self.input_interface
                else:
                    handle = File(self.args[0])
            case 2:
                self.is_reversed = True
                handle = File(self.args[1])

        self.contents = handle.readlines()
        sorted_content = sorted(self.contents)
        if self.is_reversed:
            sorted_content.reverse()
        self.output_interface.set_content(sorted_content)
        return self.output_interface
