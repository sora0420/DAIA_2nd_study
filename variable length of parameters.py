def arithmetic_mean(first, *values): #튜플 참조/ 두번째부터 들어온 인수 갯수를 모를 때 사용
    return (first+sum(values)) / (1+len(values))

print(arithmetic_mean(45, 32, 89, 78))
print(arithmetic_mean(8989, 8, 78.5, 53.2))
x = [3,5,9]
#print(arithmetic_mean(x)) #list 데이터는 처리할 수 없음
print(arithmetic_mean(*x)) #list의 길이를 사전에 알아야 하기 때문에 변수앞에 *추가
#튜플참조 방법으로 임의의 매개변수 숫자를 확인할 수 있음

my_list = [('a',232),('b',343),('c',543),('d',23)]
print(my_list)#[('a', 232), ('b', 343), ('c', 543), ('d', 23)]
print(list(zip(*my_list)))#[('a', 'b', 'c', 'd'), (232, 343, 543, 23)]

test_list = [(1,232),(2,343),(3,543),(4,23)]
print(test_list) #[(1, 232), (2, 343), (3, 543), (4, 23)]
print(list(zip(*test_list))) #[(1, 2, 3, 4), (232, 343, 543, 23)]

def f(**kwargs): # **kwargs는 딕셔너리 형태로 입력되는 것
    print(kwargs)
f()
f(de="German", en="English", fr="French")
{'fr':'French', 'de':'German', 'en':'English'}

def a(*args): #*args는 값을 넣으면 함수에 변수가 튜플형태로 입력되는 것
    print(args)
a()
a(1,2,3,4)

