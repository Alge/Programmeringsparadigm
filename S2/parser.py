import re
from token import Token

def get_data(filename = "code.lang"):
    code = open(filename, "r").read()
    return code

def remove_comments(code):
    returncode = ""
    delete = False

    for c in code:
        if c == "%":
            delete = True
        elif c == "\n":
            delete = False
        if not delete:
            returncode = returncode + c

    return returncode


def lexer(code):

    regex_rules = [
        ('\d+',     "NUMBER"),
        ('%.*\n',     "COMMENT"),
        ('\n',      "NEWLINE"),
        ('\t',      "TAB"),
        (' ',       "MELLANSLAG"),
        ("\.",      "DOT"),
        ("DOWN",    "DOWN"),
        ("FORW( |\n|\t)",   "FORWARD"),
        ("BACK( |\n|\t)",   "BACK"),
        ("LEFT( |\n|\t)",   "LEFT"),
        ("RIGHT( |\n|\t)",  "RIGHT"),
        ("UP",      "UP"),
        ("REP ",      "REP"),
        ("COLOR( |\n|\t)",      "COLOR"),
        ("#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})",      "HEXCOLOR"),
        ("\"",      "DUBBELFNUTT"),
    ]

    regex_list = []
    for rule in regex_rules:
        regex_list.append( "(?P<{0}>{1})".format(rule[1], rule[0]))

    print(regex_list)

    regex = re.compile("|".join(regex_list))

    print(regex)

    print("starting the lexing")

    token_list = []
    pos = 0

    m = regex.match(code, pos)

    print (m)

    while m:

        t = Token(m.lastgroup, code[m.start():m.end()], m.start())
        print(t)
        token_list.append(t)

        pos = m.end()
        m = regex.match(code, pos)

    if pos < len(code):
        print ("Syntaxfel på rad {}".format(code[:pos].count("\n")+1))

    print(token_list)

lexer(get_data())
