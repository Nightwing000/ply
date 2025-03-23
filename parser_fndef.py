import ply.lex as lex
import ply.yacc as yacc

tokens = ('DEF', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COLON')

reserved = {
    'def': 'DEF'
}

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_function_def(p):
    'function_def : DEF IDENTIFIER LPAREN RPAREN COLON'
    print("Valid function definition")

def p_error(p):
    print("Wrong Syntax")

parser = yacc.yacc()

code = "def my_function():"

parser.parse(code, lexer=lexer)
