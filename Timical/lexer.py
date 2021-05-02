from rply import LexerGenerator

class Lexer ():
    def __init__(self):
        super().__init__()
        self.lexer = LexerGenerator()

    def _add_tokens (self):
        # PRINT
        self.lexer.add('PRINT', r'print')
        #Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        #Semi colon
        self.lexer.add('SEMI_COLON', r'\;')
        #Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        #Number
        self.lexer.add('NUMBER', r'\d+')
        #Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
