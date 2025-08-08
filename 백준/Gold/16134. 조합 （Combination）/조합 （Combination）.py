# 백준 16134

'''
n * (n-1) * ... * (n-k+1) * (k!)^(p-2)
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, K):
    result = 1
    for i in range(N-K+1, N+1):
        result = (result * i) % MOD
    factK = 1
    for i in range(1, K+1):
        factK = (factK * i) % MOD
    
    return (result * pow(factK, MOD-2, MOD)) % MOD


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()
