from .QuoteConverter import QuoteConverter
from ..commands.call.argument.Atom import Atom
from ..grammar.ShellGrammarVisitor import ShellGrammarVisitor
from ..grammar.ShellGrammarParser import ShellGrammarParser


class AtomConverter(ShellGrammarVisitor):
    def visitAtom(self, ctx: ShellGrammarParser.AtomContext):
        child = ctx.getChild(0)
        if isinstance(child, ShellGrammarParser.QuotedContext):
            return Atom(child.accept(QuoteConverter()))
        else:
            return Atom(child.getText())
