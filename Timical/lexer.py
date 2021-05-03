from rply import LexerGenerator

class Lexer ():
    def __init__(self):
        super().__init__()
        self.lexer = LexerGenerator()

    def _add_tokens (self):
        # FILE 
        self.lexer.add('FILE', r'fileinitializer')

        # VARIABLE FILE
        self.lexer.add('VARIABLE_FILE', r'[w]\d+')

        # VARIABLE VECTOR
        # TODO: change v1 and f1 to varV1 and varF1
        self.lexer.add('VARIABLE_VECTOR', r'[v]\d+')

        # TIME STAMP
        self.lexer.add('TIME_STAMP', r'timestamp')

        # VECTOR
        self.lexer.add('VECTOR', r'vector')

        # ERROR
        self.lexer.add('ERROR', r'error')

        # 2D CHART
        self.lexer.add('2D_CHART', r'2dchart')

        # PRINT
        self.lexer.add('PRINT', r'print')

        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        self.lexer.add('OPEN_SQUARE_PAREN', r'\[')
        self.lexer.add('CLOSE_SQUARE_PAREN', r'\]')

        # Equal
        self.lexer.add('EQUAL', r'\=')

        # Semi-colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Text string with any symbol in it
        self.lexer.add('STRING', r'".+"')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
