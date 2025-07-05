# 백준 31962

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, X, bus):
    late = -1

    for i in range(N):
        if sum(bus[i]) <= X:
            late = max(late, bus[i][0])
    
    return -1 if late == -1 else late


def main():
    N, X = map(int, input().split())
    bus = []
    for _ in range(N):
        bus.append(list(map(int, input().split())))
    print(solve(N, X, bus))


main()
