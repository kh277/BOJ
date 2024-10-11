# 백준 1748


import sys

input = sys.stdin.readline


def solve():
    length = len(str(N))
    
    coef = [0]
    for i in range(length-1):
        coef.append(coef[-1]*10 + 9)
        
    result = 0
    for i in range(1, length+1):
        if length >= i:
            result += i * min(N - coef[i-1], 9*10**(i-1))

    return result


# main 함수 ----------
N = int(input())

print(solve())
