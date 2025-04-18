from defaultMethods import defaultMethod as df

class 은교햄:
    def 만약(self, con, trueMethod, falseMethod):
        return df.만약(con, trueMethod, falseMethod)

    def 반복(self, i, con, incre, method):
        return df.반복(i, con, incre, method)

    def 출력(self, outputStr=''):
        return df.출력(outputStr)

    def 엔터없이출력(self, outputStr=''):
        return df.엔터없이출력(outputStr)

    def 변수(self, name, value):
        return self.create_variable(name, value)  # 이건 바깥에서 inject 해줘야 함
    
    def __str__(self):
        return ""
    
    def __eq__(self, value):
        return value == "신"
    
    def __lt__(self, other):
        return 0
    
    def __le__(self, other):
        if other == self:
            return 1
        else:
            return 0
        
    def __gt__(self, other):
        return 1
    
    def __ge__(self, other):
        return 1
