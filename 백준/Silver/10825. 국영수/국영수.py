# 백준 10825

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, data):
    data.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))
    return [x[0] for x in data]


def main():
    N = int(input())
    data = []
    for _ in range(N):
        name, a, b, c = map(str, input().decode().split())
        data.append([name, int(a), int(b), int(c)])
    for i in solve(N, data):
        print(i)


main()
