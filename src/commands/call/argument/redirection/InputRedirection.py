from src.commands.call.argument.redirection.Redirection import Redirection


class InputRedirection(Redirection):

    def __init__(self, filepath):
        super().__init__(filepath)

    def accept(self, visitor):
        return visitor.visit_input_redirection(self)
