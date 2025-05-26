# 백준 31824

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(dic, string):
    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            cur = string[i:j+1]
            if cur in dic:
                result.append(dic[cur])
    
    return -1 if len(result) == 0 else ''.join(result)


def main():
    N, M = map(int, input().split())
    dic = dict()
    for _ in range(N):
        a, b = input().decode().split()
        dic[a] = b
    for _ in range(M):
        Q = input().decode().rstrip()
        print(solve(dic, Q))


main()
