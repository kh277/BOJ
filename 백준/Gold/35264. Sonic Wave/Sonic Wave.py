# 백준 35264

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    result = []
    wave = [0, 0, 0, 0]

    for i in range(1, N+1):
        curT = i % 4
        need = A[i-1] - wave[curT]
        if need == 0:
            continue
        elif need < 0:
            result.append((i, -need, 1))
        else:
            result.append((i, need, 3))
        wave[curT] += need
        wave[(curT+2)%4] -= need

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)

    print(len(result))
    if len(result) > 0:
        for i in result:
            print(*i)


main()
