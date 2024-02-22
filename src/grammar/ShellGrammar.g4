grammar ShellGrammar;

// parser
prog : command EOF;

command : pipe                              #pipeCmd
        | left=command ';' right=command    #seqCmd
        | call                              #callCmd
        ;

pipe : left=call '|' right=call    #simplePipe
     | left=pipe '|' right=call    #recursivePipe
     ;

call : WS? app=NON_KEYWORD (WS argument)? WS?;

argument : (redirection WS)* atom (WS (redirection | atom))*;

atom : (quoted | NON_KEYWORD);

redirection : op='<' WS? atom  #redirInput
            | op='>' WS? atom  #redirOuput
            | op='>>' WS? atom #redirAppend
            ;

quoted : single_quoted
       | back_quoted
       | double_quoted
       ;

single_quoted : '\'' single_quoted_content '\'';
back_quoted : '`' back_quoted_content '`';
double_quoted: '"' double_quoted_content '"';

single_quoted_content : (NON_KEYWORD | WS | SEMICOLON | BAR | BQUOTE | DQUOTE )*?;
back_quoted_content : (NON_KEYWORD | WS | SEMICOLON | BAR | SQUOTE | DQUOTE )+?;
double_quoted_content : (back_quoted | d_content=(NON_KEYWORD | WS | SEMICOLON | BAR | SQUOTE)+?)*?;

// lexer

WS : [ \t]+;
NON_KEYWORD : ~[ \t\r\n;|`'"]+;
SEMICOLON : ';';
BAR : '|';
SQUOTE : '\'';
BQUOTE : '`';
DQUOTE : '"';