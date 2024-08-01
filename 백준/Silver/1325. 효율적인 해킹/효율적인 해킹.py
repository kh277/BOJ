# 백준 1325

'''
A가 B를 신뢰할 경우 B를 해킹하면 A도 함께 해킹할 수 있게 된다.
이것을 B->A로 가는 간선으로 생각한다.
그러면 한 정점에서 가장 많은 칸을 이동할 수 있는 점은 무엇인가? 로 바뀌게 된다.

각 정점마다 BFS로 최대 길이를 탐색하자.

주의 반례
3 2
1 1
2 2
-> 1, 2, 3

5 4
3 2
4 3
3 4
4 5
-> 2, 5

7 5
2 1
3 1
4 1
6 5
7 6
-> 1
'''

import sys
from collections import deque

input = sys.stdin.readline


# start 정점에서 제일 멀리 떨어진 정점까지의 거리 구하기
def BFS(N: int, graph: list, start: list) -> list:
    visited = [0 for _ in range(N+1)]
    count = 1

    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()
        count += 1

        for next in graph[cur]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
        
    return count


def solve(N: int, graph: list) -> int:
    hack_count = [-1 for i in range(N+1)]

    # 각 정점에 대해 해킹되는 컴퓨터의 수 도출
    for i in range(1, N+1):
        hack_count[i] = BFS(N, graph, i)

    # 최대 데이터 도출
    max_data = max(hack_count)

    # 최대값과 중복이 되는 데이터가 있는지 확인
    result = []
    for i in range(1, N+1):
        if hack_count[i] == max_data:
            result.append(i)
    
    return result


def main():
    N, M = map(int, input().split())

    graph = [[] for i in range(N+1)]
    for i in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)

    print(*solve(N, graph))


main()