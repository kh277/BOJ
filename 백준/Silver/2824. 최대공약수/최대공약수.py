# 백준 2824

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 소인수분해
def primeFactors(N):
    factors = []

    while N % 2 == 0:
        factors.append(2)
        N //= 2

    x = 3
    while x * x <= N:
        while N % x == 0:
            factors.append(x)
            N //= x
        x += 2

    if N > 2:
        factors.append(N)
    
    return factors


def solve(N, M, numA, numB):
    # 각각의 소인수분해 저장
    factorA = dict()
    for i in range(N):
        for j in primeFactors(numA[i]):
            if j in factorA:
                factorA[j] += 1
            else:
                factorA[j] = 1

    factorB = dict()
    for i in range(M):
        for j in primeFactors(numB[i]):
            if j in factorB:
                factorB[j] += 1
            else:
                factorB[j] = 1

    # 소인수 비교
    result = 1
    for i in factorA.keys():
        if i in factorB:
            result *= i**min(factorA[i], factorB[i])

    if result < 10**9:
        return result

    return f"{result % 10**9:09d}"


def main():
    N = int(input())
    numA = list(map(int, input().split()))
    M = int(input())
    numB = list(map(int, input().split()))
    print(solve(N, M, numA, numB))


main()
