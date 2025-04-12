# 백준 15553

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, num):
    gap = []
    for i in range(1, N):
        heapq.heappush(gap, num[i]-num[i-1])
    
    result = N
    onCount = N
    while onCount > K:
        result += heapq.heappop(gap) - 1
        onCount -= 1
    
    return result


def main():
    N, K = map(int, input().split())
    num = []
    for _ in range(N):
        num.append(int(input()))
    
    print(solve(N, K, num))


main()