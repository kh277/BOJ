# 백준 1254


import sys

input = sys.stdin.readline


def is_Palin(string: str) -> bool:
    l = len(string)
    for i in range(l//2):
        if string[i] != string[-i-1]:
            return False
    
    return True


def solve() -> int:
    result = 100
    for i in range(1, len(S)+1):
        if is_Palin(S[-i:]) == True:
            result = min(result, (len(S)*2 - len(S[-i:])))
    
    return result


# main 함수 ----------
S = input().rstrip()

print(solve())
