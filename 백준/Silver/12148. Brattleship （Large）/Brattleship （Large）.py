# 백준 12148

'''
12147과 동일
'''

import sys

input = sys.stdin.readline


def solve(case, R, C, W):
    score = 0

    if R > 1:
        score += (R-1) * (C//W)
    else:
        pass

    left = 0
    if W*2 > C:
        left = C
        pass
    else:
        temp = (C-W) // W
        score += temp
        left = C - temp*W

    score += W*2 - left

    if W == left:
        pass
    else:
        score += 1
        score += left - W

    return 'Case #{0}: {1}'.format(case, score)


def main():
    T = int(input())
    for case in range(1, T+1):
        R, C, W = map(int, input().split())

        print(solve(case, R, C, W))

main()
