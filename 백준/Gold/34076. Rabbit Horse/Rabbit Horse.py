# 05화

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
STRING = "RabbitHorse"
SIZE = 11


def solve(N):
    sub = N//SIZE
    if sub == 0:
        return 'a' * N

    result = [sub for _ in range(SIZE)]
    for i in range(N%SIZE):
        result[(i+3)%SIZE] += 1

    return ''.join([STRING[i]*result[i] for i in range(SIZE)] )


def main():
    N = int(input())
    print(solve(N))


main()
