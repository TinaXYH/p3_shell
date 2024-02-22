from .head_and_tail import HeadAndTail
from src.utils import *


class Head(HeadAndTail):
    """
    Prints the first N lines of a given file or stdin.
    If there are less than N lines, prints only the existing lines without raising an exception.
    """

    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.LINES = 15

    def eval(self) -> OutputInterface:
        handle = self.get_handle()
        self.output_interface.set_content(handle.readlines()[:self.LINES])
        return self.output_interface


