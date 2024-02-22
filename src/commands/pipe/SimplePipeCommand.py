from .PipeCommand import PipeCommand
from src.commands.call.CallCommand import CallCommand


class SimplePipeCommand(PipeCommand):
    def __init__(self, left_call: CallCommand, right_call: CallCommand):
        self.left = left_call
        self.right = right_call

    def accept(self, visitor):
        return visitor.visit_simple_pipe(self)
