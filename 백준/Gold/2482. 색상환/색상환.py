# 백준 2482

'''
DP[y][x] = 총 y개의 색을 사용하면서, 마지막으로 칠한 색이 x인 경우의 수 (x: 0-index, y: 1-index)
DP[y][x] = DP[y][x-1] + DP[y-1][x-2]
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 10**9+3


def solve(N, K):
    if K > N//2:
        return 0

    # 1. 0번에 색을 칠하는 경우
    DP = [array('I', [0])*N for _ in range(N//2+1)]
    DP[1][0] = 1
    for y in range(2, N//2+1):
        for x in range(y, N):
            DP[y][x] = (DP[y][x-1] + DP[y-1][x-2]) % MOD

    # K개의 색을 칠하지만, N-1번에 색을 칠하면 안됨
    result = 0
    for x in range((K-1)//2, N-1):
        result = (result + DP[K][x]) % MOD

    # 2. 0번에 색을 칠하지 않는 경우
    DP = [array('I', [0])*N for _ in range(N//2+1)]
    for x in range(1, N):
        DP[1][x] = 1
    for y in range(2, N//2+1):
        for x in range(y, N):
            DP[y][x] = (DP[y][x-1] + DP[y-1][x-2]) % MOD

    # K개의 색을 칠함
    for x in range((K-1)//2, N):
        result = (result + DP[K][x]) % MOD

    return result


def main():
    N = int(input())
    K = int(input())
    print(solve(N, K))


main()
