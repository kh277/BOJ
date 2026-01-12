# 백준 31838

'''
DP[i][isCatch] = i번째 아이템을 주웠는지 여부가 isCatch일 때, [0, i] 구간에서의 가치 최대값.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, A):
    # 누적 합 배열 전처리
    accSum = [0 for _ in range(N)]
    accSum[0] = A[0]
    for i in range(1, N):
        accSum[i] = accSum[i-1] + A[i]
    
    # DP 계산
    DP = [[0, 0] for _ in range(N+K)]
    DP[0][0] = 0
    DP[0][1] = A[0]

    for i in range(1, N+K):
        # 이전 칸에서 집고 이번 칸에서 또 집는 경우
        DP[i][0] = max(DP[i-1])
        if i < N:
            DP[i][1] = DP[i-1][1] + A[i]

        # K칸의 아이템을 집는 경우
        if K <= i < N:
            DP[i][1] = max(DP[i][1], max(DP[i-K]) + accSum[i] - accSum[i-K])

        # N칸을 넘어서 주워야 하는 경우
        if i > N:
            DP[i][1] = max(DP[i-K]) + accSum[N-1] - accSum[i-K]

    return max([max(i) for i in DP])


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, K, A))


main()
