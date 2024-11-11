# 백준 7520

import sys
import math

input = sys.stdin.readline


# 반지름이 R이고, 각도가 A, B(A<B)인 점에서 할선 AB의 거리
# 제2 코사인법칙을 적용하여 계산함
def cosData(R, A, B):
    seta = min(B-A, -1 * (A-B)) * 2 * math.pi
    return math.sqrt(R**2 + R**2 - 2 * R**2 * math.cos(seta))


def solve(N, point):
    left = 0
    right = 1

    result = 0
    while right < N:
        leftPoint = point[left][0] / point[left][1]
        rightPoint = point[right][0] / point[right][1]

        result = max(result, cosData(N, leftPoint, rightPoint))

        # 투 포인터 적용
        if rightPoint - leftPoint >= 0.5:
            left += 1
        else:
            right += 1
        
    return "{:.2f}".format(round(result, 2))


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    point = []
    for _ in range(N):
        point.append(tuple(map(int, input().split())))
    print(f"Scenario #{i}:")
    print(solve(N, point))
    print()
