# 백준 1068

import sys
from collections import deque

input = sys.stdin.readline


def solve():
    # 그래프 생성
    graph = [[] for _ in range(N)]
    for i in range(N):
        if node[i] == -1:
            continue
        graph[node[i]].append(i)
    
    # 트리에서 delNode와 연결된 노드 저장
    delNodeList = set()
    q = deque()
    q.append(delNode)
    delNodeList.add(delNode)
    while q:
        cur = q.popleft()
        
        for i in graph[cur]:
            q.append(i)
            delNodeList.add(i)
    
    # 루트부터 탐색
    q = deque()
    q.append(0)
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if i in delNodeList:
                graph[cur].remove(i)
            else:
                q.append(i)
    
    # 자식이 0개인 노드 개수 세기
    result = 0
    for i in range(N):
        if len(graph[i]) == 0 and i not in delNodeList:
            result += 1
    
    return result


# main 함수 ----------
N = int(input())
node = list(map(int, input().split()))
delNode = int(input())

print(solve())