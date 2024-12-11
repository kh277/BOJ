# 백준 32933

'''
DP[i] = i일까지 식물을 재배했을 때, 얻을 수 있는 최대 이익.
바텀업 DP를 이용해 k일에 새로 식물을 심는다고 가정하여 DP 테이블을 갱신해준다.
'''

import sys

input = sys.stdin.readline


def solve():
    DP = [0 for _ in range(M+1)]

    # 1 ~ M일까지 탐색
    for day in range(M+1):
        for fruitType in range(K):
            grow = fruit[fruitType][0]
            reGrow = fruit[fruitType][1]
            getCost = fruit[fruitType][2]

            # day날에 식물 fruitType을 새로 심을 때, 이후 날짜에 대한 최적값 탐색
            for i in range(day, M+1):
                if day+grow > i:
                    DP[i] = max(DP[i], DP[day])
                else:
                    DP[i] = max(DP[i], DP[day]+((i-grow-day)//reGrow + 1)*getCost)

    # N개의 밭에 대해 같은 작업 반복
    return DP[M] * N


# main 함수 ----------
N, M, K = map(int, input().split())
fruit = []
for _ in range(K):
    fruit.append(list(map(int, input().split())))

print(solve())