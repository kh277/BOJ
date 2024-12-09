# 백준 32931

'''
현재 열에서 자석이 지나간 칸을 1로 표시한다면, 모든 열은 10, 01, 11로 표현할 수 있다.
또한, 첫 칸은 10, 11만 가능하며, 마지막 칸은 01, 11만 가능하다.
그리고 이전 칸이 10이었다면 현재 칸에서 01은 불가능하다.
위 사항을 고려하여 DP 테이블을 구성하자.
'''

import sys

input = sys.stdin.readline
INF = 10e15


def solve():
    # DP[x][status] = 현재 열이 x일 때, status(10, 11, 01)가 가능한 경우의 수
    DP = [[0 for _ in range(3)] for _ in range(N)]
    DP[0] = [graph[0][0], graph[0][0] + graph[1][0], -INF]

    for x in range(1, N):
        DP[x][0] = max(DP[x-1][0], DP[x-1][1]) + graph[0][x]
        DP[x][1] = max(DP[x-1]) + graph[0][x] + graph[1][x]
        DP[x][2] = max(DP[x-1][1], DP[x-1][2]) + graph[1][x]

    return max(DP[N-1][1], DP[N-1][2])


# main 함수 ----------
N = int(input())
graph = []
for i in range(2):
    graph.append(list(map(int, input().split())))

print(solve())