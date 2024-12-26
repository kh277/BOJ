# 백준 28570


import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve():
    common = gcd(N, M)
    return str(N//common)+'/'+str(M//common)


# main 함수 ----------
N, M = map(int, input().split())
print(solve())

