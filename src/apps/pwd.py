from src.apps.Application import Application
import os

from src.exceptions import InvalidArgumentError
from src.utils import InputInterface, OutputInterface


class Pwd(Application):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self) -> OutputInterface:
        if len(self.args) != 0:
            raise InvalidArgumentError("pwd: too many arguments")
        self.output_interface.set_content([os.getcwd()])
        return self.output_interface
