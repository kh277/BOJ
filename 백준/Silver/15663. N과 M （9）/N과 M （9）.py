# 백준 15663

import io
import itertools

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, A):
    result = set()
    for i in itertools.permutations(A, M):
        result.add(i)
    
    return sorted(result)


def main():
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    for i in solve(N, M, A):
        print(*i)


main()
