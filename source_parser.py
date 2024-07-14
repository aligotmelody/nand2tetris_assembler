from ply import lex




tokens = (
  "LABEL",
  "VARIABLES",
  "ADDRESSES",
  "CINSTRUCTION",
  "AINSTRUCTION",
  "COMMENTS"
)

t_LABEL = r'\([A-Za-z0-9]+\)'
t_VARIABLES = r'\@[A-Za-z]+(?:[A-Za-z0-9]+)?'
t_ADDRESSES = r'\@[0-9]+'
t_AINSTRUCTION = r'\@[A-Za-z0-9]+'
t_CINSTRUCTION = r'[A-Za-z0-9]{1,4}\s*(?:[=|;])\s*(?:(?:!|-)?(?:[A-Za-z0-9]+))?\s*(?:(?:\||\+|-)?(?:[A-Za-z0-9])?)|;(?:[A-Za-z0-9]{1,4})? '
t_ignore = '\t\r\n\f\v '  # Ignore whitespace

t_COMMENTS = r'//.*'
def t_error(t):
  print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
  t.lexer.skip(1)



def parse_source_code(source_code):
  lexer = lex.lex()
  lexer.input(source_code)
  labels = []
  Vars = []
  Addresses = []
  Ainstruction =[]
  Cinstruction ={
    "dest": "" ,
    "cmp" : "" ,
    "jmp" : "" ,
  }
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
        print(tok.value)
        #if  tok.type == "VARIABLES":
         # print(termcolor.colored("var", "blue"))
          #Vars.append(tok.value.strip("@"))
        #elif tok.type == "ADDRESSES":
         # print(termcolor.colored("ADDRESSES", "red"))
          #Addresses.append(tok.value.strip("@"))
        #else:
         # print(f"there's something wrong with this character {tok.value}")

    elif tok.type == "CINSTRUCTION":
     # print(termcolor.colored("CINSTRUCTION", "magenta"))
      print(tok.value)
    elif tok.type == "COMMENTS":
      print(tok.value)
    else:
      continue

source = """
//n=2
@2
D=M
(loop)
AD=D-1
0;jmp
@ali
"""



labels, Ainstruction, Cinstruction = parse_source_code(source)
print(labels)
print(Ainstruction)
print(Cinstruction)