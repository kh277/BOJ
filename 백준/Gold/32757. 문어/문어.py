# G번

import sys

input = sys.stdin.readline


def solve():
    if N <= K:
        return 0

    # N이 홀수인 경우
    if N % 2 == 1:
        if K % 2 == 1:
            return N-1
        else:
            return N
    # N이 짝수인 경우
    else:
        return N


# main 함수 ----------
N, K = map(int, input().split())

print(solve())