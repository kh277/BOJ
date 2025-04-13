# 백준 4196

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def SCC(graph):
    result = []
    stack = []
    low = dict()
    callStack = []

    for curV in range(len(graph)):
        callStack.append((curV, 0, len(low)))

        # DFS 처리
        while callStack:
            curV, pi, num = callStack.pop()

            if pi == 0:
                if curV in low:
                    continue
                low[curV] = num
                stack.append(curV)

            if pi > 0:
                low[curV] = min(low[curV], low[graph[curV][pi-1]])

            if pi < len(graph[curV]):
                callStack.append((curV, pi+1, num))
                callStack.append((graph[curV][pi], 0, len(low)))
                continue

            if num == low[curV]:
                comp = []
                while True:
                    comp.append(stack.pop())
                    low[comp[-1]] = len(graph)
                    if comp[-1] == curV:
                        break

                result.append(comp)

    return result[1:]


def solve(N, graph):
    # SCC 계산
    scc = SCC(graph)

    # 각 정점이 속하는 SCC 집합 저장
    sccPart = [-1 for _ in range(N+1)]
    for i in range(len(scc)):
        for j in scc[i]:
            sccPart[j] = i

    edge = []
    # 한 SCC 집합에서 다른 SCC 집합로 가는 간선만 따로 추출
    for curS in range(1, N+1):
        for curE in graph[curS]:
            if sccPart[curS] != sccPart[curE]:
                edge.append([sccPart[curS], sccPart[curE]])

    # 진입 차수 계산
    inDegree = [0 for _ in range(len(scc)+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        inDegree[i[1]] += 1

    # 진입 차수가 0인 집합 계산
    result = 0
    for i in inDegree:
        if i == 0:
            result += 1

    return result - 1


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        graph = [[] for _ in range(N+1)]
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)

        print(solve(N, graph))


main()
