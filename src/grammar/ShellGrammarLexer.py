# Generated from src/grammar/ShellGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,48,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,4,
        3,30,8,3,11,3,12,3,31,1,4,4,4,35,8,4,11,4,12,4,36,1,5,1,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,1,0,2,2,0,9,9,32,32,8,0,9,10,13,13,32,32,34,34,39,39,
        59,59,96,96,124,124,49,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,
        0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,29,1,
        0,0,0,9,34,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,0,0,0,17,
        44,1,0,0,0,19,46,1,0,0,0,21,22,5,60,0,0,22,2,1,0,0,0,23,24,5,62,
        0,0,24,4,1,0,0,0,25,26,5,62,0,0,26,27,5,62,0,0,27,6,1,0,0,0,28,30,
        7,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,8,1,0,0,0,33,35,8,1,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,
        0,0,36,37,1,0,0,0,37,10,1,0,0,0,38,39,5,59,0,0,39,12,1,0,0,0,40,
        41,5,124,0,0,41,14,1,0,0,0,42,43,5,39,0,0,43,16,1,0,0,0,44,45,5,
        96,0,0,45,18,1,0,0,0,46,47,5,34,0,0,47,20,1,0,0,0,3,0,31,36,0
    ]

class ShellGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    WS = 4
    NON_KEYWORD = 5
    SEMICOLON = 6
    BAR = 7
    SQUOTE = 8
    BQUOTE = 9
    DQUOTE = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'<'", "'>'", "'>>'", "';'", "'|'", "'''", "'`'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "NON_KEYWORD", "SEMICOLON", "BAR", "SQUOTE", "BQUOTE", 
            "DQUOTE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "WS", "NON_KEYWORD", "SEMICOLON", 
                  "BAR", "SQUOTE", "BQUOTE", "DQUOTE" ]

    grammarFileName = "ShellGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


