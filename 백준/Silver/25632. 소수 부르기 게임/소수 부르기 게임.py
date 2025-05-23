# 백준 25632

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def LinearSieve(N):
    composite = [True for _ in range(N+1)]
    prime = []

    for i in range(2, N+1):
        if composite[i] == True:
            prime.append(i)

        for j in range(len(prime)):
            if i * prime[j] > N:
                break
            composite[i * prime[j]] = False
            if i % prime[j] == 0:
                break

    return prime


def solve(A, B, C, D):
    primeA = set()
    primeB = set()
    prime = LinearSieve(max(B, D))
    for i in range(len(prime)):
        if A <= prime[i] <= B:
            primeA.add(prime[i])
        if C <= prime[i] <= D:
            primeB.add(prime[i])

    # 각 사람이 부를 수 있는 소수 개수 도출 (yt = 0, yj = 1)
    start = 0
    lenBoth = len(primeA & primeB)
    lenA = len(primeA) - lenBoth
    lenB = len(primeB) - lenBoth
    if lenBoth % 2 == 1:
        start = 1

    if lenA > lenB:
        return 'yt'
    elif lenA < lenB:
        return 'yj'
    else:
        return ['yj', 'yt'][start]


def main():
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(solve(A, B, C, D))


main()
