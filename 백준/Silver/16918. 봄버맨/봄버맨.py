# 백준 16918

import sys

input = sys.stdin.readline


def solve(R: int, C: int, N: int, graph: list) -> list:
    pointX = [-1, 1, 0, 0]
    pointY = [0, 0, -1, 1]

    # 초기 1초가 지났을 때
    for y in range(R):
        for x in range(C):
            if graph[y][x] == 'O':
                graph[y][x] = ('O', True)
            if graph[y][x] == '.':
                graph[y][x] = ('.', False)

    time = 1

    # 이후 시간에 대해 반복
    while time < N:
        time += 1

        # 짝수 시간일 경우 -> 빈 칸에 폭탄 설치
        if time % 2 == 0:
            for y in range(R):
                for x in range(C):
                    if graph[y][x][0] == '.':
                        graph[y][x] = ('O', False)

        # 홀수 시간일 경우 -> 폭탄 전부 폭발
        else:
            for y in range(R):
                for x in range(C):
                    # 폭탄 폭발
                    if graph[y][x][0] == 'O' and graph[y][x][1] == True:
                        graph[y][x] = ('.', False)
                        for i in range(4):
                            nextY = y + pointY[i]
                            nextX = x + pointX[i]

                            # 폭발 가능한 범위라면 폭발
                            if 0 <= nextX < C and 0 <= nextY < R and graph[nextY][nextX][1] != True:
                                graph[nextY][nextX] = ('.', False)
                
            # 남은 폭탄 폭발 준비
            for y in range(R):
                for x in range(C):
                    if graph[y][x][0] == 'O' and graph[y][x][1] == False:
                        graph[y][x] = ('O', True)

    # 그래프의 0번 인덱스만 추출
    return [''.join([x[0] for x in y]) for y in graph]


def main():
    # 세로, 가로, N초 후
    R, C, N = map(int, input().split())

    graph = []
    for i in range(R):
        graph.append(list(input().rstrip()))

    for i in solve(R, C, N, graph):
        for j in i:
            print(j, end='')
        print()

main()
