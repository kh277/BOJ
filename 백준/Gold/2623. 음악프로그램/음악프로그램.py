# 백준 2623

'''
가수(정점)의 수 M과 보조 PD의 수 M이 주어진다.
출연 가수의 순서를 정해야 하므로 위상 정렬을 통해 순서를 출력하자.

또한, 아래 반례처럼 사이클이 존재하면 0을 출력해야 하므로 

주의 반례
4 2
3 1 2 3
3 3 4 2
-> 0
'''

import sys
from collections import deque

input = sys.stdin.readline


def check_cycle(cur: int, graph: list, visited: list, traced: list) -> list:
    # 이미 방문한 정점이면 함수 종료
    if cur in visited:
        return True
    
    # 경로에 포함되어 있는 노드 -> 사이클 발생
    if cur in traced:
        return False
    
    traced.add(cur)
    
    for next in graph[cur]:
        if not check_cycle(next, graph, visited, traced):
            return False
    
    traced.remove(cur)
    visited.add(cur)

    return True


def TopologySort(V: int, data: list) -> list:
    graph = [[] for _ in range(V+1)]        # 간선 정보가 담긴 연결 리스트
    inDegree = [0 for _ in range(V+1)]      # 각 정점의 진입 차수 저장

    # 그래프 생성 (연결 리스트 생성 및 진입 차수 설정) -----
    for i in data:
        graph[i[0]].append(i[1])
        inDegree[i[1]] += 1
    
    # 사이클 확인 -----
    visited = set()
    traced = set()
    for i in range(V):
        if i in visited:
            continue
        if check_cycle(i, graph, visited, traced) == False:
            return [0]

    # 위상 정렬 -----
    result = []
    q = deque()

    # 진입차수가 0인 정점 큐에 삽입
    for i in range(1, V+1):
        if inDegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        cur = q.popleft()
        result.append(cur)

        # cur과 직접 연결된 노드들의 진입차수 - 1
        for neighbor in graph[cur]:
            inDegree[neighbor] -= 1

            # 진입차수가 0인 정점만 큐에 삽입
            if inDegree[neighbor] == 0:
                q.append(neighbor)

    # 위상 정렬 결과 리턴
    if len(result) == 0:
        return [0]
    return result


def main():
    N, M = map(int, input().split())

    graph = []
    for i in range(M):
        temp = list(map(int, input().split()))
        for j in range(1, temp[0]):
            graph.append([temp[j], temp[j+1]])

    for i in TopologySort(N, graph):
        print(i)


main()
