from src.apps.Application import Application
from src.exceptions import InvalidArgumentError
from src.utils import *
import os


class Mkdir(Application):
    """
    Create a named folder at a given parent folder.
    """
    
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self):
        
        if len(self.args) < 2:
            raise InvalidArgumentError("Wrong number of command line arguments")

        path = self.args[0]
        mode = self.args[1]
        try:
            os.mkdir(path, mode)
        except OSError as e:
            raise OSError(f"Directory {path} already exists.") from e