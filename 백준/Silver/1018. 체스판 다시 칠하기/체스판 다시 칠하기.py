# 백준 1018

'''
브루트포스 문제이므로 단순 반복 시 들어가는 시간복잡도를 생각해보자.
MxN 보드에서 8x8 크기와 다른지 비교해야 하므로 (M-8+1)x(N-8+1)번 비교
시작점이 흰색인지 검은색인지 모르므로 x2
8x8에서 다른 갯수를 찾아야 하므로 8x8
= (M-7) x (N-7) x 128이 된다. 최악의 경우 M=50, N=50이므로,
42x42x128 = 2xxxxx이므로 2초 내에 해결 가능하다.
'''

from sys import stdin
from math import inf

input = stdin.readline

chess_a = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
]

chess_b = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
]


def solve(M: int, N: int, board: list) -> list:
    result = inf

    for i in range(M-7):
        for j in range(N-7):
            count = board_compare(i, j, board)
            if result > count:
                result = count

    return result


def board_compare(i: int, j: int, board: list):
    count_a = 0
    count_b = 0

    for x in range(8):
        for y in range(8):
            if board[i+x][j+y] != chess_a[x][y]:
                count_a += 1
            if board[i+x][j+y] != chess_b[x][y]:
                count_b += 1

    return min(count_a, count_b)


def main():
    M, N = map(int, input().split())

    board = [None for _ in range(M)]
    for i in range(M):
        board[i] = list(input().rstrip())

    print(solve(M, N, board))


main()
