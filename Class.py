class Calc:
    classLog = []  # 클래스변수

    def __init__(self, id):
        print("계산기를 시작합니다~ 아이디는" + str(id) + "입니다~")
        self.classLog = []  # 객체 변수
        self.classLog.append(id)
        Calc.classLog.append(id)

    def add(self, op1, op2):
        print(op1 + op2)
        self.classLog.append(str(op1) + "+" + str(op2))

    def mul(self, op1, op2):
        print(op1 * op2)
        self.classLog.append(str(op1) + "*" + str(op2))

    def div(self, op1, op2):
        if (op2 == 0):
            print("0으로 나눌 수 없습니다.")
            return -1

        print(op1 / op2)
        self.classLog.append(str(op1) + "/" + str(op2))

    def printLog(self):
        print(self.classLog)


calc1 = Calc(1)
calc2 = Calc(2)

calc1.add(1, 2)
calc1.mul(3, 4)
calc2.mul(5, 6)
calc2.div(2, 0)

calc1.printLog()
calc2.printLog()
