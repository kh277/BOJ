# 백준 2582

import io
import random
from math import exp
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

DECREASE_RATE = 0.9999      # 감쇄율
BOLTZMANN_CONSTANT = 10     # 볼츠만 상수
MAX_EXPONENT = 700          # e^x를 계산하기 위한 값의 상한치
curT = 1                    # 시작 온도
limitT = 0.0005             # 임계 온도


def scoring(coin):
    return sum(coin)


def move(N, coin):
    # 랜덤하게 세로줄 뒤집기
    revCol = int(random.randint(0, 32768)) % N
    for y in range(N):
        coin[y*N + revCol] ^= 1
    
    # 1이 과반수를 넘으면 가로줄이 있으면 뒤집기
    for y in range(N):
        curRow = coin[y*N:(y+1)*N]
        if sum(curRow)*2 > N:
            coin[y*N:(y+1)*N] = array('I', [x^1 for x in curRow])

    return coin


def SimilatedAnnealing(N, coin):
    global curT

    result = 1025
    # 임계 온도에 도달할 때까지 반복
    while curT > limitT:
        curState = coin[:]

        # 다음 상태로 전이 및 에너지 계산
        nextState = move(N, coin)
        curEnergy = scoring(curState)
        nextEnergy = scoring(nextState)

        # 랜덤한 확률로 상태 전이
        # 에너지가 커진다면 거의 무조건 전이, 에너지가 작아진다면 확률적으로 전이
        probability = exp(min(MAX_EXPONENT, (curEnergy - nextEnergy) / (BOLTZMANN_CONSTANT * curT)))
        if (probability >= random.random()):
            coin = nextState
        else:
            coin = curState

        # 온도 감률 적용
        curT *= DECREASE_RATE
        result = min(result, scoring(coin))

    return result


def main():
    N = int(input())
    coin = array('I')
    for _ in range(N):
        string = input().decode().rstrip()
        for ch in string:
            coin.append(1 if ch == 'T' else 0)

    result = 1025
    # 담금질 기법 1000회 시행
    for _ in range(1000):
        result = min(result, SimilatedAnnealing(N, coin[:]))
    print(result)


main()