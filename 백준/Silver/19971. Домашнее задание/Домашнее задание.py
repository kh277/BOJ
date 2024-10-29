# 백준 19971

'''
N개의 작업과 M개의 종속성이 주어지고,
작업을 하나만 제외할 때 작업을 완료할 때까지 걸리는 최소 시간을 구하는 문제이다.

a -> b와 같은 종속 관계가 있을 경우,
a를 작업에서 제외하면 b도 완료할 수 없게 되므로, 작업을 한 개만 제외할 수 없게 된다.
따라서 종속성의 시작에 있는 작업은 제외할 수 없게 된다.
'''

import sys

input = sys.stdin.readline
INF = 10e7


def solve():
    # 종속 관계가 있는 수 제외
    canExcept = set([i for i in range(1, N+1)])
    for i in sub:
        if i[0] in canExcept:
            canExcept.remove(i[0])

    # 숫자를 제외했을 때 최소 시간 계산
    result = INF
    sumData = sum(data)
    for i in canExcept:
        result = min(result, sumData-data[i-1])

    return result


# main 함수 ----------
N, M = map(int, input().split())
data = list(map(int, input().split()))
sub = []
for _ in range(M):
    sub.append(list(map(int, input().split())))

print(solve())