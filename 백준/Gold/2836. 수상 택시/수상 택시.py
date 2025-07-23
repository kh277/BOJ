# 백준 2836

'''
뒤로 가는 경로들 중 겹치는 부분은 최대한 합쳐서 전체 길이를 센다.
이 길이가 보트를 뒤로 이동하는 총 거리가 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**10


def solve(N, M, minus):
    # 뒤로 가는 사람이 없는 경우
    if len(minus) == 0:
        return M

    # 뒤로 가는 사람들의 경로가 겹치는 경우 병합
    minus.sort()
    accSweep = 0
    start, end = minus[0]
    for i in range(1, len(minus)):
        curS, curE = minus[i]
        if end < curS:
            accSweep += end - start
            start = curS
            end = curE
        else:
            start = min(start, curS)
            end = max(end, curE)
    accSweep += end - start

    return M + accSweep*2


def main():
    N, M = map(int, input().split())
    minus = []
    for _ in range(N):
        a, b = map(int, input().split())
        if a > b:
            minus.append((b, a))
    print(solve(N, M, minus))


main()
