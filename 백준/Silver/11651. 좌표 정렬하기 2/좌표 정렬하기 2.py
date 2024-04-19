# 백준 11651

'''
조건이 두 개 이상이므로 key= labmda를 이용하자.
'''

import sys

input = sys.stdin.readline


def solve(N: int, data: list) -> list:

    # y 증가순, x 증가순 정렬 
    data.sort(key= lambda x: (x[1], x[0]))

    return data


def main():
    N = int(input())

    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    for i in solve(N, data):
        print(*i)


main()