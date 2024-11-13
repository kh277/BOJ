# 백준 9710

'''
N*N 크기의 체스판에 룩이 N개 놓여 있을 때,
룩을 이동시켜 서로를 공격할 수 없는 상태로 만들기 위한 최소 이동 횟수를 구해야 한다.
룩은 한 번에 상하좌우 중 한 방향으로 한 칸씩 이동해야 한다.

x좌표 증가하는 순서대로 정렬하여 1~N까지의 수를 할당하고,
y좌표 증가하는 순서대로 정렬하여 1~N까지의 수를 할당한다.
'''

import sys

input = sys.stdin.readline

def solve(N, point):
    result = 0

    for case in range(2):
        point.sort(key= lambda x: x[case])
        for i in range(N):
            result += abs(i+1 - point[i][case])
    
    return result


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    point = []
    for _ in range(N):
        point.append(list(map(int, input().split())))
    print("Case #{a}: {b}".format(a=i, b=solve(N, point)))
