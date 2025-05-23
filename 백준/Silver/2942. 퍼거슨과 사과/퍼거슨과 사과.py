# 백준 2942

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve(R, G):
    gcd = GCD(R, G)
    
    factors = []
    for i in range(1, gcd+1):
        if gcd % i == 0:
            factors.append(i)

    result = []
    for i in factors:
        result.append([i, R//i, G//i])
    
    return result


def main():
    R, G = map(int, input().split())
    for i in solve(R, G):
        print(*i)


main()
