# 백준 32291

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(num):
    result = set()
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            result.add(i)
            result.add(num//i)

    result = sorted(list(result))

    for i in range(len(result)-1, -1, -1):
        if result[i] >= num:
            result.pop()
        else:
            break
    return result


def main():
    N = int(input())

    print(*solve(N+1))


main()
