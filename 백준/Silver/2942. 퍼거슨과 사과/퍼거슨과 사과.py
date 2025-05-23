# 백준 2942

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solve(R, G):
    # 최대공약수 구하기
    gcd = GCD(R, G)
    
    # 최대공약수의 약수 구하기
    factors = set()
    i = 1
    while i*i <= gcd:
        if gcd % i == 0:
            factors.add(i)
            factors.add(gcd//i)
        i += 1

    # 조합 저장
    result = []
    for i in list(factors):
        result.append([i, R//i, G//i])

    return result


def main():
    R, G = map(int, input().split())
    for i in solve(R, G):
        print(*i)


main()
