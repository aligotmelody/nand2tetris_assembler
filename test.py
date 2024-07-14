from ply import lex



tokens = (
  "LABEL",
  "Variabels",
  "Addresses",
  "Cinstruction",
  "Ainstruction",
  "COMMENTS"
)

t_LABEL = r'\([A-Za-z0-9]+\)'
t_Variabels = r'[A-Za-z]+(?:[A-Za-z0-9]+)?'
t_Addresses = r'[0-9]+'
t_Ainstruction = r'\@[A-Za-z0-9]+'
t_Cinstruction = r'(?:(?:[ADM]{1,3})=)?(?:[-!]?[01ADM]+[+\-&|]?[-!]?[01ADM]*)(?:;[A-Z]{3})? '
#                  [A-Za-z]{1,4}\s*=\s*(?:(?:!|-)?([A-Za-z0-9])?)?
#                  [A-Za-z]{1,4}\s*=\s*(?:(?:!|-)?(?:[A-Za-z0-9]|\(.*?\))?)*
#|;(?:[A-Za-z0-9]{1,4})?|[A-Za-z]\s*(?:[&\|\+\-])\s*[A-Za-z0-9]'
t_ignore = '\t\r\n\f\v '  # Ignore whitespace

t_COMMENTS = r'//.*'
def t_error(t):
  print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
  t.lexer.skip(1)



def parse_source_code(source_code):
  lexer = lex.lex()
  lexer.input(source_code)
  labels = []
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
    elif tok.type == "Ainstruction":
      print(tok.value)
    elif tok.type == "Cinstruction":
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

"""

print(parse_source_code(source))