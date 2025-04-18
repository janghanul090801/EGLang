# python main.py hello.egl

import sys
from lexer import *
from parser import *
from Interpreter import *
from syntax_tree import *

def run_eungyoham_script(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    tokens = lexer(code)
    asts = parse(tokens)
    interpreter = Interpreter()
    for ast in asts:
        interpreter.eval(ast)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python main.py 파일명.egl")
    else:
        run_eungyoham_script(sys.argv[1])
