# 백준 16964

import sys
from collections import deque

input = sys.stdin.readline


# 자식 중 next가 있는 정점이 나올 때까지 위쪽 정점으로 올라가며 탐색
def check_next(next: int, stack: list, graph: list):
    # cur의 자식에 next가 없는 경우 위쪽 정점으로 올라감
    while stack:
        cur = stack[-1]
        if next in graph[cur]:
            return True
        else:
            stack.pop()
    
    return False
        

def solve(N: int, graph: list, visit_seq: list) -> int:
    # 반례 - 탐색 시작 정점이 1이 아닐 경우
    if visit_seq[0] != 1:
        return 0

    stack = deque()
    visited = [False for _ in range(N+1)]

    # DFS 방문 순서가 올바른지 순서대로 확인
    for i in range(N-1):
        cur = visit_seq[i]      # 현재 탐색 정점
        next = visit_seq[i+1]   # 다음 탐색 정점

        # cur 정점 방문 처리
        stack.append(cur)
        visited[cur] = True

        # cur의 자식에 next가 있는 경우
        if next in graph[cur]:
            continue

        # cur의 자식에 next가 없는 경우 위쪽 정점으로 올라감
        elif check_next(next, stack, graph):
            continue
    
        # 제일 위쪽 정점까지 올라갔는데도 next가 자식 목록에 없는 경우
        else:
            return 0
    
    # 모든 방문 순서가 올바른 경우
    return 1


def main():
    N = int(input())

    # 0번 정점은 미사용
    graph = [[] for i in range(N+1)]

    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visit_seq = list(map(int, input().split()))
    
    print(solve(N, graph, visit_seq))


main()