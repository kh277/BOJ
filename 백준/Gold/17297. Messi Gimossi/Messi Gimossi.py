# 백준 17297

'''
DP[1] = 5
DP[2] = 13인 피보나치 수열이 2^30-1을 넘어가는 N은 40이다.
'''

import sys

input = sys.stdin.readline


def recur(N, DP, start, curIndex):
    # 종료조건
    if curIndex == 1:
        return 'Messi'[N-start]
    elif curIndex == 2:
        return 'Messi Gimossi'[N-start]

    # 분할정복
    if start <= N < start + DP[curIndex-1]:
        return recur(N, DP, start, curIndex-1)
    elif N == start + DP[curIndex-1]:
        return ' '
    else:
        return recur(N, DP, start+DP[curIndex-1]+1, curIndex-2)


def solve(N):
    DP = [0 for _ in range(41)]
    DP[1] = 5
    DP[2] = 13

    # 2^30-1까지의 DP값 계산
    breakPoint = 3
    for i in range(3, 41):
        DP[i] = DP[i-1] + DP[i-2] + 1
        if DP[i] > N:
            breakPoint = i
            break

    result = recur(N, DP, 0, breakPoint)
    return 'Messi Messi Gimossi' if result == ' ' else result


# main 함수 ----------
N = int(input())
print(solve(N-1))
