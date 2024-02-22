from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface, File


class Uniq(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.ignore_case = False
        self.contents = []
        self.stack = []

    @staticmethod
    def is_legal_option(arg):
        return arg == '-i'

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
            raise InvalidArgumentError(f"illegal arguments: {self.args}")
        match len(self.args):
            case 0:
                self.contents = self.input_interface.readlines()
            case 1:
                if self.is_legal_option(self.args[0]):
                    self.ignore_case = True
                    self.contents = self.input_interface.readlines()
                else:
                    self.contents = File(self.args[0]).readlines()
            case 2:
                self.ignore_case = True
                self.contents = File(self.args[1]).readlines()
            case _:
                raise InvalidArgumentError(f"too many arguments: {self.args[2:]}")
        for content in self.contents:
            parsed_content = content.lower() if self.ignore_case else content
            if len(self.stack) == 0:
                self.stack.append(content)
            elif parsed_content != (self.stack[-1].lower() if self.ignore_case else self.stack[-1]):
                self.stack.append(content)
        self.output_interface.set_content(self.stack)
        return self.output_interface

