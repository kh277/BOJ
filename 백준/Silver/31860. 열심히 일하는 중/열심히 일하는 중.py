# 백준 31860

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, K, pq):
    day = 0
    accS = []
    beforeS = 0
    while pq:
        curI = -heapq.heappop(pq)

        # 일을 완료할 수 있는지 체크
        if curI-M > K:
            heapq.heappush(pq, -(curI-M))

        # 만족도 계산
        curS = beforeS // 2 + curI
        beforeS = curS
        accS.append(curS)
        day += 1

    return day, accS


def main():
    N, M, K = map(int, input().split())
    pq = []
    for _ in range(N):
        heapq.heappush(pq, -int(input()))

    day, satis = solve(N, M, K, pq)
    print(day)
    for i in satis:
        print(i)


main()
