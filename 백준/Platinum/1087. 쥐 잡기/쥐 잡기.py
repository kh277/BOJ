# 백준 1087

'''
우리의 경계에 있는 쥐는 잡힌 쥐가 아닐 때, 모든 쥐를 잡을 수 없는 가장 큰 L을 구하는 문제이다.
다시 말하면, 우리의 경계에 있는 쥐도 잡힌 쥐로 판정할 때, 모든 쥐를 잡을 수 있는 가장 작은 L을 구하는 문제로 바꿀 수 있다.

이 경우, x좌표 또는 y좌표 차이가 가장 큰 두 쥐 사이의 거리는 아래로 볼록인 그래프를 형성하게 되고, 이 극점을 구하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10e10


# 시각 t = curTime일 때, 모든 쥐를 감싸는 가장 작은 L 반환
def check(curTime):
    minX = INF
    minY = INF
    maxX = -INF
    maxY = -INF

    for i in range(N):
        minX = min(minX, mouse[i][0]+mouse[i][2]*curTime)
        minY = min(minY, mouse[i][1]+mouse[i][3]*curTime)
        maxX = max(maxX, mouse[i][0]+mouse[i][2]*curTime)
        maxY = max(maxY, mouse[i][1]+mouse[i][3]*curTime)

    return max(maxX-minX, maxY-minY)


# check(t)인 함수에서 최소값 도출
def TernarySearch():
    start = 0
    end = 2000

    # 삼분 탐색
    count = 0
    while count < 100:
        first = (2*start+end)/3
        second = (start+2*end)/3

        # 함수값 체크
        if check(first) > check(second):
            start = first
        else:
            end = second

        count += 1

    return check((first+second)/2)


# main 함수 ----------
N = int(input())
mouse = []
for _ in range(N):
    mouse.append(tuple(map(int, input().split())))

print(TernarySearch())
