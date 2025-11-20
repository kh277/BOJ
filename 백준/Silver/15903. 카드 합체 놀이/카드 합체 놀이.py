# 백준 15903

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A):
    heapq.heapify(A)
    for _ in range(M):
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        add = a+b
        heapq.heappush(A, add)
        heapq.heappush(A, add)
    
    return sum(A)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))


main()
