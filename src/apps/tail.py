from .head_and_tail import HeadAndTail
from src.utils import *


class Tail(HeadAndTail):
    def __init__(self, args: list[str], input_interface: InputInterface, output_interface: OutputInterface):
        super().__init__(args, input_interface, output_interface)
        self.LINES = 15

    def eval(self) -> OutputInterface:
        handle = self.get_handle()
        self.LINES *= -1
        self.output_interface.set_content(handle.readlines()[self.LINES:])
        return self.output_interface
