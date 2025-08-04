# 백준 27041

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**5


def solve(goalX, maxLeap, cows):
    curX = 0
    count = 0
    while True:
        if curX == goalX:
            break

        for leap in range(maxLeap, 0, -1):
            nextX = curX+leap
            if nextX <= goalX and nextX not in cows:
                curX = nextX
                count += 1
                break

    return count


def main():
    E, L, B = map(int, input().split())
    cows = set()
    for _ in range(B):
        cows.add(int(input()))
    print(solve(E, L, cows))


main()
