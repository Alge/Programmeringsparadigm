class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

    class node:
        def __init__(self, token, parent = None):
            self.token = token
            self.right = None
            self.left = None
            self.parent = parent


    def parse(self):
        t = self.lexer.next_token()

        while t != None:
            print(t)
            t = self.lexer.next_token()
