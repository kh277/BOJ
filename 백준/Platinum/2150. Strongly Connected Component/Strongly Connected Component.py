# 백준 2150

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

            # 노드를 처음 방문하는 경우
            if pi == 0:
                if curV in low:
                    continue
                low[curV] = num
                stack.append(curV)
            
            # 재방문한 경우
            if pi > 0:
                low[curV] = min(low[curV], low[graph[curV][pi-1]])
            
            # 인접 노드 처리
            if pi < len(graph[curV]):
                callStack.append((curV, pi+1, num))
                callStack.append((graph[curV][pi], 0, len(low)))
                continue

            # 모든 인접 노드 처리가 끝난 경우
            if num == low[curV]:
                comp = []
                while True:
                    comp.append(stack.pop())
                    low[comp[-1]] = len(graph)
                    if comp[-1] == curV:
                        break
                result.append(comp)

    return result


def main():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    result = [sorted(i) for i in SCC(graph)[1:]]
    result.sort(key= lambda x: x[0])

    print(len(result))
    for i in result:
        print(*sorted(i), end=" ")
        print(-1)


main()
