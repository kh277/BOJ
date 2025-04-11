# 백준 11830

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    dicX = dict()
    dicY = dict()

    for i in range(N):
        curX, curY = num[i]
        if curX not in dicX:
            dicX[curX] = 1
        else:
            dicX[curX] += 1
        if curY not in dicY:
            dicY[curY] = 1
        else:
            dicY[curY] += 1

    result = 0
    for i in range(N):
        curX, curY = num[i]
        result += (dicX[curX]-1) * (dicY[curY]-1)

    return result


def main():
    N = int(input())
    num = []
    for _ in range(N):
        num.append(list(map(int, input().split())))

    print(solve(N, num))


main()
