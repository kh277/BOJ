# 백준 20209

import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 5


def solve(N, K, start, switch):
    END_STATUS = set(tuple([i]*N) for i in range(MOD))
    q = deque()
    q.append([start, 0])       # [현재 상태, 스위치를 누를 횟수]
    visited = set()
    visited.add(start)

    while q:
        curStatus, count = q.popleft()

        if curStatus in END_STATUS:
            return count

        for i in range(K):
            nextStatus = tuple((switch[i][j] + curStatus[j]) % MOD for j in range(N))
            if nextStatus not in visited:
                visited.add(nextStatus)
                q.append([nextStatus, count+1])

    return -1


def main():
    N, K = map(int, input().split())
    num = tuple(map(int, input().split()))
    switch = []
    for i in range(K):
        temp = list(map(int, input().split()))
        temp2 = array('I', [0]) * N
        for j in range(temp[0]):
            temp2[temp[j+1]-1] += i+1
        switch.append(temp2)

    print(solve(N, K, num, switch))


main()
