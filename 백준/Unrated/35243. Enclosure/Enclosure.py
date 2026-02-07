# 백준 35243

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 조건을 만족하면서 정x각형의 넓이 구하기
def f(x, m, t):
    S = (t-x*m)**2 / (x*4*math.tan(math.pi/x))
    return S


def solve(m, t):
    start = 3
    end = t//m

    # 삼분 탐색
    while end - start >= 3:
        first = (2*start+end)//3
        second = (start+2*end)//3
        if f(first, m, t) < f(second, m, t):
            start = first+1
        else:
            end = second

    result = 0
    for i in range(start, end+1):
        result = max(f(i, m, t), result)

    return f"{result:.10f}"


def main():
    T = int(input())
    for _ in range(T):
        m, t = map(int, input().split())
        print(solve(m, t))


main()
