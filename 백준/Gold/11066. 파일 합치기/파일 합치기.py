# 백준 11066

'''
DP[i][j] = j번 파일 ~ i번 파일을 전부 합칠 때 필요한 비용의 최소값
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def solve(N, data):
    # 누적합 계산
    accSum = [0 for i in range(N)]
    accSum[0] = data[0]
    for i in range(1, N):
        accSum[i] = accSum[i-1] + data[i]

    # DP 계산
    DP = [[INF for _ in range(i+1)] for i in range(N)]
    for i in range(N):
        DP[i][i] = 0
    for fileSize in range(1, N):
        for startF in range(N-fileSize):
            endF = startF + fileSize
            for i in range(startF, endF):
                if startF == 0:
                    DP[endF][startF] = min(DP[endF][startF], DP[i][startF] + DP[endF][i+1] + accSum[endF])
                else:
                    DP[endF][startF] = min(DP[endF][startF], DP[i][startF] + DP[endF][i+1] + accSum[endF]-accSum[startF-1])

    return DP[N-1][0]


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        data = list(map(int, input().split()))
        print(solve(N, data))


main()
