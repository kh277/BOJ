# 백준 11502

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


from array import array


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


def solve(N, prime):
    for i in range(168):
        for j in range(168):
            for k in range(168):
                if prime[i] + prime[j] + prime[k] == N:
                    return [prime[i], prime[j], prime[k]]
    
    return [-1]


def main():
    T = int(input())

    prime = LinearSieve(1000)
    for _ in range(T):
        N = int(input())
        print(*solve(N, prime))


main()
