from ply import lex
import termcolor
import re

# Helper function to check if the address is numeric
Ainst_address = re.compile(r'[0-9]+')
def if_address(Ainstruct):
    return bool(Ainst_address.match(Ainstruct))

# List of token names
tokens = (
    "LABEL",
    "ADDRESSES",
    "CINSTRUCTION",
    "AINSTRUCTION",
    "COMMENTS",
    "NEWLINE"
)

# Token definitions
t_LABEL = r'\([A-Za-z0-9]+\)'
t_ADDRESSES = r'\@[0-9]+'
t_AINSTRUCTION = r'\@[A-Za-z0-9]+'
t_CINSTRUCTION = r'[A-Za-z]{1,3}={0,1}[!&|+-]{0,1}[A-Za-z0-9]+;{0,1}[A-Za-z0-9]*'

# Comments definition
t_COMMENTS = r'//.*'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Rule to track line numbers and handle newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def parse_source_code(source_code):
    lexer.input(source_code)
    labels = []
    Ainstr_Address = []
    Ainst_var = []
    Cinstruction = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == "LABEL":
            labels.append(tok.value[1:-1])  # Remove Parenthesis from label
            print(tok.value)
        elif tok.type == "AINSTRUCTION":
            Ainstruct = (tok.value.strip("@"))
            print(termcolor.colored("Ains", "green"))
            print(tok.value)
            if if_address(Ainstruct):
                print(termcolor.colored("Address", "blue"))
                Ainstr_Address.append(tok.value.strip("@"))
            else:
                print(f"the command is {tok.value}")
                Ainst_var.append(tok.value.strip("@"))
        elif tok.type == "CINSTRUCTION":
            print(termcolor.colored("CINSTRUCTION", "magenta"))
            Cinstruction.append(tok.value.strip())
            print(tok.value)
        elif tok.type == "COMMENTS":
            print(tok.value)
        else:
            continue

    return labels, Ainst_var, Ainstr_Address, Cinstruction

# Test input
source = """
// n=2
@2
D=M
(loop)
AD=D-1
0;JMP
@ali
MD=1
AMD=!D
@moham
MD=A-1
AMD=D&A
MD=D|A
AMD=M-D
@15
D=M+D
MD=-D
D;JGT
@R1     // using a label
D=M
(hello world)
(my name is ali)
"""


LAB, VARS, ADDRESSES, CINSTR = parse_source_code(source)
print("Labels:", LAB)
print("Variables:", VARS)
print("Addresses:", ADDRESSES)
print("C Instructions:", CINSTR)
print("Number of C Instructions:", len(CINSTR))
