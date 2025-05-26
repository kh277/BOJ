# 백준 14650

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
result = 0


def recur(depth, num, accSum):
    global result

    if depth == 0:
        if accSum % 3 == 0:
            result += 1
        return

    if depth == 1:
        for i in range(1, 3):
            recur(depth-1, num + [i], accSum+i)
    else:
        for i in range(3):
            recur(depth-1, num + [i], accSum+i)


def main():
    N = int(input())
    recur(N, [], 0)
    print(result)


main()
