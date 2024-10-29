# 백준 22479

'''
점 P를 통과하는 어떤 직선으로 도형을 절단해도
절단한 넓이가 같아지는 점의 좌표를 구하는 문제이다.
위에서 말한 절단한 넓이가 같아지는 좌표는 도심의 성질 중 하나이다.
다만, 저 조건을 만족하는 모든 도형이 도심을 가지는 것은 아니다.
삼각형은 위 조건을 만족하는 점이 존재하지 않는다.
'''

import sys

input = sys.stdin.readline

def shoelace_formula(N: int, graph: list) -> float:
    area = 0
    
    for i in range(N):
        j = (i+1) % N
        area += graph[i][0] * graph[j][1]
        area -= graph[i][1] * graph[j][0]
    
    return abs(area) / 2


def solve():
    if N == 3:
        return ['NA']
    A = shoelace_formula(N, point)

    C_x = 0
    for i in range(N):
        nextI = (i+1) % N
        C_x += (point[i][0] + point[nextI][0])*(point[i][0]*point[nextI][1] - point[nextI][0]*point[i][1])

    C_y = 0
    for i in range(N):
        nextI = (i+1) % N
        C_y += (point[i][1] + point[nextI][1])*(point[i][0]*point[nextI][1] - point[nextI][0]*point[i][1])


    C_x = C_x / (6*A)
    C_y = C_y / (6*A)

    return [C_x, C_y]


# main 함수 ----------
N = int(input())
point = []
for _ in range(N):
    point.append(tuple(map(int, input().split())))

print(*solve())