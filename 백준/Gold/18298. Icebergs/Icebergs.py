# 백준 18298

'''
문제
N개의 다각형에 대해 각 다각형의 꼭짓점의 좌표가 주어질 때,
다각형의 총 넓이를 구하는 문제이다.

신발끈 공식을 이용하여 넓이를 구하자.
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


def solve(N: int, points: list) -> int:
    S = 0
    
    for i in points:
        count = len(i)
        S += shoelace_formula(count, i)

    return int(S)


def main():
    N = int(input())
    
    points = []
    for _ in range(N):
        P = int(input())
        temp = []
        for i in range(P):
            temp.append(list(map(int, input().split())))
        
        points.append(temp)

    print(solve(N, points))


main()