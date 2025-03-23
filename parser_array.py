import ply.lex as lex
import ply.yacc as yacc

tokens = ('ID', 'ASSIGN', 'LBRACKET', 'RBRACKET', 'NUMBER', 'COMMA',)

t_ASSIGN = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_array_declaration(p):
    '''array_declaration : ID ASSIGN LBRACKET array_elements RBRACKET'''
    print("Valid array declaration")

def p_array_elements(p):
    '''array_elements : NUMBER COMMA array_elements
                      | NUMBER
                      | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at end of input")

parser = yacc.yacc()

code = "my_list = [1, 2, 3]"

parser.parse(code, lexer=lexer)
