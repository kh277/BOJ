# 백준 20120

'''
DP[cur][combo] = cur번째 노트를 반드시 처리했고, 현재 콤보가 combo일 때, 얻을 수 있는 점수의 최대값
maxV[i] = DP[i][0]을 제외한 DP[i] 값들 중 최대값
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def solve(N, A):
    # N이 2 이하인 경우
    if N == 1:
        return max(0, A[0])
    elif N == 2:
        return max(0, A[0], A[1], A[0]+2*A[1])

    DP = [[-INF for _ in range(i+1)] for i in range(N+1)]
    maxV = [-INF for _ in range(N+1)]

    # 초기값 설정
    DP[1] = [0, A[0]]
    DP[2] = [0, A[1], A[0] + 2*A[1]]
    maxV[1] = DP[1][1]
    maxV[2] = max(DP[2][1], DP[2][2])

    # 이후 DP 처리
    for cur in range(3, N+1):
        DP[cur][0] = max(maxV[cur-1], maxV[cur-2])
        for combo in range(1, cur+1):
            DP[cur][combo] = DP[cur-1][combo-1] + combo*A[cur-1]
            maxV[cur] = max(maxV[cur], DP[cur][combo])

    return max(0, maxV[N], maxV[N-1], maxV[N-2])


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
