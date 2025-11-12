# 백준 14433

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# B에서 curV과 연결될 수 있는지 여부 체크
def DFS(curV, graph, visited, matchB):
    for nextV in graph[curV]:
        if visited[nextV] == True:
            continue
        visited[nextV] = True

        if matchB[nextV] == 0 or DFS(matchB[nextV], graph, visited, matchB):
            matchB[nextV] = curV
            return True

    return False


def FordFulkerson(numA, numB, edge):
    graph = [[] for _ in range(numA+1)]
    for curS, curE in edge:
        graph[curS].append(curE)

    matchB = [0 for _ in range(numB+1)]
    result = 0

    for curV in range(1, numA+1):
        if DFS(curV, graph, [False for _ in range(numB+1)], matchB):
            result += 1

    return result


def main():
    N, M, K1, K2 = map(int, input().split())
    pick = []
    for _ in range(K1):
        pick.append(tuple(map(int, input().split())))
    troll1 = FordFulkerson(N, M, pick)

    pick = []
    for _ in range(K2):
        pick.append(tuple(map(int, input().split())))
    troll2 = FordFulkerson(N, M, pick)

    if troll1 < troll2:
        print('네 다음 힐딱이')
        return
    print('그만 알아보자')


main()
