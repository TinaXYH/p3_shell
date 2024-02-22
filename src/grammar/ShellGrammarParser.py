# Generated from src/grammar/ShellGrammar.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,148,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,1,0,1,0,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,5,1,40,8,1,10,1,12,
        1,43,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,53,8,2,10,2,12,2,56,
        9,2,1,3,3,3,59,8,3,1,3,1,3,1,3,3,3,64,8,3,1,3,3,3,67,8,3,1,4,1,4,
        1,4,5,4,72,8,4,10,4,12,4,75,9,4,1,4,1,4,1,4,1,4,3,4,81,8,4,5,4,83,
        8,4,10,4,12,4,86,9,4,1,5,1,5,3,5,90,8,5,1,6,1,6,3,6,94,8,6,1,6,1,
        6,1,6,3,6,99,8,6,1,6,1,6,1,6,3,6,104,8,6,1,6,3,6,107,8,6,1,7,1,7,
        1,7,3,7,112,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,11,5,11,127,8,11,10,11,12,11,130,9,11,1,12,4,12,133,8,12,11,
        12,12,12,134,1,13,1,13,4,13,139,8,13,11,13,12,13,140,5,13,143,8,
        13,10,13,12,13,146,9,13,1,13,4,128,134,140,144,2,2,4,14,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,0,3,2,0,4,7,9,10,2,0,4,8,10,10,1,0,
        4,8,155,0,28,1,0,0,0,2,34,1,0,0,0,4,44,1,0,0,0,6,58,1,0,0,0,8,73,
        1,0,0,0,10,89,1,0,0,0,12,106,1,0,0,0,14,111,1,0,0,0,16,113,1,0,0,
        0,18,117,1,0,0,0,20,121,1,0,0,0,22,128,1,0,0,0,24,132,1,0,0,0,26,
        144,1,0,0,0,28,29,3,2,1,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,6,1,-1,
        0,32,35,3,4,2,0,33,35,3,6,3,0,34,31,1,0,0,0,34,33,1,0,0,0,35,41,
        1,0,0,0,36,37,10,2,0,0,37,38,5,6,0,0,38,40,3,2,1,3,39,36,1,0,0,0,
        40,43,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,
        0,0,44,45,6,2,-1,0,45,46,3,6,3,0,46,47,5,7,0,0,47,48,3,6,3,0,48,
        54,1,0,0,0,49,50,10,1,0,0,50,51,5,7,0,0,51,53,3,6,3,0,52,49,1,0,
        0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,54,
        1,0,0,0,57,59,5,4,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,
        60,63,5,5,0,0,61,62,5,4,0,0,62,64,3,8,4,0,63,61,1,0,0,0,63,64,1,
        0,0,0,64,66,1,0,0,0,65,67,5,4,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,
        7,1,0,0,0,68,69,3,12,6,0,69,70,5,4,0,0,70,72,1,0,0,0,71,68,1,0,0,
        0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,
        1,0,0,0,76,84,3,10,5,0,77,80,5,4,0,0,78,81,3,12,6,0,79,81,3,10,5,
        0,80,78,1,0,0,0,80,79,1,0,0,0,81,83,1,0,0,0,82,77,1,0,0,0,83,86,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,9,1,0,0,0,86,84,1,0,0,0,87,
        90,3,14,7,0,88,90,5,5,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,11,1,0,
        0,0,91,93,5,1,0,0,92,94,5,4,0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,
        1,0,0,0,95,107,3,10,5,0,96,98,5,2,0,0,97,99,5,4,0,0,98,97,1,0,0,
        0,98,99,1,0,0,0,99,100,1,0,0,0,100,107,3,10,5,0,101,103,5,3,0,0,
        102,104,5,4,0,0,103,102,1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,
        105,107,3,10,5,0,106,91,1,0,0,0,106,96,1,0,0,0,106,101,1,0,0,0,107,
        13,1,0,0,0,108,112,3,16,8,0,109,112,3,18,9,0,110,112,3,20,10,0,111,
        108,1,0,0,0,111,109,1,0,0,0,111,110,1,0,0,0,112,15,1,0,0,0,113,114,
        5,8,0,0,114,115,3,22,11,0,115,116,5,8,0,0,116,17,1,0,0,0,117,118,
        5,9,0,0,118,119,3,24,12,0,119,120,5,9,0,0,120,19,1,0,0,0,121,122,
        5,10,0,0,122,123,3,26,13,0,123,124,5,10,0,0,124,21,1,0,0,0,125,127,
        7,0,0,0,126,125,1,0,0,0,127,130,1,0,0,0,128,129,1,0,0,0,128,126,
        1,0,0,0,129,23,1,0,0,0,130,128,1,0,0,0,131,133,7,1,0,0,132,131,1,
        0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,134,132,1,0,0,0,135,25,1,0,
        0,0,136,143,3,18,9,0,137,139,7,2,0,0,138,137,1,0,0,0,139,140,1,0,
        0,0,140,141,1,0,0,0,140,138,1,0,0,0,141,143,1,0,0,0,142,136,1,0,
        0,0,142,138,1,0,0,0,143,146,1,0,0,0,144,145,1,0,0,0,144,142,1,0,
        0,0,145,27,1,0,0,0,146,144,1,0,0,0,20,34,41,54,58,63,66,73,80,84,
        89,93,98,103,106,111,128,134,140,142,144
    ]

