# 백준 1436

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    result = set()
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    result.add(int(f"{a}666{b}{c}{d}"))
                    result.add(int(f"{a}{b}666{c}{d}"))
                    result.add(int(f"{a}{b}{c}666{d}"))
                    result.add(int(f"{a}{b}{c}{d}666"))

    result = sorted(list(result))
    return result[N-1]


def main():
    N = int(input())
    print(solve(N))


main()
