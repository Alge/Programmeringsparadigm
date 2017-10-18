class Token:

    def __init__(self, type, value, pos):
        self.type = type
        self.value = value
        self.pos = pos

    def __str__(self):
        return "Token: type = {0}, Value = {1}, Position = {2}".format(self.type, self.value, self.pos)