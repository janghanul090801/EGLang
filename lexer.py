import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),                 # 숫자 (예: 123)               
    ('LPAREN',   r'\('),                 # (
    ('RPAREN',   r'\)'),  
    ('DOT',      r'\.'),
    ('OPERATOR', r'==|!=|<=|>=|\|\||&&|[+\-*/<>]'),
    ('COMMA',    r','),  
    ('SEMICOLON',r';'),                  # ;
    ('SKIP',     r'[ \t]+'),             # 공백 (무시)
    ('NEWLINE',  r'\n'),                 # 줄바꿈
    ('LAMBDA',   r'임시'),
    ('COLON',     r':'),
    ('STRING',    r'"[^"]*"'),
    ('IMPORT',   r'소환!'),
    ('IDENT',    r'(?!임시|소환!)[가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z_][가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9_]*'),  # 클래스
]

# 정규식 하나로 결합
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)
master_pat = re.compile(token_regex)

def lexer(code):
    tokens = []
    line_num = 1
    for mo in master_pat.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = int(value)
            tokens.append((kind, value))
        elif kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP':
            continue
        else:
            tokens.append((kind, value))
    return tokens
