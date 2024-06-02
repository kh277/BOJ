# 백준 14786

import sys
import math

input = sys.stdin.readline


# 뉴턴-랩슨 방법을 통해 f(x) = 0의 해 구하기
def newton_raphson(x0, epsilon):
    # 초기값
    x = x0
    
    # x_next와 x의 차이가 epsilon 미만이 될 때까지 반복
    while True:
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < epsilon:
            return x_next
        x = x_next
        
    return x


def f(x):
    return A*x + B*math.sin(x) - C


def df(x):
    return A + B*math.cos(x)


def main():
    global A, B, C
    A, B, C = list(map(int, input().split()))
    
    print(newton_raphson(1, 10e-10))


main()
