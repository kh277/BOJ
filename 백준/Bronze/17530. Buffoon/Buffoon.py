# 백준 17530

import sys

input = sys.stdin.readline

def solve():
    carlos = candidate[0]
    
    for i in range(1, N):
        if carlos < candidate[i]:
            return 'N'
    
    return 'S'


# main 함수 ----------
N = int(input())
candidate = []
for _ in range(N):
    candidate.append(int(input()))

print(solve())
