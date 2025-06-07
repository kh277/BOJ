# 백준 11508

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, cost):
    cost.sort()

    result = sum(cost[0:N%3])
    for i in range(N%3, N, 3):
        result += cost[i+1] + cost[i+2]

    return result


def main():
    N = int(input())
    cost = []
    for _ in range(N):
        cost.append(int(input()))

    print(solve(N, cost))


main()
