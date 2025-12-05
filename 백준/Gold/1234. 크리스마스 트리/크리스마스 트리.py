# 백준 1234

'''
DP[i][j][k] = 1~i층을 꾸밀 때 사용한 빨강이 j개, 초록이 k개일 때의 경우의 수.
파랑의 개수는 현재 층의 위치와 사용한 빨강, 초록의 개수에 따라 자동적으로 고정됨.
또한, DP[i]를 계산하기 위해 DP[i-1]만 가져다 쓰므로 한 차원 더 줄일 수 있음.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
C = [[], [], [2], [0, 6], [6], [], [20, 90], [], [70], [0, 1680], [252]]


def solve(N, R, G, B):
    # 색이 부족한 경우
    if R+G+B < N*(N+1)//2:
        return 0

    prevDP = [[0 for _ in range(G+1)] for _ in range(R+1)]
    if B > 0:
        prevDP[0][0] = 1
    if G > 0:
        prevDP[0][1] = 1
    if R > 0:
        prevDP[1][0] = 1

    for lv in range(2, N+1):
        accSum = lv*(lv+1)//2
        DP = [[0 for _ in range(G+1)] for _ in range(R+1)]

        # 현재 층까지 사용한 빨강의 총 개수가 totalR, 초록의 총 개수가 totalG일 때, DP 계산
        for totalR in range(R+1):
            for totalG in range(G+1):
                totalB = accSum - totalR - totalG
                if totalB < 0 or totalB > B:
                    continue

                # 현재 층에서 사용할 색 조합 저장
                caseL = [[lv, 0, 0, 1], [0, lv, 0, 1], [0, 0, lv, 1]]
                if lv % 2 == 0:
                    t = lv//2
                    caseL.append([t, t, 0, C[lv][0]])
                    caseL.append([t, 0, t, C[lv][0]])
                    caseL.append([0, t, t, C[lv][0]])
                if lv % 3 == 0:
                    t = lv//3
                    caseL.append([t, t, t, C[lv][1]])

                # 색 조합을 바탕으로 DP 계산
                for useR, useG, useB, value in caseL:
                    prevR = totalR - useR
                    prevG = totalG - useG
                    prevB = totalB - useB
                    if 0 <= prevR <= R and 0 <= prevG <= G and 0 <= prevB <= B:
                        DP[totalR][totalG] += prevDP[prevR][prevG] * value
        prevDP = DP

    result = 0
    curUse = N*(N+1)//2
    for y in range(R+1):
        for x in range(G+1):
            curB = curUse - y - x
            if 0 <= curB <= B:
                result += prevDP[y][x]
    return result


def main():
    N, R, G, B = map(int, input().split())
    print(solve(N, R, G, B))


main()
