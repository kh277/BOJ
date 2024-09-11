# 백준 2739

import sys

input = sys.stdin.readline


def solve(N: int) -> int:
    result = []
    for i in range(1, 10):
        temp = str(N) + " * " + str(i) + " = " + str(N*i)
        result.append(temp)
    
    return result


def main():
    N = int(input())
    
    for i in solve(N):
        print(i)


main()