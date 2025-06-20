# 백준 12910

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, candy):
    result = 0
    brand = [0 for _ in range(51)]
    for i in candy:
        brand[i] += 1

    result += brand[1]
    before = brand[1]
    for i in range(2, 51):
        if brand[i] == 0:
            break
        before *= brand[i]
        result += before

    return result


def main():
    N = int(input())
    candy = list(map(int, input().split()))
    print(solve(N, candy))


main()
