# 백준 2252

'''
위상 정렬을 이용하여 학생들의 키를 정렬하자.
'''

import sys
from collections import deque


def TopologySort(V: int, data: list) -> list:
    graph = [[] for _ in range(V+1)]        # 간선 정보가 담긴 연결 리스트
    inDegree = [0 for _ in range(V+1)]      # 각 정점의 진입 차수 저장

    # 연결 리스트 생성 및 진입 차수 설정 
    for i in data:
        graph[i[0]].append(i[1])
        inDegree[i[1]] += 1

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
    return result


def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(M):
        A, B = map(int, input().split())
        graph.append([A, B])
    
    print(*TopologySort(N, graph))


main()
