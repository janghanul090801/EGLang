class ASTNode:
    pass

class CallExpr(ASTNode):
    def __init__(self, class_name, method_name, args):
        self.class_name = class_name
        self.method_name = method_name
        self.args = args

class Number(ASTNode):
    def __init__(self, value):
        self.value = int(value)

    def __repr__(self):
        return f"Number({self.value})"
    
class String(ASTNode):
    def __init__(self, value):
        self.value = value.strip('"') 

    def __repr__(self):
        return f'String("{self.value}")'
    
class Variable:
    def __init__(self, name):
        self.name = name

class LambdaExpr:
    def __init__(self, params, body):
        self.params = params
        self.body = body
    def __repr__(self):
        return f"LambdaExpr({self.params}, {self.body})"

class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left    # 좌측 표현식 (예: Variable, Number 등)
        self.op = op        # 연산자 문자열 (예: '+', '-', '*', '/')
        self.right = right  # 우측 표현식

    def __repr__(self):
        return f"BinaryOp({self.left}, '{self.op}', {self.right})"

class ClassExpr:
    def __init__(self, class_name):
        self.class_name = class_name

class ReturnExpr(ASTNode):
    def __init__(self, value):
        self.value = value

class TukgumExpr:
    pass