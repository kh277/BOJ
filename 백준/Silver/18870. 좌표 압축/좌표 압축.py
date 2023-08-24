# 백준 18870

'''
좌표 압축 xi'은 xi보다 작은 수의 개수와 같아야 한다.
따라서 (값, 입력순서, 작은 수의 갯수) 순서로 튜플을 만들어 값 크기에 따라 정렬을 한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, arr: list) -> list:
    # 값 크기 역순대로 정렬
    arr.sort(key= lambda x: (x[0]))

    for i in range(1, N):
        if arr[i-1][0] == arr[i][0]:
            arr[i][2] = arr[i-1][2]
        else:
            arr[i][2] = arr[i-1][2] + 1

    # 다시 입력 순서대로 정렬
    arr.sort(key= lambda x: (x[1]))

    return arr


def main():
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        # (arr[i]값, 입력순서, 작은 수의 갯수) 순서로 데이터가 들어감.
        arr[i] = [arr[i], i, 0]

    for i in solve(N, arr):
        print(i[2], end=" ")


main()
