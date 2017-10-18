from lexer import Lexer
from parser import Parser

def get_data(filename = "samples/si1.txt"):
    code = open(filename, "r").read()
    return code


l = Lexer()

l.lex(get_data())

p = Parser(l)

p.parse()
