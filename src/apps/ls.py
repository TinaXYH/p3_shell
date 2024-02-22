from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
import os
from src.utils import InputInterface, OutputInterface, Directory


class Ls(Application):
    """
    List the content of a directory print a list of files seperated by tabs
    and followed by newline character. Ignores files and directories
    whose name start with '.'
    """

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self) -> OutputInterface:
        match len(self.args):
            case 0:
                directory = Directory(os.getcwd())
            case 1:
                directory = Directory(self.args[0])
            case _:
                raise InvalidArgumentError(f"ls: too many arguments: {self.args[1:]}")
        self.output_interface.set_content(directory.get_contents())
        return self.output_interface
