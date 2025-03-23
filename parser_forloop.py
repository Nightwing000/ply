import ply.lex as lex
import ply.yacc as yacc

tokens = ('FOR', 'IN', 'RANGE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COLON', 'NUMBER', 'COMMA')

reserved = {
    'for': 'FOR',
    'in': 'IN',
    'range': 'RANGE'
}

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def p_for_loop(p):
    '''for_loop : FOR IDENTIFIER IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON statement
                | FOR IDENTIFIER IN RANGE LPAREN NUMBER RPAREN COLON statement'''
    print("Valid for loop")

def p_statement(p):
    '''statement : IDENTIFIER
                 | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print("Wrong Syntax")

parser = yacc.yacc()

test_code = [
    "for i in range(1, 10):",
    "for i in range(10):"
]

for code in test_code:
    print(f"Testing code: {code}")
    parser.parse(code, lexer=lexer)
    print("\n---\n")
