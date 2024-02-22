from .CallConverter import CallConverter
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser
from ..commands.pipe.SimplePipeCommand import SimplePipeCommand
from ..commands.pipe.RecursivePipeCommand import RecursivePipeCommand


class PipeConverter(ShellGrammarVisitor):
    def visitRecursivePipe(self, ctx: ShellGrammarParser.RecursivePipeContext):
        return RecursivePipeCommand(ctx.left.accept(self), ctx.right.accept(CallConverter()))

    def visitSimplePipe(self, ctx: ShellGrammarParser.SimplePipeContext):
        return SimplePipeCommand(ctx.left.accept(CallConverter()), ctx.right.accept(CallConverter()))
