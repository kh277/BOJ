# 백준 17881

'''
DP[v][move] = 정점 v에서 move칸만큼 이동할 때 도착할 수 있는 섬 높이의 최소값
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
ARRAY_TYPE = 'i'
INF = 10**6


def solve(N, M, H, graph):
    DP = [array(ARRAY_TYPE, [INF]) * 501 for _ in range(N)]

    # 이동 횟수가 0일 때
    for v in range(N):
        DP[v][0] = H[v]

    # 이동 횟수가 1 이상일 때
    for move in range(1, 501):
        for curV in range(N):
            for prevV in graph[curV]:
                DP[curV][move] = min(DP[curV][move], DP[prevV][move-1])

    return DP


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    graph = [array(ARRAY_TYPE) for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    DP = solve(N, M, H, graph)
    T = int(input())
    for _ in range(T):
        a, k = map(int, input().split())
        print(DP[a-1][k] if DP[a-1][k] != INF else -1)


main()
