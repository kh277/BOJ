# 백준 1264

import sys

input = sys.stdin.readline
vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}


def solve():
    result = 0
    for i in string:
        if i in vowel:
            result += 1
    
    return result


# main 함수 ----------
while True:
    string = input().rstrip()
    if string == "#":
        break
    print(solve())