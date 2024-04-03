# 백준 29196

import sys

input = sys.stdin.readline

def solve(k: int) -> int:
    temp = k[2:]
    length = len(k)

    return [temp, '1' + '0'*(length-2)]

def main():
    k = input().rstrip()
    print("YES")
    print(*solve(k))

main()