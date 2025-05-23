class defaultMethod() :
    @staticmethod
    def 만약(con, trueMethod, falseMethod):
        return trueMethod() if con else falseMethod()

    @staticmethod
    def 반복(i, goal, incre, method):
        for j in range(i,goal,incre):
            method(j)

    @staticmethod
    def 출력(outputStr):
        if callable(outputStr):
            print(outputStr())
        else :
            print(outputStr)

    @staticmethod
    def 엔터없이출력(outputStr):
        if callable(outputStr):
            print(outputStr(), end="")
        else :
            print(outputStr, end="")

    @staticmethod
    def 삽입(var_name:list, value):
        var_name.append(value)

    @staticmethod
    def 인덱싱(var:list, index:int):
        return var.index(index)