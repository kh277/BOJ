# 백준 3024


import sys

input = sys.stdin.readline


def solve(N: int, graph: list) -> str:

    # 좌상단에서 우하단으로 진행
    for y in range(N-2):
        for x in range(N-2):
            cur = graph[y][x]
            if cur == '.':
                continue
            count = [0, 0, 0]   # 가로, 세로, 대각선 연속 수
            for i in range(3):
                if graph[y+i][x] == cur:
                    count[0] += 1
                if graph[y][x+i] == cur:
                    count[1] += 1
                if graph[y+i][x+i] == cur:
                    count[2] += 1
            
            if 3 in count:
                return cur
    
    # 우상단에서 좌하단으로 진행
    for y in range(N-2):
        for x in range(N-1, 1, -1):
            cur = graph[y][x]
            if cur == '.':
                continue

            count = [0, 0, 0]   # 가로, 세로, 대각선 연속 수
            for i in range(3):
                if graph[y+i][x] == cur:
                    count[0] += 1
                if graph[y][x-i] == cur:
                    count[1] += 1
                if graph[y+i][x-i] == cur:
                    count[2] += 1
            if 3 in count:
                return cur    
    return "ongoing"


def main():
    N = int(input())

    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    print(solve(N, graph))


main()