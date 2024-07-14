from ply import lex
import termcolor
import re

Ainst_address = re.compile(r'[0-9]+')
def if_address(Ainstruct):
      return bool(Ainst_address.match(Ainstruct))

tokens = (
  "LABEL",
  "ADDRESSES",
  "CINSTRUCTION",
  "AINSTRUCTION",
  "COMMENTS"
)

t_LABEL = r'\((?:[A-Za-z0-9]+\s*(?:[A-Za-z0-9]+)?)*\)'
t_ADDRESSES = r'\@[0-9]+'
t_AINSTRUCTION = r'\@(?:[A-Za-z0-9]+)'
t_CINSTRUCTION = r'[A-Za-z0]{1,3}\s{0,2}(?:[=|;])\s{0,2}(?:(?:!|-)?)\s{0,2}(?:[A-Za-z0-9]{1,4})\s{0,2}(?:(?:\||\+|\-|&)?(?:[A-Za-z0-9])?)|;(?:[A-Za-z0-9]{1,3})? '
t_ignore = '\t\r\f\v '  # Ignore whitespace
t_COMMENTS = r'//.*'

lex.lex(debug=0, optimize=False, reflags=re.DOTALL)

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass
    

def t_error(t):
  print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
  t.lexer.skip(1)
  





def parse_source_code(source_code):
  #lex.lex(debug=0, optimize=False, reflags=re.DOTALL)
  lexer = lex.lex()
  lexer.input(source_code)
  labels = []
  Ainstr_Address = []
  Ainst_var =[]
  Cinstruction = []
  N_Cinstruction = {
        "dest": "dest" ,
        "cmp" : "cmp" ,
        "jmp" : "jmp" ,
      }
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
        if  if_address(Ainstruct):
           print(termcolor.colored("Address", "blue"))
           Ainstr_Address.append(tok.value.strip("@"))
        else:
           print(f"the command is {tok.value}")
           Ainst_var.append(tok.value.strip("@"))
    elif tok.type == "CINSTRUCTION":
      print(termcolor.colored("CINSTRUCTION", "magenta"))
      Cinstruction.append(tok.value.strip("\n"))
      print(tok.value)
    elif tok.type == "COMMENTS":
      print(tok.value)
    else:
      continue

  return labels, Ainst_var, Ainstr_Address, Cinstruction
   


with open("ass_test.txt", "r") as F:
  source = F.read()
  


"""
//n=2
@2
D=M
(loop)
AD=D-1
0;jmp
@ali
MD=1
AMD=!D
@moham
MD=A-1
AMD=D&A
MD=D|A
AMD=M-d
@15
D=m+d
MD=-D
D;JGT
@R1     //using a label
d=m
(hello world)
(my name is ali)

"""
#total labels 3, total vars 3, total Ainst_addre 2, Cinstr 13
LAB, VARS, ADDRESSES, CINSTR= parse_source_code(source)
print(LAB)
print(VARS)
print(ADDRESSES)
print(CINSTR)
print(len(CINSTR))