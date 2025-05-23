# 백준 31263

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10000


def solve(N, S):
    DP = [INF for _ in range(N)]

    # DP[0] 처리
    DP[0] = 1
    if N > 1 and 10 <= int(S[:2]) <= 99:
        DP[1] = 1
    if N > 2 and 100 <= int(S[:3]) <= 641:
        DP[2] = 1

    # DP값 처리
    for i in range(1, N):
        # 길이 3 체크
        if i+2 < N and 100 <= int(S[i:i+3]) <= 641:
            DP[i+2] = min(DP[i+2], DP[i-1]+1)
        # 길이 2 체크
        if i+1 < N and 10 <= int(S[i:i+2]) <= 99:
            DP[i+1] = min(DP[i+1], DP[i-1]+1)
        # 길이 1 체크
        if 1 <= int(S[i]) <= 9:
            DP[i] = min(DP[i], DP[i-1]+1)

    return DP[N-1]


def main():
    N = int(input())
    S = input().decode().rstrip()
    print(solve(N, S))


main()
