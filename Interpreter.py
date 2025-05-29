from syntax_tree import *
from 은교햄 import *

class Interpreter:
    def __init__(self):
        self.global_env = {}
        self.env_stack = [self.global_env]  # 환경 스택
        self.classes = {}

    def current_env(self):
        return self.env_stack[-1]

    def summonEungyoHam(self):
        self.은교햄_instance = 은교햄()
        self.은교햄_instance.create_variable = self.create_variable  # 외부 메서드 주입

        self.classes = {
            "은교햄": self.은교햄_instance
        }

    def iscallable_and_return(self, left, right):
        if callable(left):
            left = left()
        if callable(right):
            right = right()
        return left, right

    def wrap_lambda(self, node, outer_env):
        def wrapped_func(*args):
            local_env = dict(zip(node.params, args))
            self.env_stack.append(local_env)  # 지역 스코프 진입
            result = None
            for expr in node.body:
                result = self.eval(expr)
            self.env_stack.pop()  # 지역 스코프 탈출
            return result
        return wrapped_func

    def create_variable(self, var_name_node, *value_node_list):
        if len(value_node_list) == 1:
            if isinstance(var_name_node, Variable):
                var_name = var_name_node.name
            elif isinstance(var_name_node, String):
                var_name = var_name_node.value.strip('"')
            else:
                raise TypeError("변수 이름은 식별자 또는 문자열이어야 합니다.")
        
            self.classes["은교햄"].var_list[var_name] = value_node_list[0]
        else:
            var_list = []
            for value_node in value_node_list:
                if isinstance(var_name_node, Variable):
                    var_name = var_name_node.name
                    var_list.append(value_node)
                elif isinstance(var_name_node, String):
                    var_name = var_name_node.value.strip('"')
                    var_list.append(value_node)
                else:
                    raise TypeError("변수 이름은 식별자 또는 문자열이어야 합니다.")
            
            
                self.classes["은교햄"].var_list[var_name] = var_list

    def create_function(self, func_name, func):
        setattr(self.은교햄_instance, func_name, func)

    def eval(self, node):
        env = self.current_env()
            
        if isinstance(node, CallExpr):
            cls = self.classes.get(node.class_name)
            if cls is None:
                raise Exception(f"Unknown class: {node.class_name}")
            cls = self.classes["은교햄"]
            method = cls.var_list[node.method_name]        # 이거 수정 필요 -> 변수에서 가져와야되는데 씨발 어케하지
            if method is None:
                raise Exception(f"Unknown method: {node.method_name}")
            
            if node.method_name == "변수":
                evaled_args = [self.eval(arg) for arg in node.args[1:]]
                return self.create_variable(node.args[0], *evaled_args)
            # elif node.method_name == '함수':
            #     return self.create_function(self.eval(node.args[0], env), self.wrap_lambda(node.args[1], env))
            # 여기 수정: env 넘기기
            arg_vals = [self.eval(arg) for arg in node.args]
            return method(*arg_vals)
        elif isinstance(node, PropertyAccessExpr):
            return self.classes["은교햄"].var_list[node.property_name]
        elif isinstance(node, Number):
            return node.value
        elif isinstance(node, String):
            return node.value.strip('"')
        elif isinstance(node, LambdaExpr):
            return self.wrap_lambda(node, env)
        elif isinstance(node, ClassExpr):
            self.summonEungyoHam()
        elif isinstance(node, Variable):
            for env in reversed(self.env_stack):  # 가장 가까운 스코프부터 확인
                if node.name in env:
                    return env[node.name]
            if node.name in self.classes:
                return self.classes[node.name]
            raise NameError(f"변수 '{node.name}'를 찾을 수 없습니다.")
        elif isinstance(node, BinaryOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            left, right = self.iscallable_and_return(left, right)
            if isinstance(left, str) or isinstance(right, str):
                left = str(left)
                right = str(right)
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
            
        elif isinstance(node, TukgumExpr):
            del self.classes["은교햄"]
        