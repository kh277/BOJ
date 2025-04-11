# 백준 15795

'''
DP[i] = 길이가 i이고 K까지의 수를 사용한 흥미로운 수열의 개수
즉, DP[N] = DP[N-1] + DP[N-2] + ... + DP[N-K]가 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


def solve(N, K):
    DP = [0 for _ in range(N+1)]
    DP[0] = 1

    window = DP[0]
    for i in range(1, N+1):
        DP[i] = window % MOD
        window = (window + DP[i]) % MOD
        if i >= K:
            window = (window - DP[i-K])

    return DP[N]


def main():
    N, K = map(int, input().split())
    print(solve(N, K))


main()