# 백준 1263

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tasks):
    tasks.sort(key= lambda x: (x[1], x[0]))

    curTime = 1000000
    for i in range(N-1, -1, -1):
        curT, curD = tasks[i]
        if curTime >= curD:
            curTime = curD - curT
        else:
            curTime = curTime - curT
    
    if curTime < 0:
        return -1
    return curTime


def main():
    N = int(input())
    tasks = []
    for _ in range(N):
        tasks.append(list(map(int, input().split())))

    print(solve(N, tasks))


main()
