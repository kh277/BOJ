# 백준 11279

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    pq = []
    for _ in range(N):
        a = int(input())
        if a == 0:
            if len(pq) == 0:
                print(0)
            else:
                print(-heapq.heappop(pq))
        else:
            heapq.heappush(pq, -a)


main()
