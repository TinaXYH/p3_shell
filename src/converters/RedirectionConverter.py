from ..commands.call.argument.redirection import *
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser
from .AtomConverter import AtomConverter


class RedirectionConverter(ShellGrammarVisitor):
    @staticmethod
    def get_converted_atom(ctx):
        return ctx.atom().accept(AtomConverter())
    
    def visitRedirInput(self, ctx: ShellGrammarParser.RedirInputContext):
        return InputRedirection(self.get_converted_atom(ctx))

    def visitRedirOuput(self, ctx: ShellGrammarParser.RedirOuputContext):
        return OutputRedirectionOverwrite(self.get_converted_atom(ctx))

    def visitRedirAppend(self, ctx: ShellGrammarParser.RedirAppendContext):
        return OutputRedirectionAppend(self.get_converted_atom(ctx))
