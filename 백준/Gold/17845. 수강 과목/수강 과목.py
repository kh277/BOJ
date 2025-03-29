# 백준 17845

'''
최대 공부시간(N) = 배낭의 무게, 과목의 중요도 = 물건의 가치인 배낭 문제이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, subj):
    DP = [[0 for _ in range(N+1)] for _ in range(K+1)]

    for x in range(1, K+1):
        curV, curW = subj[x-1]
        for y in range(1, N+1):
            if y - curW >= 0:
                DP[x][y] = max(DP[x][y-1], DP[x-1][y-curW]+curV, DP[x-1][y])
            else:
                DP[x][y] = max(DP[x][y-1], DP[x-1][y])

    return DP[K][N] 


def main():
    N, K = map(int, input().split())
    subj = []
    for _ in range(K):
        subj.append(list(map(int, input().split())))
    print(solve(N, K, subj))


main()