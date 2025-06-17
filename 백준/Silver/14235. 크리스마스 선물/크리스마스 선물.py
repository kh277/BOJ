# 백준 14235

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    pq = []
    for _ in range(N):
        A = list(map(int, input().split()))
        if A[0] == 0:
            if len(pq) == 0:
                print(-1)
            else:
                print(-heapq.heappop(pq))
        else:
            for i in range(1, A[0]+1):
                heapq.heappush(pq, -A[i])


main()
