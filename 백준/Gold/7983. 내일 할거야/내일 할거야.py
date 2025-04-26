# 백준 7983

'''
마감 시간이 오래 남은 작업부터 앞쪽으로 스케줄링하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, task):
    task.sort(key= lambda x: -x[1])
    deadline = task[0][1]

    for i in range(N):
        curD, curT = task[i]
        if curT < deadline:
            deadline = curT
        deadline -= curD

    return deadline


def main():
    N = int(input())
    task = []
    for _ in range(N):
        task.append(list(map(int, input().split())))
    print(solve(N, task))


main()
