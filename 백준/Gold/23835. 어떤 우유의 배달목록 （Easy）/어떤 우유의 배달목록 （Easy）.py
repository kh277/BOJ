# 백준 2836

'''
뒤로 가는 경로들 중 겹치는 부분은 최대한 합쳐서 전체 길이를 센다.
이 길이가 보트를 뒤로 이동하는 총 거리가 된다.
'''

import io
from array import array
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# start -> end로 가는 경로에 우유 개수 추가
def update(N, graph, start, end, milk):
    visited = [-1] * N      # 방문 처리 및 부모 정점 탐색
    q = deque()
    q.append([start, 0])
    visited[start] = start

    while q:
        curV, passV = q.pop()

        # 마지막 방에 도착한 경우 경로에 대해 우유 추가
        if curV == end:
            while passV > 0:
                milk[curV] += passV
                curV = visited[curV]
                passV -= 1
            return

        # 정점 탐색
        for nextV in graph[curV]:
            if visited[nextV] == -1:
                q.append([nextV, passV+1])
                visited[nextV] = curV


def main():
    N = int(input())
    graph = [array('I') for _ in range(N)]
    milk = array('I', [0]) * N
    for _ in range(N-1):
        s, e = map(int, input().split())
        graph[s-1].append(e-1)
        graph[e-1].append(s-1)

    Q = int(input())
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            update(N, graph, q[1]-1, q[2]-1, milk)
        else:
            print(milk[q[1]-1])


main()
