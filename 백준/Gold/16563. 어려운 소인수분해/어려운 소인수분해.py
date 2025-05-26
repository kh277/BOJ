# 백준 16563

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def LinearSieve(N):
    spf = array('I', [0]) * (N+1)
    prime = array('I')

    for i in range(2, N):
        # 소수 추가
        if spf[i] == 0:
            prime.append(i)
            spf[i] = i

        # 합성수 제거
        for j in range(len(prime)):
            if i * prime[j] > N:
                break
            spf[i * prime[j]] = prime[j]
            if i % prime[j] == 0:
                break

    return spf


def solve(spf, num):
    result = array('I')
    while num > 1:
        result.append(spf[num])
        num = num // spf[num]
    
    return result


def main():
    N = int(input())
    spf = LinearSieve(5000000)
    for i in list(map(int, input().split())):
        print(*solve(spf, i))


main()
