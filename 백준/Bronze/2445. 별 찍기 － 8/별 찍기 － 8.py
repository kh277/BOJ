# 백준 2445


import sys

input = sys.stdin.readline


def solve():
    result = []
    
    for i in range(1, N+1):
        temp = "*" * i
        temp += " " * (2*(N-i))
        temp += "*" * i
        result.append(temp)
    
    for i in range(N-1, 0, -1):
        temp = "*" * i
        temp += " " * (2*(N-i))
        temp += "*" * i
        result.append(temp)
    
    return result


# main 함수 ----------
N = int(input())

for i in solve():
    print(i)
