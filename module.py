def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def ifib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        return a

import fibonacci #모듈 생성한거 import
print(fibonacci.fib(7))

#import reload
#reload(fibonacci) #모듈 수정시

#del fibonacci 모듈 삭제

'''
패키지 모듈 만들기
1. 패키지 모듈을 만들 디렉토리 생성
2. cmd에서 set PYTHONPATH='디렉토리 경로' 추가
3. python입력
4. package 안에는 __init__.py가 있어야함
from SimplePackage import a,b
simplepackage만 가져오는 경우 모듈 a 및 b에는 액세스 할 수 없음

'''
from SimplePackage import a, b