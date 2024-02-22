from .ArgumentConverter import ArgumentConverter
from ..commands.call.argument.Argument import Argument
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser
from ..commands.call.CallCommand import CallCommand


class CallConverter(ShellGrammarVisitor):
    def visitCall(self, ctx: ShellGrammarParser.CallContext):
        app = ctx.app.text
        argument = ctx.argument()
        arg = argument.accept(ArgumentConverter()) if argument else Argument()
        return CallCommand(app, arg)
