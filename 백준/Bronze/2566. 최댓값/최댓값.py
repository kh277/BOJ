# 백준 2738

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(data):
    maxD = [[-1], [0, 0]]
    for y in range(9):
        for x in range(9):
            if data[y][x] > maxD[0][0]:
                maxD[0][0] = data[y][x]
                maxD[1] = [y+1, x+1]
    
    return maxD


def main():
    data = []
    for i in range(9):
        data.append(list(map(int, input().split())))

    for i in solve(data):
        print(*i)


main()
