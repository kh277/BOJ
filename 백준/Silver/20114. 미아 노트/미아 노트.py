# 백준 20114

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def findChar(string, sX, H, W):
    for y in range(H):
        for x in range(W):
            if string[y][sX+x] != '?':
                return string[y][sX+x]

    return '?'


def solve(N, H, W, string):
    result = []
    for x in range(0, N*W, W):
        result.append(findChar(string, x, H, W))
    
    return ''.join(result)


def main():
    N, H, W = map(int, input().split())
    string = []
    for _ in range(H):
        string.append(input().decode().rstrip())

    print(solve(N, H, W, string))


main()
