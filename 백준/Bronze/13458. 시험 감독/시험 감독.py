# 백준 13458


import sys

input = sys.stdin.readline


def solve() -> int:
    result = 0
    
    # 총감독관 감독
    for i in range(N):
        A[i] = max(A[i] - B, 0)
        result += 1
    
    # 부감독관 감독
    for i in range(N):
        if A[i] % C == 0:
            result += A[i] // C
        else:
            result += A[i] // C + 1
    
    return result


# main 함수 ----------
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

print(solve())
