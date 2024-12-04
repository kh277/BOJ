# 백준 1259

import sys

input = sys.stdin.readline


def solve():
    length = len(string)
    for i in range(length):
        if string[i] != string[length-1-i]:
            return 'no'
    return 'yes'


# main 함수 ----------
while True:
    string = input().rstrip()
    if string == '0':
        break
    print(solve())
