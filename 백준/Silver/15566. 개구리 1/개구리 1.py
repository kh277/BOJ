# 백준 29791

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def setFrog(N, M, interest, favorite, edge, status):
    flower = array('i', [-1]) * N     # 연못에 배치할 개구리 번호

    # 개구리가 좋아하는 연꽃에 flower에 배치
    for curFrog in range(N):
        curFlag = bool(status & (1<<curFrog))

        # 이미 다른 개구리가 배치되어 있는 경우
        if flower[favorite[curFrog][curFlag]-1] != -1:
            return [False, []]

        # status가 0이면 선호하는 첫 번째 연꽃에, 1이면 두 번째 연꽃에 개구리 배치
        flower[favorite[curFrog][bool(status & (1<<curFrog))]-1] = curFrog

    # 모든 통나무에 대해 확인
    for s, e, typeF in edge:
        if interest[flower[s-1]][typeF-1] != interest[flower[e-1]][typeF-1]:
            return [False, []]

    return [True, [i+1 for i in flower]]


def solve(N, M, interest, favorite, edge):
    # 개구리를 배치할 수 있는 모든 상태에 대해 처리
    for status in range(1<<N):
        result, flower = setFrog(N, M, interest, favorite, edge, status)
        if result == True:
            return [['YES'], flower]
    return [['NO']]


def main():
    N, M = map(int, input().split())
    interest = []
    for _ in range(N):
        interest.append(list(map(int, input().split())))
    favorite = []
    for _ in range(N):
        favorite.append(list(map(int, input().split())))
    edge = []
    for _ in range(M):
        edge.append(list(map(int, input().split())))

    for i in solve(N, M, interest, favorite, edge):
        print(*i)


main()
