# 백준 32759

'''
입력된 수열 num에서 가장 큰 수를 A, 두 번째로 큰 수를 B라고 할 때,
A, B가 양수일 때, 음수일 때를 따로 분리해서 세보자.
'''

import sys

input = sys.stdin.readline
MOD = 1000000007


def solve():
    num.sort()
    A = num[-1]
    B = num[-2]

    # 1. A, B 둘 다 양수인 경우
    if A >= 0 and B >= 0:
        for _ in range(N):
            temp = B
            B = A
            A = (A+temp) % MOD

    # 2. A가 양수이고 B가 음수인 경우
    elif A > 0 and B < 0:
        changeIndex = int(-B/A)+1
        # N번 이내에 B가 양수가 되는 경우
        if changeIndex < N:
            B = A*changeIndex + B
            for _ in range(changeIndex, N):
                temp = B
                B = A
                A = (A+temp) % MOD
        else:
            A = num[-1]*N + num[-2]

    # 3. A, B 둘 다 음수인 경우
    else:
        A = A+B

    return (2*MOD+A) % MOD


# main 함수 ----------
N, M = map(int, input().split())
num = list(map(int, input().split()))
print(solve())