from src.commands.call.argument.quoted.BackQuoted import BackQuoted
from src.commands.call.argument.quoted.DoubleQuoted import DoubleQuoted
from src.commands.call.argument.quoted.SingleQuoted import SingleQuoted
from src.grammar.ShellGrammarVisitor import ShellGrammarVisitor
from src.grammar.ShellGrammarParser import ShellGrammarParser


class QuoteConverter(ShellGrammarVisitor):
    def __init__(self):
        super().__init__()

    def visitQuoted(self, ctx: ShellGrammarParser.QuotedContext):
        return ctx.getChild(0).accept(self)

    def visitSingle_quoted(self, ctx: ShellGrammarParser.Single_quotedContext):
        return ctx.single_quoted_content().accept(self)

    def visitBack_quoted(self, ctx: ShellGrammarParser.Back_quotedContext):
        return ctx.back_quoted_content().accept(self)

    def visitDouble_quoted(self, ctx: ShellGrammarParser.Double_quotedContext):
        return ctx.double_quoted_content().accept(self)

    def visitSingle_quoted_content(self, ctx: ShellGrammarParser.Single_quoted_contentContext):
        return SingleQuoted("".join(map(lambda c: c.getText(), ctx.getChildren())))

    def visitBack_quoted_content(self, ctx: ShellGrammarParser.Back_quoted_contentContext):
        return BackQuoted("".join(map(lambda c: c.getText(), ctx.getChildren())))

    def visitDouble_quoted_content(self, ctx: ShellGrammarParser.Double_quoted_contentContext):
        return DoubleQuoted(list(map(lambda c: self.visitBack_quoted(c)
                            if isinstance(c, ShellGrammarParser.Back_quotedContext)
                            else c.getText(), ctx.getChildren())))
