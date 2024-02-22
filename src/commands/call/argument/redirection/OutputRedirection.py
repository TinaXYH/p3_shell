from src.commands.call.argument.redirection.Redirection import Redirection
from abc import ABC


class OutputRedirection(Redirection, ABC):
    def __init__(self, filepath):
        super().__init__(filepath)


class OutputRedirectionOverwrite(OutputRedirection):
    def __init__(self, filepath):
        super().__init__(filepath)

    def accept(self, visitor):
        return visitor.visit_output_overwrite(self)


class OutputRedirectionAppend(OutputRedirection):
    def __init__(self, filepath):
        super().__init__(filepath)

    def accept(self, visitor):
        return visitor.visit_output_append(self)
