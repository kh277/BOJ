# 백준 14168

'''
DP[i][j][k] = H소는 i번째까지, G소는 j번째까지 탐색했고 현재 k소 위치에 있을 때, 이동한 최소 거리
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**12


def getDist(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


def solve(H, G, cowH, cowG):
    DP = [[[INF, INF] for _ in range(G+1)] for _ in range(H+1)]
    DP[1][0][0] = 0

    for curH in range(1, H+1):
        for curG in range(G+1):

            # curH-1소 -> curH소
            DP[curH][curG][0] = min(DP[curH][curG][0], DP[curH-1][curG][0]+getDist(cowH[curH-2], cowH[curH-1]))

            # curG소 -> curH소
            DP[curH][curG][0] = min(DP[curH][curG][0], DP[curH-1][curG][1]+getDist(cowH[curH-1], cowG[curG-1]))

            if curG > 0:
                # curG-1소 -> curG소
                DP[curH][curG][1] = min(DP[curH][curG][1], DP[curH][curG-1][1]+getDist(cowG[curG-2], cowG[curG-1]))

                # curH소 -> curG소
                DP[curH][curG][1] = min(DP[curH][curG][1], DP[curH][curG-1][0]+getDist(cowH[curH-1], cowG[curG-1]))

    return DP[H][G][0]


def main():
    H, G = map(int, input().split())
    cowH = []
    cowG = []
    for _ in range(H):
        cowH.append(list(map(int, input().split())))
    for _ in range(G):
        cowG.append(list(map(int, input().split())))

    print(solve(H, G, cowH, cowG))


main()
