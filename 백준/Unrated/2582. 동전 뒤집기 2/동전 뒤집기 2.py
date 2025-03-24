# 백준 2582

import io
import random
from copy import deepcopy
from math import exp

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
DECREASE_RATE = 0.9998      # 감쇄율
BOLTZMANN_CONSTANT = 10     # 볼츠만 상수
MAX_EXPONENT = 700          # e^x를 계산하기 위한 값의 상한치
curTemperature = 1
limitTemperature = 0.0005



def scoring(coin):
    return sum(sum(x) for x in coin)


def move(N, coin):
    # revCol열 뒤집기
    revCol = int(random.randint(0, 32768)) % N
    for y in range(N):
        coin[y][revCol] ^= 1
    
    # 나머지 행에서 1이 과반수를 넘으면 뒤집기
    for y in range(N):
        if sum(coin[y])*2 > N:
            for x in range(N):
                coin[y][x] ^= 1
    
    return coin


def SimilatedAnnealing(N, coin):
    global curTemperature

    result = 1025
    while curTemperature > limitTemperature:
        curState = deepcopy(coin)

        # cur -> next 상태로 전이
        coin = move(N, coin)

        # 에너지 계산
        curEnergy = scoring(curState)
        nextEnergy = scoring(coin)

        # 전이 후 에너지가 낮을 경우 확률적으로 상태 전이
        if (nextEnergy - curEnergy) < 0:
            probability = exp(min(MAX_EXPONENT, (nextEnergy - curEnergy) / (BOLTZMANN_CONSTANT * curTemperature)))

            # 랜덤한 확률로 상태 전이
            if (probability > random.random()):
                coin = curState

        # 온도 감률 적용
        curTemperature *= DECREASE_RATE
        result = min(result, scoring(coin))

    return result


def main():
    N = int(input())
    coin = []
    for _ in range(N):
        coin.append(list(map(str, input().decode().rstrip())))
    for y in range(N):
        for x in range(N):
            coin[y][x] = 1 if coin[y][x] == 'T' else 0
    print(SimilatedAnnealing(N, coin))


main()