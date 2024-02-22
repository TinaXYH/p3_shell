from .AtomConverter import AtomConverter
from .RedirectionConverter import RedirectionConverter
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser
from ..commands.call.argument.Argument import Argument


class ArgumentConverter(ShellGrammarVisitor):
    def visitArgument(self, ctx: ShellGrammarParser.ArgumentContext):
        argument = Argument()
        for child in ctx.getChildren():
            if isinstance(child, ShellGrammarParser.AtomContext):
                argument.add_content(child.accept(AtomConverter()))
            elif isinstance(child, ShellGrammarParser.RedirectionContext):
                argument.add_content(child.accept(RedirectionConverter()))
        return argument
