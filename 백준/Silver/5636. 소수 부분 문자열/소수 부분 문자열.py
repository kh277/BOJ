# 백준 5636

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def sieve(N):
    sieve = array('i', [0]) * N
    primes = array('i')

    for i in range(2, N):
        if sieve[i] == 0:
            primes.append(i)
        
        for j in primes:
            if i*j >= N:
                break
            sieve[i*j] = 1
            if i % j == 0:
                break

    return primes


def solve(N):
    result = -1
    for i in range(0, len(N)-1):
        for j in range(i+1, len(N)):
            if j-i > 6:
                break
            cur = int(N[i:j])
            if cur in primes:
                result = max(result, cur)

    return result


def main():
    global primes
    primes = sieve(100000)
    while True:
        N = input().decode().rstrip()
        if N == '0':
            break
        print(solve(N))


main()
