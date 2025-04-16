# 백준 1063

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
movePos = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0], \
    'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}


def move(posK, posS, curMove):
    nextKX = posK[1] + curMove[1]
    nextKY = posK[0] + curMove[0]

    # 킹이 체스판을 빠져나가지 않을 경우
    if 0 <= nextKX < 8 and 0 <= nextKY < 8:
        # 킹이 돌이 있는 위치로 이동할 경우
        if nextKX == posS[1] and nextKY == posS[0]:
            nextSX = posS[1] + curMove[1]
            nextSY = posS[0] + curMove[0]
            # 돌이 체스판을 빠져나가지 않을 경우
            if 0 <= nextSX < 8 and 0 <= nextSY < 8:
                return [[nextKY, nextKX], [nextSY, nextSX]]
        # 킹이 돌이 있지 않은 위치로 이동할 경우
        else:
            return [[nextKY, nextKX], posS]

    return [posK, posS]


def main():
    K, S, N = map(str, input().decode().rstrip().split())
    posK = [8-int(K[1]), ord(K[0])-ord('A')]
    posS = [8-int(S[1]), ord(S[0])-ord('A')]

    for _ in range(int(N)):
        curMove = input().decode().rstrip()
        posK, posS = move(posK, posS, movePos[curMove])

    K = chr(posK[1] + ord('A')) + str(8-posK[0])
    S = chr(posS[1] + ord('A')) + str(8-posS[0])
    print(K)
    print(S)


main()
