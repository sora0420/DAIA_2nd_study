class Greeting:
    def __init__(self, name):
        self.name = name
        print("Hi"+ " "+str(name))

    def __del__(self):
        print("Destructor started")

    def SayHello(self):
        print(("Hello")+ " " + str(self.name))

x1 = Greeting("a")
x2 = x1

x3 = Greeting("b")
x4 = x3
x4.SayHello()

del x1 #클래스 인스턴스 x1을 삭제할 때 소멸자 호출 x
del x2 #>>del 명령이 x1객체에 대한 참조 카운트를 1만큼 감소시킴
del x4 #참조횟수가 0이되면 __del__ 메소드 호출
