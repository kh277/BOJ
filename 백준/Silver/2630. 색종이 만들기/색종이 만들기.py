# 백준 2630

'''
파란색 색종이와 흰색 색종이의 개수를 구해야 하므로 분할 정복을 이용하자.
'''

import sys

input = sys.stdin.readline


def solve(N: int, graph: list) -> list:

    # 더 분할할 수 없는 경우
    if N == 1:
        if graph[0][0] == 1:
            # 흰색, 파란색 순서로 저장
            return [0, 1]
        else:
            return [1, 0]
    
    # graph의 원소가 전부 1인 경우
    if all(all(j == 1 for j in i) for i in graph):
        return [0, 1]
    
    # graph의 원소가 전부 0인 경우
    if all(all(j == 0 for j in i) for i in graph):
        return [1, 0]
    
    # graph를 4등분하여 분할 정복
    A = solve(N//2, [i[:N//2] for i in graph[:N//2]])
    B = solve(N//2, [i[N//2:] for i in graph[:N//2]])
    C = solve(N//2, [i[:N//2] for i in graph[N//2:]])
    D = solve(N//2, [i[N//2:] for i in graph[N//2:]])

    return [A[0]+B[0]+C[0]+D[0], A[1]+B[1]+C[1]+D[1]]

def main():
    N = int(input())
    graph = [None for _ in range(N)]

    for i in range(N):
        graph[i] = list(map(int, input().split()))

    for i in solve(N, graph):
        print(i)


main()