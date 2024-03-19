# 백준 2491

'''
LIS 문제와 비슷하지만 연속해야 한다는 차이가 있다.

1. 증가하는 경우
for문을 돌려서 이전 값보다 큰 경우 +1, 작아지는 경우 0으로 초기화

2. 감소하는 경우
for문을 돌려서 이전 값보다 작은 경우 +1, 커지는 경우 0으로 초기화

두 가지 경우를 모두 보고 가장 큰 값을 세면 된다.
'''

import sys

input = sys.stdin.readline


def maxInc(N: int, A: list) -> int:
    # 증가부분
    inc = 1
    inc_temp = 1
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            inc_temp = 0
        inc_temp += 1
        if inc < inc_temp:
            inc = inc_temp

    return inc


def solve(N: int, A: list) -> int:
    return max(maxInc(N, A), maxInc(N, list(reversed(A))))


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))


main()
