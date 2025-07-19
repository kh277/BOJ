# 백준 13411

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, robot):
    robot.sort(key= lambda x: ((x[1]**2+x[2]**2)**0.5/x[0], x[3]))
    return [i[3]+1 for i in robot]


def main():
    N = int(input())
    robot = []
    for i in range(N):
        x, y, v = map(int, input().split())
        robot.append((v, x, y, i))
    for i in solve(N, robot):
        print(i)


main()
