# 백준 6359

import sys

input = sys.stdin.readline


def solve():
    room = [0 for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i, N+1, i):
            room[j] = (room[j]+1)%2
    
    return sum(room)


# main 함수 ----------
T = int(input())
for _ in range(T):
    N = int(input())
    print(solve())