# 백준 1251

import sys

input = sys.stdin.readline


def solve():
    result = string[0]+string[1]+string[2:][::-1]
    for i in range(1, len(string)-1):
        for j in range(i+1, len(string)):
            temp = string[:i][::-1] + string[i:j][::-1] + string[j:][::-1]
            if temp < result:
                result = temp
    
    return result


# main 함수 ----------
string = input().rstrip()

print(solve())