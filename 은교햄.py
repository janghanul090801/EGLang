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

    def 변수(self, name, values):
        return self.create_variable(name, values)  # 이건 바깥에서 inject 해줘야 함
    
    def 리스트(self, *values):
        return list(values)
    
    def 함수(self, func_name, func):
        return self.create_function(func_name, func)
    
    def 삽입(self, var_name : list, value):
        return df.삽입(var_name, value)
    
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
