# 백준 1865

'''
음수 사이클이 존재하는지 찾아야 한다.
음수 간선이 있으므로 다익스트라 대신 벨만-포드를 사용해야 한다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8


def solve(V, E, edge):
    DP = array('i', [0]) * (V+1)

    for _ in range(1, V):
        for i in range(E):
            startV, endV, dist = edge[i]

            # 간선 갱신
            if DP[startV] + dist < DP[endV]:
                DP[endV] = DP[startV] + dist

    # 갱신이 한 번이라도 일어나는지 체크
    for i in range(1, V+1):
        for j in range(E):
            startV, endV, dist = edge[j]
            if DP[startV] + dist < DP[endV]:
                return 'YES'

    return 'NO'


def main():
    T = int(input())
    for _ in range(T):
        N, M, W = map(int, input().split())
        edge = []
        for _ in range(M):
            a, b, c = map(int, input().split())
            edge.append([a, b, c])
            edge.append([b, a, c])
        for _ in range(W):
            a, b, c = map(int, input().split())
            edge.append([a, b, -c])

        print(solve(N, 2*M+W, edge))


main()
