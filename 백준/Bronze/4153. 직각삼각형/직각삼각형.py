# 백준 4153

import sys

input = sys.stdin.readline


def solve():
    L = [a, b, c]
    mid = L[:]
    mid.remove(max(mid))
    mid.remove(min(mid))

    if max(L)**2 == min(L)**2 + mid[0]**2:
        return 'right'
    else:
        return 'wrong'
    

# main 함수 ----------
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    print(solve())