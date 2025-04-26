# 백준 7983

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, task):
    task.sort(key= lambda x: (-x[1], x[0]))

    deadline = task[0][1]
    index = 0

    # 마감 시간이 긴 작업부터 스케줄링
    while index < N:
        curD, curT = task[index]

        if curT < deadline:
            deadline = curT
            continue

        deadline -= curD
        index += 1
    
    return deadline


def main():
    N = int(input())
    task = []
    for _ in range(N):
        task.append(list(map(int, input().split())))
    print(solve(N, task))


main()
