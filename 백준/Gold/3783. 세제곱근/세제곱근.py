# 백준 3783

'''
뉴턴-랩슨 방법으로 y = x^3의 해를 구하면 된다.

주의 반례
3
0
1
989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898
999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
->
0
1.0000000000
99662159587181066183986038468999178232540866499854.8082441923
99999999999999999999999999999999999999999999999999.9999999999
'''

import sys
from decimal import *
import math

input = sys.stdin.readline
getcontext().prec = 300    # 소수점 정확도 설정


# 소수점 10자리 버림 계산
def truncate(number, n=10):
    factor = Decimal('10') ** n

    return Decimal(str(math.floor(number * factor))) / factor


# f(x) = 0의 함수값 계산
def f(x):
    return x**3 - A


# f'(x) = 0의 함수값 계산
def df(x):
    return 3*x**2


# 뉴턴-랩슨 방법을 통해 f(x) = 0의 해 구하기
def newton_raphson(epsilon, max_iter):
    # 예외 처리
    if A == 0:
        return 0

    # 초기값 설정 및 Decimal 자료형 수정
    x = Decimal(A)
    epsilon = Decimal(epsilon)
    
    # x_next와 x의 차이가 epsilon 미만이 될 때까지 반복
    for i in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < epsilon:
            break
        x = Decimal(str(x_next))
    
    # 소수점 250번째 자리에서 반올림 후 10번째 자리에서 절삭
    x = Decimal(str(x_next)).quantize(Decimal('10e-250'), rounding=ROUND_HALF_UP)
    return "{:.10f}".format(truncate(x, 10))


def main():
    T = int(input())
    for _ in range(T):
        global A
        A = int(input())

        print(newton_raphson('10e-300', 5000))


main()