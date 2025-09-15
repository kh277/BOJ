# 백준 26987

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


def solve(graph):
    scc = SCC(graph)

    result = 0
    for i in scc:
        if len(i) >= 2:
            result += 1

    return result


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)

    print(solve(graph))


main()
