# 백준 24782

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def DFS(N, K, graph, curV, colorList):
    if curV == N:
        return 1

    result = 0
    for curColor in range(K):
        # curV를 curColor로 칠할 수 있는지 체크
        canPaint = True
        for nextV in graph[curV]:
            if colorList[nextV] == curColor:
                canPaint = False
                break

        # 이후 재귀
        if canPaint == True:
            colorList[curV] = curColor
            result = max(result, DFS(N, K, graph, curV+1, colorList))
            colorList[curV] = -1

    return result


def solve(N, graph):
    # 첫 번째 색은 0번으로 미리 지정
    colorList = [-1] * N
    colorList[0] = 0

    # 그래프를 i색으로 칠할 수 있는지 체크
    for i in range(1, N):
        canPaint = DFS(N, i, graph, 1, colorList)
        if canPaint == 1:
            return i
    return N


def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    print(solve(N, graph))


main()
