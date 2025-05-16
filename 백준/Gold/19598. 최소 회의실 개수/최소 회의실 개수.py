# 백준 19598

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tasks):
    tasks.sort(key = lambda x: (x[0], x[1]))
    result = 1
    pq = []
    heapq.heappush(pq, tasks[0][1])

    for i in range(1, N):
        curR, curD = tasks[i]
        near = heapq.heappop(pq)
        if near > curR:
            heapq.heappush(pq, near)
            result += 1
        heapq.heappush(pq, curD)

    return result


def main():
    N = int(input())
    tasks = []
    for _ in range(N):
        a, b = map(int, input().split())
        tasks.append((a, b))

    print(solve(N, tasks))


main()
