from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
import os
from src.utils import InputInterface, OutputInterface


class Cd(Application):
    """Changes current working directory"""

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self) -> OutputInterface:
        if not self.args:
            # default to home directory.
            self.args.append(os.path.expanduser("~"))
        if len(self.args) != 1:
            raise InvalidArgumentError(f"cd: too many arguments: {self.args[1:]}")
        os.chdir(self.args[0])
        return self.output_interface
