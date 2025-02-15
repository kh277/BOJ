# 백준 2533

'''
생각해볼 수 있는 것은 자신이 EA(얼리 어답터)일 경우, 자신의 자식 노드들은 전부 EA여야 한다.
자신이 EA일 경우는 자신의 자식 노드들은 EA일 수도 있고 아닐 수도 있다. 이 경우, 최소 EA값을 저장하면 된다.
모든 정점은 얼리 어답터이거나, 일반 정점이거나 둘 중 하나 뿐이다.
DP[i][type] = i번째 정점이 type(일반 정점=0, 얼리 어답터=1)일 경우, 자기 노드 + 모든 자손 노드 중 최소 얼리어답터 수
'''

import io
import sys
import random

sys.setrecursionlimit(10**6)
input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def recur(curNode, graph, DP, visited):
    visited[curNode] = True

    # 자신이 EA인 경우 처리
    DP[curNode][1] += 1

    for nextNode in graph[curNode]:
        if visited[nextNode] == False:
            recur(nextNode, graph, DP, visited)
            
            # 자신이 EA가 아닌 경우 -> 자식이 반드시 EA여야 함
            DP[curNode][0] += DP[nextNode][1]

            # 자신이 EA인 경우
            DP[curNode][1] += min(DP[nextNode])


def solve(N, graph):
    DP = [[0, 0] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    startPos = random.randrange(1, N+1)

    recur(startPos, graph, DP, visited)
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