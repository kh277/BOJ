# 백준 17070

'''
모든 이동은 파이프의 머리쪽을 기준으로 생각한다.

가로 -> 대각선 : [y][x]에서 [y][x+1], [y+1][x], [y+1][x+1] 좌표 확인 후 이동
세로 -> 대각선 : [y][x]에서 [y][x+1], [y+1][x], [y+1][x+1] 좌표 확인 후 이동
대각선 -> 가로 : [y][x]에서 [y][x+1] 좌표 확인 후 이동
대각선 -> 세로 : [y][x]에서 [y+1][x] 좌표 확인 후 이동

좌표에 이동 방향까지 기록해야 하므로 3차원 DP를 이용하자.
DP[y][x][i] = 머리가 [y][x]이고 i(0은 가로, 1은 대각선, 2는 세로) 방향을 보는 경우의 수 
'''

import sys

input = sys.stdin.readline



def solve(N: int, graph: list) -> int:
    DP = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

    # 시작점 초기화 [가로방향 경우, 대각선방향 경우, 세로방향 경우]
    DP[0][1] = [1, 0, 0]

    for y in range(N):
        for x in range(1, N):
            if y < N-1 and graph[y+1][x] != 1:
                DP[y+1][x][2] += DP[y][x][1]    # 대각선 -> 세로
                DP[y+1][x][2] += DP[y][x][2]    # 세로 -> 세로
            if x < N-1 and graph[y][x+1] != 1:
                DP[y][x+1][0] += DP[y][x][0]    # 가로 -> 가로
                DP[y][x+1][0] += DP[y][x][1]    # 대각선 -> 가로
            if y < N-1 and x < N-1 and graph[y+1][x] != 1 and graph[y][x+1] != 1 and graph[y+1][x+1] != 1:
                DP[y+1][x+1][1] += DP[y][x][0]  # 가로 -> 대각선
                DP[y+1][x+1][1] += DP[y][x][1]  # 대각선 -> 대각선
                DP[y+1][x+1][1] += DP[y][x][2]  # 세로 -> 대각선

    return sum(DP[N-1][N-1])


def main():
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    
    print(solve(N, graph))


main()