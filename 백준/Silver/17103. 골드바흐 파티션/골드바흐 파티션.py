# 백준 4281

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

    return sieve, prime


def solve(N, sieve, prime):
    result = 0
    for i in range(len(prime)):
        cur = N - prime[i]
        if prime[i] > cur:
            break
        
        if sieve[cur] == cur:
            result += 1
    
    return result


def main():
    T = int(input())
    sieve, prime = LinearSieve(1000000)
    for _ in range(T):
        N = int(input())
        print(solve(N, sieve, prime))


main()
