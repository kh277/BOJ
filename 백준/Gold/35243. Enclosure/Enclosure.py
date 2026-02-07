# 백준 35243

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 조건을 만족하면서 정x각형의 넓이 구하기
def f(x, m, t):
    S = (t-x*m)**2 / (x*4*math.tan(math.pi/x))
    return S


def solve(m, t):
    result = 0
    for i in range(3, t//m+1):
        cur = f(i, m, t)
        if cur > result:
            result = cur
        else:
            break

    return f"{result:.10f}"


def main():
    T = int(input())
    for _ in range(T):
        m, t = map(int, input().split())
        print(solve(m, t))


main()
