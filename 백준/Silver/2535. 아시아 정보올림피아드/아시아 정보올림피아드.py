# 백준 2535

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    heapq.heapify(data)
    gold = heapq.heappop(data)
    silver = heapq.heappop(data)
    while True:
        bronze = heapq.heappop(data)
        if gold[1] == silver[1] and gold[1] == bronze[1]:
            continue
        break

    return [gold[1:], silver[1:], bronze[1:]]


def main():
    N = int(input())
    data = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        data.append([-c, a, b])
    for i in solve(N, data):
        print(*i)


main()
