from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import *
import os


class Touch(Application):
    """
    Create a empty file for a given path.
    """
    
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self):
        if len(self.args) != 1:
            raise InvalidArgumentError("Wrong number of command line arguments")

        if len(self.atgs) == 2:
            path = self.args[0]
            
        try:
            os.open(path, "-x")
        except OSError as e:
            raise OSError(f"File {path} could not be removed.") from e
        