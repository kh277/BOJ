# 백준 2533

'''
생각해볼 수 있는 것은 자신이 EA(얼리 어답터)일 경우, 자신의 자식 노드들은 전부 EA여야 한다.
자신이 EA일 경우는 자신의 자식 노드들은 EA일 수도 있고 아닐 수도 있다. 이 경우, 최소 EA값을 저장하면 된다.
모든 정점은 얼리 어답터이거나, 일반 정점이거나 둘 중 하나 뿐이다.
DP[i][type] = i번째 정점이 type(일반 정점=0, 얼리 어답터=1)일 경우, 자기 노드 + 모든 자손 노드 중 최소 얼리어답터 수

pypy3 언어로 재귀 탐색을 할 경우 메모리 초과가 발생하게 된다.
따라서 트리를 후위 순회 순서로 DP 처리를 하자.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, graph):
    DP = [[0, 0] for _ in range(N+1)]
    parent = [0] * (N+1)
    postorder = []      # 후위 순회 순서 저장
    startPos = 1

    # 후위 순회 순서 구하기
    stack = [1]
    parent[startPos] = -1
    while stack:
        curNode = stack.pop()
        postorder.append(curNode)

        for nextNode in graph[curNode]:
            if nextNode == parent[curNode]:
                continue

            parent[nextNode] = curNode
            stack.append(nextNode)

    # 후위 순회의 역순으로 DP 탐색
    for curNode in reversed(postorder):
        DP[curNode][1] += 1     # 자신이 EA인 경우 처리

        for nextNode in graph[curNode]:
            if nextNode == parent[curNode]:
                continue

            # 자신이 EA가 아닌 경우 -> 자식이 반드시 EA여야 함
            DP[curNode][0] += DP[nextNode][1]

            # 자신이 EA인 경우
            DP[curNode][1] += min(DP[nextNode])

    return min(DP[startPos])


def main():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(solve(N, graph))


main()