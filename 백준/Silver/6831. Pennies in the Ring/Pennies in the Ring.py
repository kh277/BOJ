# 백준 6831

'''
반지름이 N인 원 내부에 좌표가 전부 정수인 점이 몇 개 존재하는지를 구하는 문제이다.
'''

import sys

input = sys.stdin.readline


def solve(N):
    # x = 0이고 y > 0인 점의 개수 -> N개
    result = N

    # x = 1~N에 대해 y > 0인 점의 개수
    for x in range(1, N+1):
        result += int((N**2 - x**2)**0.5)
    
    # 사분면 4개 + (0, 0)
    return result * 4 + 1


# main 함수 ----------
while True:
    N = int(input())
    if N == 0:
        break

    print(solve(N))
