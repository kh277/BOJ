# 백준 30788

'''
DP[i][j][k] = i번째 각도까지 사용했고 지금까지 짝수쪽에 j번 넣었을 때, 각도 k에 접근 가능한지 여부
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, angle):
    if N % 2 == 1:
        return [['NO']]

    evenMax = N//2
    DP = [[[-1] * 360 for _ in range(evenMax+1)] for _ in range(N+1)]
    DP[0][0][0] = 0

    # DP 계산
    for i in range(N):
        for j in range(evenMax+1):
            for curA in range(360):
                if DP[i][j][curA] != -1:
                    # 짝수쪽에 추가
                    if j < evenMax:
                        nextA = (curA + 2*angle[i] + 360) % 360
                        DP[i+1][j+1][nextA] = j
                    # 홀수쪽에 추가
                    if i - j <= evenMax:
                        nextA = (curA - 2*angle[i] + 360) % 360
                        DP[i+1][j][nextA] = j

    if DP[N][evenMax][0] == -1:
        return [['NO']]

    # DP 역추적
    traceback = [[], []]
    curA = 0
    curJ = evenMax
    for i in range(N, 0, -1):
        curDP = DP[i][curJ][curA]
        # 짝수에 넣은 경우
        if curDP != curJ:
            curA = (curA - 2*angle[i-1] + 360) % 360
            traceback[1].append(i)
            curJ -= 1
        # 홀수에 넣은 경우
        else:
            curA = (curA + 2*angle[i-1] + 360) % 360
            traceback[0].append(i)

    # 출력 정리
    result = []
    for i in range(N):
        result.append(traceback[i%2][i//2])

    return [['YES'], result]


def main():
    N = int(input())
    angle = list(map(int, input().split()))

    for i in solve(N, angle):
        print(*i)


main()
