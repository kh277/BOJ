# 백준 1374

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    data.sort(key= lambda x: (x[0], x[1]))

    pq = [0]
    for i in range(N):
        curS, curE = data[i]
        leastRoom = heapq.heappop(pq)
        if curS >= leastRoom:
            heapq.heappush(pq, curE)
        else:
            heapq.heappush(pq, leastRoom)
            heapq.heappush(pq, curE)
        
    return len(pq)


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split()))[1:])
    print(solve(N, data))


main()
