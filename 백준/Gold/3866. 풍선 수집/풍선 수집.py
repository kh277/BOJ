# 백준 3866

'''
DP[i][c] = 현재 들고 있는 풍선이 c개일 때, i번째 풍선까지 회수하기 위한 최소 이동 거리.
DP[i]를 계산하기 위해서는 DP[i-1]만 필요하기 때문에 1차원으로 줄일 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8
MAX_X = 100


def solve(N, ball):
    prevDP = [INF] * 4
    prevDP[0] = 0
    prevT = 0
    prevX = 0

    for i in range(1, N+1):
        DP = [INF] * 4
        ballX, ballT = ball[i-1]
        canCatch = False

        # 갖고 있는 풍선을 그대로 들고 현재 풍선을 잡는 경우
        for count in range(3):
            robotT = prevT + abs(ballX - prevX)*(count+1)
            if prevDP[count] != INF and robotT <= ballT:
                canCatch = True
                DP[count+1] = min(DP[count+1], prevDP[count] + abs(ballX-prevX))

        # 갖고 있는 풍선을 집에 보관한 뒤 현재 풍선을 잡는 경우
        for count in range(1, 4):
            robotT = prevT + prevX*(count+1) + ballX
            if prevDP[count] != INF and robotT <= ballT:
                canCatch = True
                DP[1] = min(DP[1], prevDP[count] + prevX+ballX)

        # 풍선을 잡지 못한 경우
        if canCatch == False:
            return f"NG {i}"
        prevT = ballT
        prevX = ballX
        prevDP = DP

    # 최소 이동거리 도출
    result = INF
    for c in range(4):
        result = min(result, prevDP[c] + prevX)

    return f"OK {result}"


def main():
    while True:
        N = int(input())
        if N == 0:
            break
        ball = []
        for _ in range(N):
            ball.append(list(map(int, input().split())))

        print(solve(N, ball))


main()
