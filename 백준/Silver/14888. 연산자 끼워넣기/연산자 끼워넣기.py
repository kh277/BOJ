# 백준 14888번

import sys
input = sys.stdin.readline


def DFS(N: int, A: list, op: list) -> list:
    maximum = -1000000001
    minimum = 1000000001

    # 어떤 연산자라도 음수가 생긴 경우 -> 유효하지 않은 연산
    if any(i < 0 for i in op):
        return [maximum, minimum]

    # 연산할 숫자가 하나만 남은 경우
    if N == 1:
        return [A[0], A[0]]

    # DFS를 통해 연산 값 추출
    temp = [DFS(N - 1, [A[0] + A[1]] + A[2:], [op[0] - 1, op[1], op[2], op[3]]),
            DFS(N - 1, [A[0] - A[1]] + A[2:], [op[0], op[1] - 1, op[2], op[3]]),
            DFS(N - 1, [int(A[0] * A[1])] + A[2:], [op[0], op[1], op[2] - 1, op[3]]),
            DFS(N - 1, [int(A[0] / A[1])] + A[2:], [op[0], op[1], op[2], op[3] - 1])]

    # 최대값, 최소값 추출
    for i in temp:
        if i[0] > maximum:
            maximum = i[0]
        if i[1] < minimum:
            minimum = i[1]

    return [maximum, minimum]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    op = list(map(int, input().split()))

    for i in DFS(N, A, op):
        print(i)

main()
