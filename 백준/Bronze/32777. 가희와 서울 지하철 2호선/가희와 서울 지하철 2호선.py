# 3번

import sys

input = sys.stdin.readline


def solve(start, end):
    if start < end:
        innerCycle = end - start + 1
        outerCycle = 243 - end + 1 + start - 201 + 1
    else:
        innerCycle = 243 - start + 1 + end - 201 + 1
        outerCycle = start - end + 1

    if innerCycle < outerCycle:
        return "Inner circle line"
    elif innerCycle > outerCycle:
        return "Outer circle line"
    else:
        return "Same"


# main 함수 ----------
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(solve(a, b))