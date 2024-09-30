# 백준 31498

'''
x초일 때 토카의 위치 : (1/2)Kx^2 + (B+(1/2)K)x + A
x초일 때 돌돌이의 위치 : -Dx + (A+C)


주의 반례 :
10 20
0 10
10
-> -1

35 8
100 1
1
-> 7

9 5
100 1
2
-> 3
'''


import sys
import math

input = sys.stdin.readline


# Ax^2 + Bx + C = 0의 해 중 작은 쪽 반환
def qudratic(A, B, C):
    return ((-1)*B - math.sqrt(B**2 - 4*A*C)) / (2*A)


def solve() -> int:
    # 토카의 위치가 0에 도달할 수 없는 경우
    # (토카의 위치를 나타낸 이차방정식의 판별식 D < 0인 경우)
    if (2*B+K)**2 - 8*A*K < 0:
        return -1
    
    # 토카가 집에 도착하는 시간 구하기
    if K == 0:
        toka_home = A / B
    else:
        toka_home = qudratic(K/2, -K/2-B, A)
        
    # 돌돌이가 집에 도착하는 시간 구하기
    doldol_home = (A+C) / D
    
    # 토카와 돌돌이가 같은 점프횟수로 집에 도착하는 경우 -1 출력
    return -1 if math.ceil(toka_home) >= math.ceil(doldol_home) else math.ceil(toka_home)


# main 함수 ----------
A, B = map(int, input().split())
C, D = map(int, input().split())
K = int(input())

print(solve())