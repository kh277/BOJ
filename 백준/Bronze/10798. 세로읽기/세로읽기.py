# 백준 10798

import sys

input = sys.stdin.readline


def solve(string: str) -> str:
    result = ""
    
    max_len = 0
    for i in range(5):
        max_len = max(max_len, len(string[i]))
    
    for i in range(max_len):
        for j in range(5):
            try:
                result += string[j][i]
            except:
                continue
    
    return result


def main():
    string = []
    for _ in range(5):
        string.append(input().rstrip())
    
    print(solve(string))


main()