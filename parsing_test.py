from ply import lex
import termcolor
import re



dest_dict = {
    'null': '000', 'M': '001', 'D': '010', 'MD': '011',
    'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'
}



comp_dict = {
   
   '0': '0101010', '1': '0111111', '-1':'0111010', 'D':'0001100', 'A': '0110000', '!D': '0001101',
    '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111',
    'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011', 'A-D':'0000111',
    'D&A': '0000000', 'D|A': '0010101', 'M': '1110000', '!M': '1110001', '-M': '1110011',
    'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
    'D&M': '1000000', 'D|M': '1010101'
            
            }



jmp_dict = {
    'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
    'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'
}



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
t_CINSTRUCTION = r'(?:[ADM]{1,3}=)?(?:[!ADM]{1})?[\-+&|]{0,1}[01ADM]{1}(?:;J\w+)? '
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
  lex.lex(debug=0, optimize=False, reflags=re.DOTALL)
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
      Cinstruction.
      print(tok.value)
    elif tok.type == "COMMENTS":
      print(tok.value)
    else:
      continue

  return labels, Ainst_var, Ainstr_Address, Cinstruction
   

def assem_2_binary():

with open("ass_test.txt", "r") as F:
   source_code = F.read()



"""
//n=2
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
@R1     //using a label
D=M
(example description to the test with)
"""



  



#total labels 3, total vars 3, total Ainst_addre 2, Cinstr 13
LAB, VARS, ADDRESSES, CINSTR = parse_source_code(source_code)
print(LAB)

print(ADDRESSES)
print(len(ADDRESSES))

print(len(CINSTR))



