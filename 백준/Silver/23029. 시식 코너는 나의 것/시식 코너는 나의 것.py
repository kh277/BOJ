# 백준 31824

'''
DP[i] = i번 인덱스의 음식을 먹었을 때, 먹은 음식 개수의 최대값
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, food):
    DP = array('I', [0]) * (N)
    DP[0] = food[0]
    if N > 1:
        DP[1] = max(food[1], food[0]+food[1]//2)
    if N > 2:
        DP[2] = max(food[0]+food[2], food[1]+food[2]//2)

    for i in range(3, N):
        DP[i] = max(DP[i-4]+food[i-1]+food[i]//2, DP[i-3]+food[i-1]+food[i]//2, DP[i-3]+food[i], DP[i-2]+food[i])

    return max(DP[N-2], DP[N-1])


def main():
    N = int(input())
    food = array('I')
    for _ in range(N):
        food.append(int(input()))
    print(solve(N, food))


main()
