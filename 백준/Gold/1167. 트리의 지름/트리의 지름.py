# 백준 1167

'''
V개의 정점, 및 여러 개의 간선이 존재.
어떤 정점에서 다른 정점까지의 거리가 가장 긴 것이 지름. 이 때 트리의 지름은?
-> 아무 점이나 잡고 DFS 진행 시 해당 점으로부터 가장 멀리 떨어진 점으로 이동.
이동한 점에서 다시 DFS 진행 시 다른 가장 먼 점으로 이동. 이 거리가 지름이 됨.
'''

import sys

input = sys.stdin.readline

def DFS(graph: list, visited: list, start: int, distance: int) -> list:
    # 맨 처음 DFS를 실행한 경우 - visited 리스트 생성
    if visited == None:
        visited = [False for _ in range(len(graph)+1)]

    visited[start] = True
    max_distance = distance
    max_point = start

    # 현재 정점에서 탐색할 수 있는 다른 모든 정점에 대해
    # 다음에 탐색할 [노드, 거리]가 나옴
    for next in graph[start]:
        if not visited[next[0]]:
            temp = DFS(graph, visited, next[0], distance+next[1])

            # 거리 갱신이 된다면 -> 갱신하기
            if temp[1] > max_distance:
                max_point = temp[0]
                max_distance = temp[1]
    
    return [max_point, max_distance]
                

def solve(V: int, graph: list, start: int) -> int:
    # 아무 점에서 DFS 진행 -> 가장 먼 점 temp의 위치 반환
    temp = DFS(graph, None, start, 0)

    # temp에서 가장 멀리 떨어진 result의 위치 반환
    result = DFS(graph, None, temp[0], 0)

    # result의 가중치 반환
    return result[1]


def main():
    V = int(input())
    graph = [[] for _ in range(V+1)]

    for i in range(V):
        temp = list(map(int, input().split()))
        
        # (도착 정점, 길이) 순으로 정보 저장
        for j in range(1, len(temp)-1, 2):
            graph[temp[0]].append([temp[j], temp[j+1]])
    
    print(solve(V, graph, 1))


main()
