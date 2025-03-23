import ply.lex as lex
import ply.yacc as yacc

tokens = ('TRUE', 'FALSE', 'AND', 'OR', 'NOT', 'LPAREN', 'RPAREN')

t_TRUE = r'True'
t_FALSE = r'False'
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

syntax_error = False

def p_expression_bool(p):
    '''expression : TRUE
                  | FALSE
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | LPAREN expression RPAREN'''
    pass

def p_error(p):
    global syntax_error
    syntax_error = True

parser = yacc.yacc()

def check_boolean_expression(input_string):
    global syntax_error
    syntax_error = False
    lexer.input(input_string)
    print("Tokens:")
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)
    parser.parse(input_string, lexer=lexer)
    if syntax_error:
        print("Given Syntax is wrong.")
    else:
        print("Given Syntax is valid.")

print("Test 1:")
check_boolean_expression("True and False or not True")

print("\nTest 2:")
check_boolean_expression("True and (False or True)")

print("\nTest 3 (Invalid):")
check_boolean_expression("True or and False")
