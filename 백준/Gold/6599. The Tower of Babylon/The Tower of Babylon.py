# 백준 6599

'''
DP[h][i] = 블럭이 h-1개 쌓여 있고, i번째 밑면까지 탐색했을 때, 쌓을 수 있는 최대 높이
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(square):
    square.sort()
    DP = [[0 for _ in range(len(square))] for _ in range(len(square))]
    for i in range(len(square)):
        DP[0][i] = square[i][2]

    for h in range(len(square)):
        for i in range(len(square)):
            curX, curY, _ = square[i]
            for j in range(len(square)):
                nextX, nextY, nextH = square[j]

                # square[i] 위에 square[j]가 올라갈 수 있는 경우
                if nextX < curX and nextY < curY:
                    DP[h][j] = max(DP[h][j], DP[h-1][i]+nextH)
                else:
                    DP[h][j] = max(DP[h][j], DP[h-1][j])

    return max(DP[-1])


def main():
    count = 1
    while True:
        N = int(input())
        if N == 0:
            break
        grid = set()
        for _ in range(N):
            x, y, z = map(int, input().split())
            grid.add((min(x, y), max(x, y), z))
            grid.add((min(y, z), max(y, z), x))
            grid.add((min(z, x), max(z, x), y))

        print(f"Case {count}: maximum height = {solve(list(grid))}")
        count += 1


main()
