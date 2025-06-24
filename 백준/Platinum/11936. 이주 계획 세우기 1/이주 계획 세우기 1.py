# 백준 11938

'''
N개의 정점을 L개의 좌표로 이동시킬 때, M개의 간선이 이루는 교차점의 개수를 최소화하는 것이 목표이다.
score() : 선분 교차점의 개수
move() : 랜덤하게 두 정점의 좌표 교환
'''

import io
import random
from math import exp
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8

DECREASE_RATE = 0.9995      # 감쇄율
BOLTZMANN_CONSTANT = 10     # 볼츠만 상수
MAX_EXPONENT = 700          # e^x를 계산하기 위한 값의 상한치
curT = 1                    # 시작 온도
limitT = 0.0005             # 임계 온도


# 선분 교차 판정 서브 함수1
def CCW(A, B, C):
    result = A[0]*B[1] + B[0]*C[1] + C[0]*A[1]
    result -= B[0]*A[1] + C[0]*B[1] + A[0]*C[1]
    return (result > 0) - (result < 0)


# 선분 교차 판정
def LineIntersection(A, B, C, D):
    ab = CCW(A, B, C) * CCW(A, B, D)
    cd = CCW(C, D, A) * CCW(C, D, B)

    return ab < 0 and cd < 0


# 에너지 체크 함수 : 각 나라를 pos에 저장된 정점에 할당 후 교차점 개수 세기
def scoring(pos, edge, point):
    cross = 0
    for i in range(len(edge)):
        A = pos[edge[i][0]]
        B = pos[edge[i][1]]
        for j in range(i+1, len(edge)):
            C = pos[edge[j][0]]
            D = pos[edge[j][1]]
            if LineIntersection(point[A], point[B], point[C], point[D]):
                cross += 1

    return cross


# 전이 함수 : 랜덤하게 두 거주지를 교환
def move(locate1, locate2, locate, country):
    country1 = country[locate1]
    country2 = country[locate2]

    country[locate1], country[locate2] = country2, country1
    if country1 != -1:
        locate[country1] = locate2
    if country2 != -1:
        locate[country2] = locate1


def SimilatedAnnealing(N, L, edge, point):
    global curT

    locate = array('i', [i for i in random.sample(range(L), N)])     # locate[i] = i번 나라가 할당된 거주지의 번호
    country = array('i',  [-1]) * L     # country[i] = i번 거주지에 할당된 나라의 번호
    for i in range(N):
        country[locate[i]] = i

    score = INF
    # 임계 온도에 도달할 때까지 반복
    while curT > limitT:
        curEnergy = scoring(locate, edge, point)

        # 전이 : 랜덤하게 두 도시를 뽑아 교환
        locate1, locate2 = random.sample(range(L), 2)
        move(locate1, locate2, locate, country)

        # 전이 후 에너지 계산
        nextEnergy = scoring(locate, edge, point)

        # 랜덤한 확률로 상태 전이
        # 에너지가 커진다면 거의 무조건 전이, 에너지가 작아진다면 확률적으로 전이
        probability = exp(min(MAX_EXPONENT, (curEnergy - nextEnergy) / (BOLTZMANN_CONSTANT * curT)))
        if (probability < random.random()):
            move(locate1, locate2, locate, country)
        else:
            score = min(score, nextEnergy)

        # 온도 감률 적용 및 에너지 계산
        curT *= DECREASE_RATE

    return [i+1 for i in locate]


def main():
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        a, b = map(int, input().split())
        edge.append([a-1, b-1])
    
    L = int(input())
    point = []
    for _ in range(L):
        point.append(list(map(int, input().split())))
    
    for i in SimilatedAnnealing(N, L, edge, point):
        print(i)


main()
