# 백준 4406

'''
시작 좌표: (a/2, b/2)
도착 좌표: (ma, nb)
위 내용을 기반으로 기울기와 속도를 구하면 된다.
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(a, b, s, m, n):
    if m*a - a == 0:
        slope = 1
    slope = math.atan((n*b)/(m*a))*180/math.pi
    speed = ((m*m*a*a + n*n*b*b)/(s*s))**0.5
    return (f"{slope:.2f} {speed:.2f}")


def main():
    while True:
        a, b, s, m, n = map(int, input().split())
        if a == 0 and b == 0 and s == 0:
            break
        print(solve(a, b, s, m, n))


main()
