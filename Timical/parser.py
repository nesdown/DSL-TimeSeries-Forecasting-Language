from rply import ParserGenerator
from ast import Number, Sum, Sub, Print
from interpreter import Interpreter


class Parser():
    def __init__(self):
        self.sp = Interpreter()

        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            [
                'STRING', 
                'NUMBER', 
                'VARIABLE_FILE',
                'VARIABLE_VECTOR',
                'VECTOR',
                'OPEN_SQUARE_PAREN',
                'CLOSE_SQUARE_PAREN',
                'FILE', 
                'TIME_STAMP', 
                'VECTOR', 
                'ERROR',
                'PRINT', 
                'OPEN_PAREN', 
                'CLOSE_PAREN',
                'SEMI_COLON', 
                'EQUAL',
                'SUM', 
                'SUB'
            ]
        )

    def parse(self):
        # command for processing the files all together
        @self.pg.production('program : VARIABLE_FILE EQUAL FILE OPEN_PAREN STRING CLOSE_PAREN SEMI_COLON')
        def program(p):
            return self.sp.File_Open(p[0], p[4])

        @self.pg.production('program : VARIABLE_VECTOR EQUAL VECTOR OPEN_SQUARE_PAREN STRING CLOSE_SQUARE_PAREN SEMI_COLON')
        def program(p):
            return self.sp.Vector_Init(p[0], p[3])

        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()