# 백준 2344

'''
1. 해당 상자에서 각 가로 및 세로 칸에 대해 입력과 출력은 1대1 대응이다.
즉, 1번에서 9번으로 빛이 가게 된다면, 9번은 반드시 1번으로만 가게 된다.
2. 또한 왼쪽 칸 또는 아래쪽 칸에서 입력된 빛은 무조건 오른쪽 칸 또는 위쪽 칸으로 가게 된다.

위 두 가지 특징을 가지고 왼쪽, 아래쪽에 대해서만 입력을 구한 뒤 오른쪽, 위쪽은 입출력을 반전시키면 된다.
'''

import sys

input = sys.stdin.readline


# [y좌표, x좌표, 방향]에서 출발 -> [y좌표, x좌표, 방향]에 도착
def light(N: int, M: int, graph: list, start: list) -> list:
    cur = start
    while True:
        # 현재 위치에 거울이 존재한다면 -> 방향 전환
        if graph[cur[0]][cur[1]] == 1:
            cur = [cur[0], cur[1], cur[2]^1]

        # 오른쪽 또는 위쪽 끝에 도달한 경우 -> 탈출
        if (cur[0] == 0 and cur[2] == 1) or (cur[1] == M-1 and cur[2] == 0):
            return cur
        
        # 좌->우 방향일 경우
        if cur[2] == 0:
            cur = [cur[0], cur[1]+1, 0]
        # 하->상 방향일 경우
        else:
            cur = [cur[0]-1, cur[1], 1]


def solve(N: int, M: int, graph: list) -> list:
    result = [0 for _ in range(2*N + 2*M + 1)]

    # 왼쪽에서 시작하는 1 ~ N번까지 빛 처리
    for y in range(N):
        
        # [y좌표, x좌표, 방향(0은 좌에서 우, 1은 하에서 상)] 순서로 저장
        start = [y, 0, 0]
        temp = light(N, M, graph, start)

        # 위쪽에 도착한 경우 (y좌표가 0, 방향이 하->상인 경우)
        if temp[0] == 0 and temp[2] == 1:
            result[y+1] = 2*N + 2*M - temp[1]
            result[2*N + 2*M - temp[1]] = y+1
        
        # 오른쪽에 도착한 경우 (x좌표가 M-1, 방향이 좌->우인 경우)
        else:
            result[y+1] = 2*N + M - temp[0]
            result[2*N + M - temp[0]] = y+1

    # 아래쪽에서 시작하는 N+1 ~ N+M번까지 빛 처리
    for x in range(M):
        start = [N-1, x, 1]
        temp = light(N, M, graph, start)

        # 위쪽에 도착한 경우
        if temp[0] == 0 and temp[2] == 1:
            result[x+N+1] = 2*N + 2*M - temp[1]
            result[2*N + 2*M - temp[1]] = x+N+1
        
        # 오른쪽에 도착한 경우
        else:
            result[x+N+1] = 2*N + M - temp[0]
            result[2*N + M - temp[0]] = x+N+1

    return result[1:]


def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    print(*solve(N, M, graph))


main()