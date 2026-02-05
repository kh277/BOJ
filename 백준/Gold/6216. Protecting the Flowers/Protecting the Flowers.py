# 백준 6216

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, cow):
    cow.sort(key= lambda x: (-x[1]/x[0]))

    leftCow = 0
    for i in range(N):
        leftCow += cow[i][1]

    result = 0
    for i in range(N):
        leftCow -= cow[i][1]
        result += leftCow * 2 * cow[i][0]

    return result


def main():
    N = int(input())
    cow = []
    for _ in range(N):
        cow.append(tuple(map(int, input().split())))
    print(solve(N, cow))


main()
