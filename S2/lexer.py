import re
from token import Token
class Lexer:

    def __init__(self):

        self.token_list = []
        self.token_index = 0

        self.regex_rules = [
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

        for rule in self.regex_rules:
            regex_list.append( "(?P<{0}>{1})".format(rule[1], rule[0]))

        self.regex = re.compile("|".join(regex_list))

    def lex(self, code):
        pos = 0


        m = self.regex.match(code, pos)

        print (m)

        while m:

            t = Token(m.lastgroup, code[m.start():m.end()], m.start())
            print(t)
            self.token_list.append(t)

            pos = m.end()
            m = self.regex.match(code, pos)

        if pos < len(code):
            print ("Syntaxfel på rad {}".format(code[:pos].count("\n")+1))


    def next_token(self):
        if self.token_index >= len(self.token_list):
            return None
        t =  self.token_list[self.token_index]
        self.token_index += 1
        return t