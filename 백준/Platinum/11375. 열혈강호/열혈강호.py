# 백준 11375

import io, sys

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
sys.setrecursionlimit(10**5)


# B에서 curV과 연결될 수 있는지 여부 체크
def DFS(curV, graph, visited, matchB):
    for nextV in graph[curV]:
        if visited[nextV] == True:
            continue
        visited[nextV] = True

        # nextV가 매칭되지 않았거나, 다른 정점과 매칭시킬 수 있다면 -> 연결
        if matchB[nextV] == 0 or DFS(matchB[nextV], graph, visited, matchB):
            matchB[nextV] = curV
            return True

    return False


def Ford_Fulkerson(numA, numB, graph):
    matchB = [0 for _ in range(numB+1)]
    result = 0

    for curV in range(1, numA+1):
        if DFS(curV, graph, [False for _ in range(numB+1)], matchB):
            result += 1

    return result


def main():
    N, M = map(int, input().split())

    # 간선 정보 전처리
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i] = list(map(int, input().split()))[1:]

    print(Ford_Fulkerson(N, M, graph))


main()