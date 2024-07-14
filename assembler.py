from source_parser import parse_source_code

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

parse_source_code(source)