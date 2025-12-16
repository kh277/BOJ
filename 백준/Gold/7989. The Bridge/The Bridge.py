# 백준 7989

'''
DP[i] = i번째 사람까지 옮기는 데 필요한 최소 시간
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, W):
    if N == 1:
        return W[0]
    elif N == 2:
        return W[1]

    DP = [0 for _ in range(N)]
    DP[0] = W[0]
    DP[1] = W[1]
    DP[2] = W[0]+W[1]+W[2]

    for i in range(3, N):
        DP[i] = DP[i-2] + min(W[0] + 2*W[1] + W[i], 2*W[0] + W[i-1] + W[i])

    return DP[N-1]


def main():
    N = int(input())
    W = []
    for _ in range(N):
        W.append(int(input()))

    print(solve(N, W))


main()
