from lexer import Lexer

def get_data(filename = "samples/si1.txt"):
    code = open(filename, "r").read()
    return code


l = Lexer()

l.lex(get_data())

l.clean()

t = l.next_token()

while t != None:
    print(t)
    t = l.next_token()