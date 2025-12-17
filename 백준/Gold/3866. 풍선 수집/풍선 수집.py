# 백준 3866

'''
DP[i][x][c] = 현재 위치가 x이고 들고 있는 풍선이 c개일 때, i번째 풍선까지 회수하기 위한 최소 이동 거리.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**8
MAX_X = 100


def solve(N, ball):
    DP = [[[INF] * 4 for _ in range(MAX_X+1)] for _ in range(N+1)]
    DP[0][0][0] = 0

    prevT = 0
    for i in range(1, N+1):
        ballX, ballT = ball[i-1]
        canCatch = False

        # 갖고 있는 풍선을 그대로 들고 현재 풍선을 잡는 경우
        for prevX in range(MAX_X+1):
            for count in range(3):
                if DP[i-1][prevX][count] == INF:
                    continue
                robotT = prevT + abs(ballX - prevX)*(count+1)
                if robotT <= ballT:
                    canCatch = True
                    DP[i][ballX][count+1] = min(DP[i][ballX][count+1], DP[i-1][prevX][count] + abs(ballX-prevX))
        
        # 갖고 있는 풍선을 집에 보관한 뒤 현재 풍선을 잡는 경우
        for prevX in range(MAX_X+1):
            for count in range(1, 4):
                if DP[i-1][prevX][count] == INF:
                    continue
                robotT = prevT + prevX*(count+1) + ballX
                if robotT <= ballT:
                    canCatch = True
                    DP[i][ballX][1] = min(DP[i][ballX][1], DP[i-1][prevX][count] + prevX+ballX)

        # 풍선을 잡지 못한 경우
        if canCatch == False:
            return f"NG {i}"
        prevT = ballT

    # 최소 이동거리 도출
    result = INF
    for curX in range(MAX_X+1):
        for c in range(4):
            result = min(result, DP[N][curX][c] + curX)
    
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
