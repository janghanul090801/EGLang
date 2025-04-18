from syntax_tree import *
from defaultMethods import defaultMethod as df

class Interpreter:
    def __init__(self):
        self.env = {}

    def summonEungyoHam(self):
        self.classes = {
            "은교햄": {
                "만약": lambda con, trueMethod, falseMethod: df.만약(con, trueMethod, falseMethod),
                "반복": lambda i, con, incre, method: df.반복(i, con, incre, method),
                "출력": lambda outputStr='': df.출력(outputStr),
                "엔터없이출력": lambda outputStr='': df.엔터없이출력(outputStr),
                "변수": lambda name, value: self.create_variable(name, value),
            }
        }

    def wrap_lambda(self, node, outer_env):
        def wrapped_func(*args):
            local_env = outer_env.copy()
            param_bindings = dict(zip(node.params, args))
            local_env.update(param_bindings)
            result = None
            for expr in node.body:
                result = self.eval(expr, local_env)
            return result
        return wrapped_func

    def create_variable(self, var_name_node, value_node):
        if isinstance(var_name_node, Variable):
            var_name = var_name_node.name
        elif isinstance(var_name_node, String):
            var_name = var_name_node.value.strip('"')
        else:
            raise TypeError("변수 이름은 식별자 또는 문자열이어야 합니다.")
        
        
        self.env[var_name] = value_node

    def eval(self, node, env=None):
        if env is None:
            env = self.env
        if isinstance(node, CallExpr):
            cls = self.classes.get(node.class_name)
            if cls is None:
                raise Exception(f"Unknown class: {node.class_name}")
            method = cls.get(node.method_name)
            if method is None:
                raise Exception(f"Unknown method: {node.method_name}")
            
            if node.method_name == "변수":
                return self.create_variable(node.args[0], self.eval(node.args[1], env))
            # 여기 수정: env 넘기기
            arg_vals = [self.eval(arg, env) for arg in node.args]
            return method(*arg_vals)
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value.strip('"')
        elif isinstance(node, LambdaExpr):
            return self.wrap_lambda(node, env)
        elif isinstance(node, ClassExpr):
            self.summonEungyoHam()
        elif isinstance(node, Variable):
            if node.name in env:
                return env[node.name]
            else:
                raise NameError(f"변수 '{node.name}'를 찾을 수 없습니다.")
        elif isinstance(node, BinaryOp):
            left = self.eval(node.left, env)
            right = self.eval(node.right, env)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
            elif node.op == '<':
                return left < right
            elif node.op == '>':
                return left > right
            elif node.op == '==':
                return left == right
            elif node.op == '!=':
                return left != right
            elif node.op == '<=':
                return left <= right
            elif node.op == '>=':
                return left >= right
            elif node.op == '||':
                return left or right
            elif node.op == '&&':
                return left and right
            else:
                raise ValueError(f"Unknown operator: {node.op}")