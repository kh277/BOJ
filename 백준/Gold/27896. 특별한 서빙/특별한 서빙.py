# 백준 27896

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, satis):
    q = []

    count = 0
    accSum = 0
    for i in range(N):
        heapq.heappush(q, -satis[i])
        accSum += satis[i]
        if accSum >= M:
            accSum -= (-2) * heapq.heappop(q)
            count += 1

    return count


def main():
    N, M = map(int, input().split())
    satis = list(map(int, input().split()))
    print(solve(N, M, satis))


main()
