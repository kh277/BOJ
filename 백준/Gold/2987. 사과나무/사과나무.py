# 백준 2987

'''
점 P가 삼각형 ABC 내부에 존재한다면,
넓이 ABC = 넓이PAB + 넓이 PBC + 넓이 PCA를 만족해야 한다.
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


def solve(triangle: list, apple: list) -> list:

    count = 0
    S = shoelace_formula(3, [triangle[0], triangle[1], triangle[2]])
    for i in apple:
        
        A = shoelace_formula(3, [i, triangle[0], triangle[1]])
        B = shoelace_formula(3, [i, triangle[1], triangle[2]])
        C = shoelace_formula(3, [i, triangle[2], triangle[0]])

        if S == A + B + C:
            count += 1

    return [round(S, 1), count]


def main():
    triangle = []
    apple = []
    for i in range(3):
        triangle.append(tuple(map(int, input().split())))
    
    N = int(input())
    for i in range(N):
        apple.append(tuple(map(int, input().split())))
    
    for i in solve(triangle, apple):
        print(i)


main()