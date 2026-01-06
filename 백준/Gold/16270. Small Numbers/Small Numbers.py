# 백준 16270

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# N 이하의 소수 전부 반환
def LinearSieve(N):
    sieve = array('I', [0]) * (N+1)
    prime = array('I')

    for i in range(2, N+1):
        # 소수 추가
        if sieve[i] == 0:
            prime.append(i)
            sieve[i] = i

        # 합성수 제거
        for j in range(len(prime)):
            if i * prime[j] > N:
                break
            sieve[i * prime[j]] = prime[j]
            if i % prime[j] == 0:
                break

    return prime


# N을 소인수분해 하여 개수가 홀수인 소인수 반환
def factorize(prime, N):
    result = []

    for i in prime:
        if i*i > N:
            break
        if N % i == 0:
            count = 0
            while N % i == 0:
                N //= i
                count ^= 1
            if count == 1:
                result.append(i)

    if N > 1:
        result.append(N)

    return result


# arr에서 두 부분으로 나누어 합이 최소가 되도록 만들기
def getMin(arr, index, left, right):
    if index == len(arr):
        return [left+right, left, right]

    aL = left*arr[index]
    bR = right*arr[index]
    a = getMin(arr, index+1, aL, right)
    b = getMin(arr, index+1, left, bR)

    if a[0] < b[0]:
        return a
    return b


def solve(A, B, prime):
    # A, B 소인수분해
    factA = factorize(prime, A)
    factB = factorize(prime, B)

    # A와 B의 인수 XOR 처리
    left = list(set(factA) ^ set(factB))

    # 합이 최소가 되도록 둘로 나누기
    return getMin(left, 0, 1, 1)[1:]


def main():
    # 소수 체 전처리
    prime = LinearSieve(31623)

    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(*solve(A, B, prime))


main()
