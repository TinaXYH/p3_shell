from antlr4 import *

from src.commands.CommandErrorListener import CommandErrorListener
from src.grammar.ShellGrammarLexer import ShellGrammarLexer
from src.grammar.ShellGrammarParser import ShellGrammarParser


class CmdTreeConverter:
    @staticmethod
    def convert(cmd):
        in_stream = InputStream(cmd)
        lexer = ShellGrammarLexer(in_stream)
        token_stream = CommonTokenStream(lexer)
        parser = ShellGrammarParser(token_stream)
        parser.removeErrorListeners()
        error_listener = CommandErrorListener()
        parser.addErrorListener(error_listener)
        return parser.prog().command()