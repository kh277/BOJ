# 백준 13705

'''
주의 반례
97084 82977 68488 (소수점 정밀도 예시)
-> 0.384700

27020 1897 56128 (소수점 정밀도 예시)
-> 2.013848

1 1 100000 (시간 초과 예시)
-> 99999.433481

'''


import sys
from decimal import *
import time

input = sys.stdin.readline
PI = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
getcontext().prec = 150     # 소수점 정확도 설정
getcontext().rounding = ROUND_HALF_UP   # 반올림 방법 설정
TAYLOR_REPEAT_COUNT = 50    # 테일러 급수를 계산할 항 수 설정


# 팩토리얼 계산 함수
def factorial(n):
    result = [1 for _ in range(n+1)]

    for i in range(1, n+1):
        result[i] = result[i-1] * i
    
    return result[n]


# f(x) = 0의 함수값 계산
def f(x):
    return A*x + B*sin(x) - C


# f'(x) = 0의 함수값 계산
def df(x):
    return A + B*cos(x)


# 테일러 급수를 이용하여 sin(x) = 0의 함수값 계산
def sin(x, n=TAYLOR_REPEAT_COUNT):
    x = Decimal(str(x))

    # x값이 너무 클 경우 삼각함수의 주기성을 이용해서 줄여줌
    x = x % (2 * PI)

    result = Decimal(0)

    for i in range(n):
        sign = Decimal(-1) ** i
        result += sign * (x ** (2 * i + 1)) / Decimal(str(factorial(2 * i + 1)))
        
    return result


# 테일러 급수를 이용하여 cos(x) = 0의 함수값 계산
def cos(x, n=TAYLOR_REPEAT_COUNT):
    x = Decimal(str(x))

    # x값이 너무 클 경우 삼각함수의 주기성을 이용해서 줄여줌
    x = x % (2 * PI)

    result = Decimal(0)

    for i in range(n):
        sign = Decimal(-1) ** i
        result += sign * (x ** (2 * i)) / Decimal(str(factorial(2 * i)))

    return result


# 뉴턴-랩슨 방법을 통해 f(x) = 0의 해 구하기
def newton_raphson(x0, epsilon, max_iter):
    # 초기값 및 Decimal 자료형 수정
    x = Decimal(C) / Decimal(A)
    epsilon = Decimal(epsilon)
    
    # x_next와 x의 차이가 epsilon 미만이 될 때까지 반복
    for i in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < epsilon:
            break
        x = Decimal(str(x_next))
    
    # 소수 일곱째 자리에서 반올림   
    return Decimal(str(x_next)).quantize(Decimal('10e-6'), rounding=ROUND_HALF_UP)


def main():
    global A, B, C
    A, B, C = list(map(Decimal, input().split()))
    
    print(newton_raphson('1', '10e-50', 2000))


main()
