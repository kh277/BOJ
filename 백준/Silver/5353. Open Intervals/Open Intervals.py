# 백준 5353

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tasks):
    tasks.sort(key= lambda x: (x[1], x[0]))

    count = 0
    prevD = 0
    for i in range(N):
        curR, curD = tasks[i]
        if prevD <= curR:
            prevD = curD
            count += 1
    
    return count


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        tasks = []
        for _ in range(N):
            tasks.append(list(map(int, input().split())))

        print(solve(N, tasks))


main()
