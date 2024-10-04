# 백준 6086


from collections import deque
INF = 10e5


def BFS(capacity, source, sink, parent):
    visited = [False for _ in range(len(capacity))]
    
    q = deque([source])
    visited[source] = True
    
    while q:
        curV = q.popleft()
        
        for nextV in range(len(capacity)):
            # 용량이 남은 간선이 있는 경우
            if visited[nextV] == False and capacity[curV][nextV] > 0:
                q.append(nextV)
                visited[nextV] = True
                parent[nextV] = curV
                
                # sink에 도착할 경우
                if nextV == sink:
                    return True
    
    return False


def NetworkFlow(capacity, source, sink):
    parent = [-1 for _ in range(len(capacity))]
    max_flow = 0
    
    # BFS로 증가 경로 탐색
    while BFS(capacity, source, sink, parent):
        # 증가 경로의 최소 용량 탐색
        path_flow = INF
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]

        # 경로에 따라 용량 업데이트
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow

    return max_flow


# main 함수 ----------
N = int(input())
capacity = [[0 for _ in range(52)] for _ in range(52)]

for i in range(N):
    s, e, f = map(str, input().split())
    if s <= 'Z':
        s = ord(s) - ord('A')
    else:
        s = ord(s) - ord('a') + 26
    if e <= 'Z':
        e = ord(e) - ord('A')
    else:
        e = ord(e) - ord('a') + 26
        
    capacity[s][e] += int(f)
    capacity[e][s] += int(f)

print(NetworkFlow(capacity, 0, 25))
