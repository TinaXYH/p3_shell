from antlr4.error.ErrorListener import ErrorListener
from src.exceptions import IllegalCommandError


class CommandErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise IllegalCommandError("illegal command")
