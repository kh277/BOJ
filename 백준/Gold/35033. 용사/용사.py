# 백준 35033

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# graph에서 자식 정점의 개수 구하기
def getTreeSize(V, graph, visited, subSize, root):
    # 루트에서 리프 노드로 내려가기
    parent = [0 for _ in range(V+1)]
    trace = [1]
    stack = []
    stack.append(root)
    visited[root] += 1
    parent[root] = -1

    while stack:
        curV = stack.pop()
        for nextV in graph[curV]:
            if visited[nextV] == -1:
                visited[nextV] += 1
                parent[nextV] = curV
                stack.append(nextV)
                trace.append(nextV)

    # 뒤집어 다시 올라가며 서브트리 정점 수 계산
    for curV in trace[::-1]:
        subSize[parent[curV]] += subSize[curV]


def solve(V, graph, root):
    # 각 서브트리에 속한 자식 정점의 개수 구하기
    visited = [-1 for _ in range(V+1)]
    subSize = [1] * (V+1)
    getTreeSize(V, graph, visited, subSize, 1)

    # 연결된 자식 정점의 개수가 많은 것부터 우선 처리하도록 정렬
    for i in range(1, V+1):
        graph[i].sort(key= lambda x: -subSize[x])

    stack1 = []
    stack2 = []
    seq = []
    stack1.append(root)
    visited[root] = 1

    # 비재귀 후위 순회
    while stack1:
        curV = stack1.pop()
        stack2.append(curV)

        for nextV in graph[curV]:
            if visited[nextV] == 0:
                stack1.append(nextV)
                visited[nextV] = 1

    while stack2:
        curV = stack2.pop()
        seq.append(curV)

    return seq


def main():
    V = int(input())
    graph = [[] for _ in range(V+1)]
    for _ in range(V-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(*solve(V, graph, 1))


main()
