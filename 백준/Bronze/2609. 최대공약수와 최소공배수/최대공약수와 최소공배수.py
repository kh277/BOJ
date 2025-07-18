# 백준 2609

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    A, B = map(int, input().split())
    print(gcd(A, B))
    print(lcm(A, B))


main()
