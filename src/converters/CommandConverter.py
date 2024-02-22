from .CallConverter import CallConverter
from .PipeConverter import PipeConverter
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser
from ..commands.SequenceCommand import SequenceCommand


class CommandConverter(ShellGrammarVisitor):
    def visitSeqCmd(self, ctx: ShellGrammarParser.SeqCmdContext):
        return SequenceCommand(ctx.left.accept(self), ctx.right.accept(self))

    def visitPipeCmd(self, ctx: ShellGrammarParser.PipeCmdContext):
        return ctx.pipe().accept(PipeConverter())

    def visitCallCmd(self, ctx: ShellGrammarParser.CallCmdContext):
        return ctx.call().accept(CallConverter())
