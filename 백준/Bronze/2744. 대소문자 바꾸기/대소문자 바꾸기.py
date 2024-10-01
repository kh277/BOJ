# 백준 2744


import sys

input = sys.stdin.readline


def solve():
    result = ""
    for i in string:
        if i.isupper() == True:
            result += i.lower()
        else:
            result += i.upper()
    
    return result


# main 함수 ----------
string = input().rstrip()

print(solve())
