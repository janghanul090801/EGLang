class defaultMethod() :
    @staticmethod
    def 만약(con, trueMethod, falseMethod):
        trueMethod() if con else falseMethod()

    @staticmethod
    def 반복(i, goal, incre, method):
        for j in range(i,goal,incre):
            method(j)

    @staticmethod
    def 출력(outputStr):
        print(outputStr)

    @staticmethod
    def 엔터없이출력(outputStr):
        print(outputStr, end="")