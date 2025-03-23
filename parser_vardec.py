import ply.lex as lex
import ply.yacc as yacc

tokens = ['ID', 'NUMBER', 'STRING', 'ASSIGN', 'TRUE', 'FALSE']
t_ASSIGN = r'='

reserved = {
    'True': 'TRUE',
    'False': 'FALSE'
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\"]|\\.)*\"'
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

syntax_error = False

def p_program(p):
    '''program : statement
               | statement program'''
    pass

def p_statement_var_assign(p):
    '''statement : ID ASSIGN expression'''
    print(f"Valid variable assignment: {p[1]} = {p[3]}")

def p_expression(p):
    '''expression : NUMBER
                  | STRING
                  | TRUE
                  | FALSE'''
    p[0] = p[1]

def p_error(p):
    global syntax_error
    print("Syntax error in input!")
    syntax_error = True

parser = yacc.yacc()

code = '''
x = 10
name = "Alice"
flag = True
'''

syntax_error = False

print("\nParsing Result:")
parser.parse(code)

if syntax_error:
    print("Syntax is NOT valid.")
else:
    print("Syntax is valid.")
