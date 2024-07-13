from ply import lex

tokens = (
  "LABEL",
  "Variabels",
  "Comments",
  "Ainstruction",
  "Cinstruction",
)

t_LABEL = r"\([A-Za-z0-9]+\):"
t_Ainstruction = r"\@[A-Za-z0-9]+"
t_Cinstruction = r"\@([A-Za-z0-9]+|\||&|\+|;|=[A-Za-z0-9])"
t_Variabels = r"[A-Za-z]+"
t_Comments = r"//.*"
t_ignore = " \t\n"  # Ignore whitespace

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
  while True:
    tok = lexer.token()
    if not tok:
      
      break
    if tok.type == "LABEL":
      labels.append(tok.value[1:-1])  # Remove Parenthesis from label
      print(tok)
    elif tok.type == "Ainstruction":
      Ainstruction.append(tok.value.strip("@"))
    elif tok.type == "Cinstruction":
      Cinst_dest_rest = (tok.value.split("="))
      print(Cinst_dest_rest)
      Cinst_cm_jm = Cinst_dest_rest.split(";")
      dest = Cinst_dest_rest[0]
      cmp  = Cinst_cm_jm[0]
      jmp  = Cinst_cm_jm[1]
      N_Cinstruction = {
        "dest": dest ,
        "cmp" : cmp ,
        "jmp" : jmp ,
      }
      Cinstruction.update(N_Cinstruction)



  return labels, Ainstruction, Cinstruction

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