from .Application import Application
from abc import ABC
from ..exceptions import InvalidArgumentError
from ..utils import InputInterface, OutputInterface, File


class HeadAndTail(Application, ABC):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.LINES = 15

    @staticmethod
    def is_legal_file(arg: str):
        return arg != "" and arg[0] != '-'

    @staticmethod
    def is_legal_option(opt1, opt2):
        return opt1 == "-n" and int(opt2) > 0

    def is_legal_args(self):
        if len(self.args) == 0:
            return True
        elif len(self.args) == 1:
            return self.is_legal_file(self.args[0])
        elif len(self.args) == 2:
            return self.is_legal_option(self.args[0], self.args[1])
        elif len(self.args) == 3:
            return self.is_legal_option(self.args[0], self.args[1]) \
                   and self.is_legal_file(self.args[2])
        else:
            return False

    def get_handle(self) -> File | InputInterface:
        if not self.is_legal_args():
            raise InvalidArgumentError(f"Illegal arguments: {self.args}")
        match len(self.args):
            case 0:
                return self.input_interface
            case 1:
                return File(self.args[0])
            case 2:
                self.LINES = int(self.args[1])
                return self.input_interface
            case 3:
                self.LINES = int(self.args[1])
                return File(self.args[2])
