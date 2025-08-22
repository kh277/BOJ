# 백준 16376

import io
import math
import random
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

MEMORY_SIZE = 5     # 기억할 이전 상태의 개수
MAX_ITER = 50000     # 지역 최적해를 찾지 못했을 경우 탐색을 종료하는 기준점
END_SCORE = 0


# 점수 체크 함수
def scoring(N, edge, status):
    score = 0
    for i in range(N-1):
        curS, curE = edge[i]
        if math.gcd(status[curS-1], status[curE-1]) > 1:
            score += 1

    return score


def scoring(N, edge, status):
    score = 0
    for i in range(N-1):
        curS, curE = edge[i]
        if math.gcd(status[curS-1], status[curE-1]) > 1:
            score += 1

    return score


def DLAS(N, edge, status):
    curScore = scoring(N, edge, status)
    bestStatus = status.copy()
    bestScore = curScore

    memory = [curScore] * MEMORY_SIZE
    k = 0
    iterCount = 0

    # 목표에 도달할 때까지 반복
    while curScore > END_SCORE and iterCount < MAX_ITER:
        prevScore = curScore

        # 현재 상태 백업 후 상태 변이
        x1, x2 = random.sample(range(N), 2)
        status[x1], status[x2] = status[x2], status[x1]
        nextScore = scoring(N, edge, status)

        # 상태가 개선된 경우 최적해 갱신
        if nextScore < bestScore:
            bestStatus = status.copy()
            iterCount = 0
            bestScore = nextScore

        # 수용 전략
        if nextScore == curScore or nextScore < max(memory):
            curScore = nextScore
        else:
            status[x1], status[x2] = status[x2], status[x1]
            nextScore = curScore

		# 대체 전략
        if curScore > memory[k] or (curScore < memory[k] and curScore < prevScore):
            memory[k] = curScore

        k = (k+1) % MEMORY_SIZE
        iterCount += 1

    return bestStatus


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        edge = [array('I', [0]) * 2 for _ in range(N-1)]
        for i in range(N-1):
            u, v = map(int, input().split())
            edge[i][0] = u
            edge[i][1] = v
        status = [i for i in range(1, N+1)]
        print(*DLAS(N, edge, status))


main()
