# 백준 6926

'''
달리기 구간(x), 도착 지점까지 걸리는 시간(y), 달리기 속도(runS), 사이클 속도(cycS)라고 할 때,
y = {(cycS - runS)*x + t*runS} / (runS*cycS)를 만족한다.
전체 범위에서, 다른 참가자들과의 y값 차이가 최대가 되는 x값을 찾아야 한다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000
EPS = 1e-9


# 달리기 구간의 길이가 x일 때, (runS, cycS) 스펙을 가진 선수가 도착하는 시간 반환
def getY(T, runS, cycS, x):
    up = (cycS-runS)*x + runS*T
    down = runS*cycS
    return up / down


# 달리기 구간의 길이가 x일 때, 치터 선수와 다른 선수가 도착하는 시간의 차이의 최소값 반환
def f(T, N, data, x):
    result = INF
    curY = getY(T, data[N-1][0], data[N-1][1], x)
    for i in range(N-1):
        result = min(result, getY(T, data[i][0], data[i][1], x) - curY)
    return result


def solve(T, N, data):
    start = 0
    end = T

    # 삼분 탐색으로 다른 모든 직선들과의 차이의 최대값 도출
    repeatCount = 0
    while repeatCount < 100:
        first = (2*start+end)/3
        second = (start+2*end)/3

        if f(T, N, data, first) < f(T, N, data, second):
            start = first
        else:
            end = second
        repeatCount += 1

    if f(T, N, data, start) + EPS < 0:
        return "The cheater cannot win."
    return f"The cheater can win by {f(T, N, data, start)*3600+EPS:.0f} seconds with r = {start+EPS:.2f}km and k = {T-start+EPS:.2f}km."


def main():
    T = int(input())
    N = int(input())
    data = []
    for _ in range(N):
        data.append(tuple(map(float, input().split())))
    print(solve(T, N, data))


main()
