# 백준 2022

'''
두 빌딩 사이의 거리를 a라고 두면,
(sqrt(x^2-a^2) * sqrt(y^2-a^2)) / (sqrt(x^2-a^2) + sqrt(y^2-a^2)) = c이라는 식이 성립한다.

이 경우, 두 빌딩 사이의 거리는 위의 방정식을 성립시키는 a의 값이 된다.
이분 탐색으로 a를 근사하여 구하자. 
'''

import sys
import math

input = sys.stdin.readline
eps = 10e-7


def solve(X: float, Y: float, C: float) -> float:
    start = 0
    end = min(X, Y)
    mid = 0
    
    while end - start > eps:
        mid = (start + end) / 2
        
        # 방정식 계산
        A = math.sqrt(X**2-mid**2)
        B = math.sqrt(Y**2-mid**2)
        target = (A*B)/(A+B) - C

        # 탈출조건
        if abs(target) <= eps:
            break
        
        # 이분 탐색
        if target >= 0:
            start = mid
        else:
            end = mid
    
    return mid


def main():
    x, y, c = map(float, input().split())
    
    print(solve(x, y, c))


main()