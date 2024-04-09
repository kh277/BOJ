# 백준 2166

'''
다각형을 이루는 순서대로 점의 좌표가 주어진다.
N1, N2, ... Ni라고 할 때, N1N2N3, N1N3N4, N1N4N5, ... 로 삼각형을 만들고
각각의 넓이를 구해 하나로 합쳐 결과를 출력한다.

넓이를 구할 때는 신발끈 공식을 이용하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, graph: list) -> float:
    area = 0
    
    for i in range(N):
        j = (i+1) % N
        area += graph[i][0] * graph[j][1]
        area -= graph[i][1] * graph[j][0]
    
    return round(abs(area) / 2, 1)


def main():
    N = int(input())
    graph = []

    for i in range(N):
        graph.append(tuple(map(float, input().split())))
    
    print(solve(N, graph))


main()
