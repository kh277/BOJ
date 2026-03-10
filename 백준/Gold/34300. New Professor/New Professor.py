# 백준 34300

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    count = 0
    heapq.heapify(A)
    while True:
        if len(A) < 5:
            break

        T = []
        for _ in range(5):
            T.append(heapq.heappop(A)+1)
            count += 1
        for i in T:
            if i < 0:
                heapq.heappush(A, i)

    return count + len(A)


def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(-int(input()))
    print(solve(N, A))


main()
