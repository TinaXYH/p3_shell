from src.apps.Application import Application
from src.exceptions import *
from src.utils import *
import sys


class Exit(Application):
    '''
    Exit shell
    '''

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)

    def eval(self):
        sys.exit()
