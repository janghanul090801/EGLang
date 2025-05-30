from syntax_tree import *

def parse(tokens):
    tokens = list(tokens)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else (None, None)

    def peek_ahead(n=1):
        if pos + n < len(tokens):
            return tokens[pos + n]
        return (None, None)

    def match(expected):
        nonlocal pos
        if peek()[0] == expected:
            pos += 1
            return True
        return False

    def expect(expected):
        if not match(expected):
            raise SyntaxError(f"Expected {expected}, got {peek()}")

    def expect_token(expected_type):
        nonlocal pos
        token = tokens[pos]
        if token[0] != expected_type:
            raise SyntaxError(f"Expected {expected_type}, got {token}")
        pos += 1
        return token[1]

    # ---------------------- expression parsing ----------------------

    def parse_expr():
        return parse_or()

    def parse_or():
        left = parse_and()
        while peek()[0] == 'OPERATOR' and peek()[1] == '||':
            op = expect_token('OPERATOR')
            right = parse_and()
            left = BinaryOp(left, op, right)
        return left

    def parse_and():
        left = parse_equality()
        while peek()[0] == 'OPERATOR' and peek()[1] == '&&':
            op = expect_token('OPERATOR')
            right = parse_equality()
            left = BinaryOp(left, op, right)
        return left

    def parse_equality():
        left = parse_relational()
        while peek()[0] == 'OPERATOR' and peek()[1] in ('==', '!='):
            op = expect_token('OPERATOR')
            right = parse_relational()
            left = BinaryOp(left, op, right)
        return left

    def parse_relational():
        left = parse_term()
        while peek()[0] == 'OPERATOR' and peek()[1] in ('<', '>', '<=', '>='):
            op = expect_token('OPERATOR')
            right = parse_term()
            left = BinaryOp(left, op, right)
        return left

    def parse_term():
        left = parse_factor()
        while peek()[0] == 'OPERATOR' and peek()[1] in ('+', '-'):
            op = expect_token('OPERATOR')
            right = parse_factor()
            left = BinaryOp(left, op, right)
        return left

    def parse_factor():
        left = parse_atom()
        while peek()[0] == 'OPERATOR' and peek()[1] in ('*', '/'):
            op = expect_token('OPERATOR')
            right = parse_atom()
            left = BinaryOp(left, op, right)
        return left

    def parse_atom():
        token_type, value = peek()
        if token_type == 'NUMBER':
            return Number(expect_token('NUMBER'))
        elif token_type == 'STRING':
            return String(expect_token('STRING'))
        elif token_type == 'IDENT':
            if peek_ahead()[0] == 'DOT':
                return parse_call_or_access_expr(require_semicolon=False)
            return Variable(expect_token('IDENT'))
        elif token_type == 'LAMBDA':
            return parse_lambda_expr()
        else:
            raise SyntaxError(f"Unexpected atom: {peek()}")

    # ---------------------- summon ----------------------

    def parse_summon_expr():
        expect('IMPORT')
        expect('SEMICOLON')
        return ClassExpr("은교햄")

    # ---------------------- lambda ----------------------

    def parse_lambda_expr():
        expect('LAMBDA')  # '임시'

        params = []
        if peek()[0] == 'IDENT':
            while True:
                params.append(expect_token('IDENT'))
                if not match('COMMA'):
                    break

        expect('COLON')

        body = []
        while True:
            if peek()[0] == 'IDENT' and peek_ahead()[0] == 'DOT':
                body.append(parse_call_or_access_expr(require_semicolon=False))
            else:
                body.append(parse_expr())

            if not match('SEMICOLON'):
                break

        return LambdaExpr(params, body)
    
    # --------------------- tukgum ---------------------

    def parse_tukgum_expr():
        expect('TUKGUM')
        expect('SEMICOLON')
        return TukgumExpr()

    # ---------------------- call ----------------------

    def parse_call_or_access_expr(require_semicolon=True):
        class_name = expect_token('IDENT')  # 은교햄
        expect('DOT')
        member_name = expect_token('IDENT')

        if peek()[0] == 'LPAREN':
            # 은교햄.이름(...)
            expect('LPAREN')
            args = []
            while peek()[0] != 'RPAREN':
                if peek()[0] == 'LAMBDA':
                    args.append(parse_lambda_expr())
                else:
                    args.append(parse_expr())
                match('COMMA')
            expect('RPAREN')
            if require_semicolon:
                expect("SEMICOLON")
            return CallExpr(class_name, member_name, args)

        else:
            # 은교햄.이름;
            if require_semicolon:
                expect("SEMICOLON")
            return PropertyAccessExpr(class_name, member_name)


    # ---------------------- main loop ----------------------

    exprs = []
    while peek()[0] is not None:
        if peek()[0] == 'IMPORT':
            exprs.append(parse_summon_expr())
        elif peek()[0] == 'LAMBDA':
            exprs.append(parse_lambda_expr())
        elif peek()[0] == 'TUKGUM':
            exprs.append(parse_tukgum_expr())
        elif peek()[0] == 'IDENT' and peek_ahead()[0] == 'DOT':
            exprs.append(parse_call_or_access_expr())
    return exprs
