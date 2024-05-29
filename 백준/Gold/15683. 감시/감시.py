# 백준 15683

import sys
from copy import deepcopy

input = sys.stdin.readline


class CCTV():
    def __init__(self, N: int, M: int, graph: list):
        self.N = N
        self.M = M
        self.graph = graph
        self.camera = []
        self.answer = 10e2


    # 사각지대의 개수 구하기
    def check_point(self, graph: list) -> int:
        count = 0
        for y in range(self.N):
            for x in range(self.M):
                if graph[y][x] == 0:
                    count += 1
    
        return count


    # 카메라의 시야가 닿는 곳은 -1로 바꾸는 함수
    def change(self, graph: list, curY: int, curX: int, case: list):
        pointX = [0, -1, 0, 1]
        pointY = [1, 0, -1, 0]

        case = case % 4

        while True:
            nextX = curX + pointX[case]
            nextY = curY + pointY[case]
            curX = nextX
            curY = nextY

            # 맵 내부라면
            if 0 <= nextY < self.N and 0 <= nextX < self.M:
                # 다음 탐색 위치가 벽이라면
                if graph[nextY][nextX] == 6:
                    return graph

                # 다음 탐색 위치가 카메라가 아니라면
                elif graph[nextY][nextX] == 0:
                    graph[nextY][nextX] = -1

                # 다음 탐색 위치가 카메라라면
                else:
                    continue
            
            # 맵 외부라면
            else:
                return graph


    def DFS(self, graph: list, depth: int):
        # 종료조건
        if depth == len(self.camera):
            self.answer = min(self.answer, self.check_point(graph))
            return
        
        cameraX = self.camera[depth][1]
        cameraY = self.camera[depth][0]

        # 상하좌우 방향에 대해 반복
        for i in range(4):
            temp = deepcopy(graph)
            case = graph[cameraY][cameraX]

            # 카메라의 종류에 따라 분류
            if case == 1:
                temp = self.change(temp, cameraY, cameraX, i)
            elif case == 2:
                temp = self.change(temp, cameraY, cameraX, i)
                temp = self.change(temp, cameraY, cameraX, i+2)
            elif case == 3:
                temp = self.change(temp, cameraY, cameraX, i)
                temp = self.change(temp, cameraY, cameraX, i+1)
            elif case == 4:
                temp = self.change(temp, cameraY, cameraX, i)
                temp = self.change(temp, cameraY, cameraX, i+1)
                temp = self.change(temp, cameraY, cameraX, i+2)
            else:
                temp = self.change(temp, cameraY, cameraX, i)
                temp = self.change(temp, cameraY, cameraX, i+1)
                temp = self.change(temp, cameraY, cameraX, i+2)
                temp = self.change(temp, cameraY, cameraX, i+3)

            self.DFS(temp, depth + 1)


    def solve(self):
        # 카메라의 위치 확인
        for y in range(self.N):
            for x in range(self.M):
                if self.graph[y][x] not in [0, 6]:
                    self.camera.append([y, x])
    
        # DFS를 통해 최소 사각지대 구하기
        self.DFS(self.graph, 0)


def main():
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    a = CCTV(N, M, graph)
    a.solve()
    print(a.answer)


main()