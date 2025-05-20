# 백준 26123

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, D, H):
    H.sort(reverse=True)

    maxH = max(H)
    afterH = max(0, maxH-D)
    result = 0
    for i in range(N):
        if H[i] > afterH:
            result += H[i] - afterH
    
    return result


def main():
    N, D = map(int, input().split())
    H = list(map(int, input().split()))
    print(solve(N, D, H))


main()
