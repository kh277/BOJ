# 백준 1480

'''
DLAS 휴리스틱을 사용하여 최적해를 탐색한다.
전략1. 두 보석을 서로 교환한다.
전략2. 가방에서 임의의 보석을 제거한다.
전략3. 임의의 가방에 할당되지 않은 제일 작은 보석을 추가한다.
'''

import io
import random

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

MEMORY_SIZE = 5     # 기억할 이전 상태의 개수
MAX_ITER = 1000   # 지역 최적해를 찾지 못했을 경우 탐색을 종료하는 기준점


# 점수 체크 함수
def scoring(status):
    result = 0
    for i in status:
        if i > -1 :
            result += 1

    return result


# 상태 변이 함수
def move(N, M, jewel, status, leftSize):
    r = int(random.randint(0, 100))
    before = []

    # (60%) 임의의 두 보석 교환
    if N >= 2 and r < 60:
        a, b = random.sample(range(N), 2)
        if status[a] != -1 and status[b] != -1:
            aLeft = leftSize[status[a]]
            bLeft = leftSize[status[b]]
            if aLeft + jewel[a] - jewel[b] >= 0 and bLeft + jewel[b] - jewel[a] >= 0:
                before.append([1, status[a], leftSize[status[a]]])
                before.append([1, status[b], leftSize[status[b]]])
                before.append([0, a, status[a]])
                before.append([0, b, status[b]])
                leftSize[status[a]] += jewel[a] - jewel[b]
                leftSize[status[b]] += jewel[b] - jewel[a]
                status[a], status[b] = status[b], status[a]

    # (20%) 가방에서 임의의 보석 제거
    elif r < 80:
        a = random.randint(0, N-1)
        if status[a] != -1:
            before.append([1, status[a], leftSize[status[a]]])
            before.append([0, a, status[a]])
            leftSize[status[a]] += jewel[a]
            status[a] = -1

    # (20%) 임의의 가방에 임의의 보석 추가
    else:
        cand = [i for i in range(N) if status[i] == -1]
        if len(cand) == 0:
            return []
        jewelI = random.choice(cand)

        canAdd = [i for i in range(M) if leftSize[i] >= jewel[jewelI]]
        if len(canAdd) == 0:
            return []
        bagI = random.choice(canAdd)

        before.append([1, bagI, leftSize[bagI]])
        before.append([0, jewelI, status[jewelI]])
        leftSize[bagI] -= jewel[jewelI]
        status[jewelI] = bagI

    return before


def DLAS(N, M, bag, jewel):
    status = [-1] * N
    leftSize = [i for i in bag]

    curScore = -scoring(status)
    bestScore = curScore

    memory = [curScore] * MEMORY_SIZE
    k = 0
    iterCount = 0
    count = 0

    while iterCount < MAX_ITER:
        prevScore = curScore

        # 현재 상태 백업 후 상태 변이
        before = move(N, M, jewel, status, leftSize)
        nextScore = -scoring(status)

        # 상태가 개선된 경우 최적해 갱신
        if nextScore < bestScore:
            iterCount = 0
            bestScore = nextScore

        # 수용 전략
        if nextScore == curScore or nextScore < max(memory):
            curScore = nextScore
        else:
            # 최적해 미갱신 시 이전 상태 복귀
            for i, a, b in before:
                if i == 0:
                    status[a] = b
                else:
                    leftSize[a] = b

		# 대체 전략
        if curScore > memory[k] or (curScore < memory[k] and curScore < prevScore):
            memory[k] = curScore

        k = (k+1) % MEMORY_SIZE
        iterCount += 1
        count += 1

    return -bestScore


def main():
    N, M, C = map(int, input().split())
    bag = [C] * M
    jewel = list(map(int, input().split()))

    print(max([DLAS(N, M, bag, jewel) for _ in range(20)]))


main()