class ShellGrammarParser ( Parser ):

    grammarFileName = "ShellGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<'", "'>'", "'>>'", "<INVALID>", "<INVALID>", 
                     "';'", "'|'", "'''", "'`'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "NON_KEYWORD", "SEMICOLON", "BAR", "SQUOTE", 
                      "BQUOTE", "DQUOTE" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_argument = 4
    RULE_atom = 5
    RULE_redirection = 6
    RULE_quoted = 7
    RULE_single_quoted = 8
    RULE_back_quoted = 9
    RULE_double_quoted = 10
    RULE_single_quoted_content = 11
    RULE_back_quoted_content = 12
    RULE_double_quoted_content = 13

    ruleNames =  [ "prog", "command", "pipe", "call", "argument", "atom", 
                   "redirection", "quoted", "single_quoted", "back_quoted", 
                   "double_quoted", "single_quoted_content", "back_quoted_content", 
                   "double_quoted_content" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    WS=4
    NON_KEYWORD=5
    SEMICOLON=6
    BAR=7
    SQUOTE=8
    BQUOTE=9
    DQUOTE=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(ShellGrammarParser.CommandContext,0)


        def EOF(self):
            return self.getToken(ShellGrammarParser.EOF, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ShellGrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.command(0)
            self.state = 29
            self.match(ShellGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SeqCmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.CommandContext
            super().__init__(parser)
            self.left = None # CommandContext
            self.right = None # CommandContext
            self.copyFrom(ctx)

        def SEMICOLON(self):
            return self.getToken(ShellGrammarParser.SEMICOLON, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.CommandContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CommandContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeqCmd" ):
                return visitor.visitSeqCmd(self)
            else:
                return visitor.visitChildren(self)


    class PipeCmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipeCmd" ):
                return visitor.visitPipeCmd(self)
            else:
                return visitor.visitChildren(self)


    class CallCmdContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(ShellGrammarParser.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallCmd" ):
                return visitor.visitCallCmd(self)
            else:
                return visitor.visitChildren(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShellGrammarParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = ShellGrammarParser.PipeCmdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 32
                self.pipe(0)
                pass

            elif la_ == 2:
                localctx = ShellGrammarParser.CallCmdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.SeqCmdContext(self, ShellGrammarParser.CommandContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 36
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 37
                    self.match(ShellGrammarParser.SEMICOLON)
                    self.state = 38
                    localctx.right = self.command(3) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_pipe

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class RecursivePipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.PipeContext
            super().__init__(parser)
            self.left = None # PipeContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def BAR(self):
            return self.getToken(ShellGrammarParser.BAR, 0)
        def pipe(self):
            return self.getTypedRuleContext(ShellGrammarParser.PipeContext,0)

        def call(self):
            return self.getTypedRuleContext(ShellGrammarParser.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecursivePipe" ):
                return visitor.visitRecursivePipe(self)
            else:
                return visitor.visitChildren(self)


    class SimplePipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.PipeContext
            super().__init__(parser)
            self.left = None # CallContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def BAR(self):
            return self.getToken(ShellGrammarParser.BAR, 0)
        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.CallContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.CallContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimplePipe" ):
                return visitor.visitSimplePipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ShellGrammarParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ShellGrammarParser.SimplePipeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 45
            localctx.left = self.call()
            self.state = 46
            self.match(ShellGrammarParser.BAR)
            self.state = 47
            localctx.right = self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ShellGrammarParser.RecursivePipeContext(self, ShellGrammarParser.PipeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 49
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 50
                    self.match(ShellGrammarParser.BAR)
                    self.state = 51
                    localctx.right = self.call() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.app = None # Token

        def NON_KEYWORD(self):
            return self.getToken(ShellGrammarParser.NON_KEYWORD, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def argument(self):
            return self.getTypedRuleContext(ShellGrammarParser.ArgumentContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ShellGrammarParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 57
                self.match(ShellGrammarParser.WS)


            self.state = 60
            localctx.app = self.match(ShellGrammarParser.NON_KEYWORD)
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 61
                self.match(ShellGrammarParser.WS)
                self.state = 62
                self.argument()


            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(ShellGrammarParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.AtomContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.AtomContext,i)


        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.RedirectionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = ShellGrammarParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0:
                self.state = 68
                self.redirection()
                self.state = 69
                self.match(ShellGrammarParser.WS)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.atom()
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 77
                    self.match(ShellGrammarParser.WS)
                    self.state = 80
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [1, 2, 3]:
                        self.state = 78
                        self.redirection()
                        pass
                    elif token in [5, 8, 9, 10]:
                        self.state = 79
                        self.atom()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.QuotedContext,0)


        def NON_KEYWORD(self):
            return self.getToken(ShellGrammarParser.NON_KEYWORD, 0)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ShellGrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.state = 87
                self.quoted()
                pass
            elif token in [5]:
                self.state = 88
                self.match(ShellGrammarParser.NON_KEYWORD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_redirection

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RedirInputContext(RedirectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.RedirectionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ShellGrammarParser.AtomContext,0)

        def WS(self):
            return self.getToken(ShellGrammarParser.WS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirInput" ):
                return visitor.visitRedirInput(self)
            else:
                return visitor.visitChildren(self)


    class RedirAppendContext(RedirectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.RedirectionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ShellGrammarParser.AtomContext,0)

        def WS(self):
            return self.getToken(ShellGrammarParser.WS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirAppend" ):
                return visitor.visitRedirAppend(self)
            else:
                return visitor.visitChildren(self)


    class RedirOuputContext(RedirectionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ShellGrammarParser.RedirectionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ShellGrammarParser.AtomContext,0)

        def WS(self):
            return self.getToken(ShellGrammarParser.WS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirOuput" ):
                return visitor.visitRedirOuput(self)
            else:
                return visitor.visitChildren(self)



    def redirection(self):

        localctx = ShellGrammarParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ShellGrammarParser.RedirInputContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                localctx.op = self.match(ShellGrammarParser.T__0)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 92
                    self.match(ShellGrammarParser.WS)


                self.state = 95
                self.atom()
                pass
            elif token in [2]:
                localctx = ShellGrammarParser.RedirOuputContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                localctx.op = self.match(ShellGrammarParser.T__1)
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 97
                    self.match(ShellGrammarParser.WS)


                self.state = 100
                self.atom()
                pass
            elif token in [3]:
                localctx = ShellGrammarParser.RedirAppendContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                localctx.op = self.match(ShellGrammarParser.T__2)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 102
                    self.match(ShellGrammarParser.WS)


                self.state = 105
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Single_quotedContext,0)


        def back_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Back_quotedContext,0)


        def double_quoted(self):
            return self.getTypedRuleContext(ShellGrammarParser.Double_quotedContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = ShellGrammarParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_quoted)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.single_quoted()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.back_quoted()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.double_quoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SQUOTE)
            else:
                return self.getToken(ShellGrammarParser.SQUOTE, i)

        def single_quoted_content(self):
            return self.getTypedRuleContext(ShellGrammarParser.Single_quoted_contentContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_single_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_quoted" ):
                return visitor.visitSingle_quoted(self)
            else:
                return visitor.visitChildren(self)




    def single_quoted(self):

        localctx = ShellGrammarParser.Single_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_single_quoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ShellGrammarParser.SQUOTE)
            self.state = 114
            self.single_quoted_content()
            self.state = 115
            self.match(ShellGrammarParser.SQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Back_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BQUOTE)
            else:
                return self.getToken(ShellGrammarParser.BQUOTE, i)

        def back_quoted_content(self):
            return self.getTypedRuleContext(ShellGrammarParser.Back_quoted_contentContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_back_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBack_quoted" ):
                return visitor.visitBack_quoted(self)
            else:
                return visitor.visitChildren(self)




    def back_quoted(self):

        localctx = ShellGrammarParser.Back_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_back_quoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ShellGrammarParser.BQUOTE)
            self.state = 118
            self.back_quoted_content()
            self.state = 119
            self.match(ShellGrammarParser.BQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Double_quotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.DQUOTE)
            else:
                return self.getToken(ShellGrammarParser.DQUOTE, i)

        def double_quoted_content(self):
            return self.getTypedRuleContext(ShellGrammarParser.Double_quoted_contentContext,0)


        def getRuleIndex(self):
            return ShellGrammarParser.RULE_double_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble_quoted" ):
                return visitor.visitDouble_quoted(self)
            else:
                return visitor.visitChildren(self)




    def double_quoted(self):

        localctx = ShellGrammarParser.Double_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_double_quoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(ShellGrammarParser.DQUOTE)
            self.state = 122
            self.double_quoted_content()
            self.state = 123
            self.match(ShellGrammarParser.DQUOTE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_quoted_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NON_KEYWORD)
            else:
                return self.getToken(ShellGrammarParser.NON_KEYWORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SEMICOLON)
            else:
                return self.getToken(ShellGrammarParser.SEMICOLON, i)

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BAR)
            else:
                return self.getToken(ShellGrammarParser.BAR, i)

        def BQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BQUOTE)
            else:
                return self.getToken(ShellGrammarParser.BQUOTE, i)

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.DQUOTE)
            else:
                return self.getToken(ShellGrammarParser.DQUOTE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_single_quoted_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_quoted_content" ):
                return visitor.visitSingle_quoted_content(self)
            else:
                return visitor.visitChildren(self)




    def single_quoted_content(self):

        localctx = ShellGrammarParser.Single_quoted_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_single_quoted_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 125
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1776) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Back_quoted_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NON_KEYWORD)
            else:
                return self.getToken(ShellGrammarParser.NON_KEYWORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SEMICOLON)
            else:
                return self.getToken(ShellGrammarParser.SEMICOLON, i)

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BAR)
            else:
                return self.getToken(ShellGrammarParser.BAR, i)

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SQUOTE)
            else:
                return self.getToken(ShellGrammarParser.SQUOTE, i)

        def DQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.DQUOTE)
            else:
                return self.getToken(ShellGrammarParser.DQUOTE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_back_quoted_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBack_quoted_content" ):
                return visitor.visitBack_quoted_content(self)
            else:
                return visitor.visitChildren(self)




    def back_quoted_content(self):

        localctx = ShellGrammarParser.Back_quoted_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_back_quoted_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 131
                    _la = self._input.LA(1)
                    if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1520) != 0):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 134 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Double_quoted_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.d_content = None # Token

        def back_quoted(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ShellGrammarParser.Back_quotedContext)
            else:
                return self.getTypedRuleContext(ShellGrammarParser.Back_quotedContext,i)


        def NON_KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.NON_KEYWORD)
            else:
                return self.getToken(ShellGrammarParser.NON_KEYWORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.WS)
            else:
                return self.getToken(ShellGrammarParser.WS, i)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SEMICOLON)
            else:
                return self.getToken(ShellGrammarParser.SEMICOLON, i)

        def BAR(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.BAR)
            else:
                return self.getToken(ShellGrammarParser.BAR, i)

        def SQUOTE(self, i:int=None):
            if i is None:
                return self.getTokens(ShellGrammarParser.SQUOTE)
            else:
                return self.getToken(ShellGrammarParser.SQUOTE, i)

        def getRuleIndex(self):
            return ShellGrammarParser.RULE_double_quoted_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble_quoted_content" ):
                return visitor.visitDouble_quoted_content(self)
            else:
                return visitor.visitChildren(self)




    def double_quoted_content(self):

        localctx = ShellGrammarParser.Double_quoted_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_double_quoted_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 142
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [9]:
                        self.state = 136
                        self.back_quoted()
                        pass
                    elif token in [4, 5, 6, 7, 8]:
                        self.state = 138 
                        self._errHandler.sync(self)
                        _alt = 1+1
                        while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1+1:
                                self.state = 137
                                localctx.d_content = self._input.LT(1)
                                _la = self._input.LA(1)
                                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 496) != 0):
                                    localctx.d_content = self._errHandler.recoverInline(self)
                                else:
                                    self._errHandler.reportMatch(self)
                                    self.consume()

                            else:
                                raise NoViableAltException(self)
                            self.state = 140 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.command_sempred
        self._predicates[2] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




