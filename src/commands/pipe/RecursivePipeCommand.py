from .PipeCommand import PipeCommand
from src.commands.call.CallCommand import CallCommand


class RecursivePipeCommand(PipeCommand):
    def __init__(self, left_pipe: PipeCommand, right_call: CallCommand):
        self.left = left_pipe
        self.right = right_call

    def accept(self, visitor):
        return visitor.visit_recursive_pipe(self)
