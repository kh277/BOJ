# 백준 13261

'''
일반적이 DP로 처리하면 TLE가 나오므로, DnC opt를 이용해 DP 계산을 최적화해야 한다.

DP[i][j] = min(DP[i-1][k] + C[k+1][j])
(i명이 [0, j]칸까지 감시할 때 최소 위험도)
    = min((i-1명이 [0, k]칸까지 감시할 때 최소 위험도) + ([1명이 [k+1, j]칸까지 감시하는 비용])), (0 <= k < j)

참고한 코드 : https://seastar105.tistory.com/31
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def recur(DP, accSum, curGuard, start, end, optStart, optEnd):
    mid = (start+end)//2
    divide = -1

    # 하위 부분 DP 계산
    for k in range(optStart, min(mid, optEnd)):
        curV = DP[curGuard-1][k] + (accSum[mid]-accSum[k])*(mid-k)
        if divide == -1 or DP[curGuard][mid] > curV:
            divide = k
            DP[curGuard][mid] = curV

    # 두 구간 [start, mid-1], [mid+1, end]으로 분할
    if start <= mid-1:
        recur(DP, accSum, curGuard, start, mid-1, optStart, divide+1)
    if mid+1 <= end:
        recur(DP, accSum, curGuard, mid+1, end, divide, optEnd)


def solve(L, G, C):
    # 누적합 전처리
    accSum = [0 for _ in range(L+1)]
    for i in range(1, L+1):
        accSum[i] = accSum[i-1] + C[i]

    # DP 초기값 설정
    DP = [[0 for _ in range(L+1)] for _ in range(G+1)]
    for i in range(1, L+1):
        DP[1][i] = accSum[i] * i

    # DP 계산
    for i in range(2, G+1):
        recur(DP, accSum, i, 1, L, 0, L)

    return DP[G][L]


def main():
    L, G = map(int, input().split())
    C = [0] + list(map(int, input().split()))

    print(solve(L, G, C))


main()
