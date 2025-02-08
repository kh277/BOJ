# 백준 1590

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 2**32


def solve():
    result = INF

    for i in range(N):
        curStart, curGap, curTotal = bus[i]

        # 버스가 전부 지나간 경우
        if curStart + curGap*(curTotal-1) < T:
            continue
        # 버스가 아직 도착하지 않은 경우
        elif T < curStart:
            result = min(result, curStart-T)
        # 버스를 탈 수 있는 경우
        else:
            result = min(result, (curStart + curGap*curTotal - T) % curGap)

    return result if result != INF else -1


# main 함수 ----------
N, T = map(int, input().split())
bus = []
for _ in range(N):
    bus.append(map(int, input().split()))

print(solve())