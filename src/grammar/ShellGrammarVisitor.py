# Generated from src/grammar/ShellGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ShellGrammarParser import ShellGrammarParser
else:
    from ShellGrammarParser import ShellGrammarParser

# This class defines a complete generic visitor for a parse tree produced by ShellGrammarParser.

class ShellGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShellGrammarParser#prog.
    def visitProg(self, ctx:ShellGrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#seqCmd.
    def visitSeqCmd(self, ctx:ShellGrammarParser.SeqCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#pipeCmd.
    def visitPipeCmd(self, ctx:ShellGrammarParser.PipeCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#callCmd.
    def visitCallCmd(self, ctx:ShellGrammarParser.CallCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#recursivePipe.
    def visitRecursivePipe(self, ctx:ShellGrammarParser.RecursivePipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#simplePipe.
    def visitSimplePipe(self, ctx:ShellGrammarParser.SimplePipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#call.
    def visitCall(self, ctx:ShellGrammarParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#argument.
    def visitArgument(self, ctx:ShellGrammarParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#atom.
    def visitAtom(self, ctx:ShellGrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#redirInput.
    def visitRedirInput(self, ctx:ShellGrammarParser.RedirInputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#redirOuput.
    def visitRedirOuput(self, ctx:ShellGrammarParser.RedirOuputContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#redirAppend.
    def visitRedirAppend(self, ctx:ShellGrammarParser.RedirAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#quoted.
    def visitQuoted(self, ctx:ShellGrammarParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#single_quoted.
    def visitSingle_quoted(self, ctx:ShellGrammarParser.Single_quotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#back_quoted.
    def visitBack_quoted(self, ctx:ShellGrammarParser.Back_quotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#double_quoted.
    def visitDouble_quoted(self, ctx:ShellGrammarParser.Double_quotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#single_quoted_content.
    def visitSingle_quoted_content(self, ctx:ShellGrammarParser.Single_quoted_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#back_quoted_content.
    def visitBack_quoted_content(self, ctx:ShellGrammarParser.Back_quoted_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShellGrammarParser#double_quoted_content.
    def visitDouble_quoted_content(self, ctx:ShellGrammarParser.Double_quoted_contentContext):
        return self.visitChildren(ctx)



del ShellGrammarParser