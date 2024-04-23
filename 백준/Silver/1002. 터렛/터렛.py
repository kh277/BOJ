# 백준 1002

'''
(x1, y1)을 중심으로 하고 반지름이 r1인 원을 A,
(x2, y2)를 중심으로 하고 반지름이 r2인 원을 B,
(x1, y1) ~ (x2, y2)까지의 거리를 L이라고 하자.

가능한 경우의 수는 다음과 같다
1. 두 원이 만나지 않는 경우
1-1: L > r1 + r2 (일반적인 경우)
1-2: L < |r1 - r2| (한 원의 내부에 다른 원이 있고 만나지 않는 경우)

2. 두 원이 한 점에서 만나는 경우
2-1: L = r1 + r2 (일반적인 경우)
2-2: L = |r1 - r2| (한 원 내부에 다른 원이 있고 한 점에서 만나는 경우)

3. 두 원이 서로 다른 두 점에서 만나는 경우
3-1: L < r1 + r2 (일반적인 경우)

4. 두 원이 매우 많은 점에서 만나는 경우
4: L = 0 and r1 = r2 (두 원이 일치하는 경우)
'''


import sys
import math

input = sys.stdin.readline


def solve(A: list, B: list) -> int:
    L = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

    # 4. 두 원이 매우 많은 점에서 만나는 경우
    if L == 0 and A[2] == B[2]:
        return -1

    # 2. 두 원이 한 점에서 만나는 경우
    # 부동소수점 오차를 제거하기 위해 10e-6 이하인 경우에만 일치 판정
    elif abs(L - (A[2]+B[2])) < 10e-6 or abs(L - abs(A[2]-B[2])) < 10e-6:
        return 1
    
    # 1. 두 원이 만나지 않는 경우
    elif L > A[2]+B[2] or L < abs(A[2]-B[2]):
        return 0
    
    # 3. 두 원이 서로 다른 두 점에서 만나는 경우
    else:
        return 2


def main():
    T = int(input())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(solve([x1, y1, r1], [x2, y2, r2]))


main()