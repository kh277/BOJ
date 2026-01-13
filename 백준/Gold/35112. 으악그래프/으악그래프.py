# 백준 35112

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(V, E, edge):
    if V >= E:
        return 'Yes'
    return 'No'


def main():
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        edge.append(list(map(int, input().split())))
    print(solve(V, E, edge))


main()
