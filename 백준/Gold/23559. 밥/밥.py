# 백준 23559

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, X, food):
    result = 0

    # 1000원 메뉴 총합 계산
    for i in range(N):
        result += food[i][1]

    # 5000원으로 증가시켰을 때 이득인 경우 pq에 저장
    pq = []
    for i in range(N):
        if food[i][0] > food[i][1]:
            heapq.heappush(pq, food[i][1]-food[i][0])

    # X를 넘지 않을 때까지 5000원으로 변경
    X -= 1000*N
    while pq:
        if X - 4000 >= 0:
            cur = heapq.heappop(pq)
            result -= cur
            X -= 4000
            continue
        break

    return result


def main():
    N, X = map(int, input().split())
    food = []
    for _ in range(N):
        food.append(list(map(int, input().split())))
    print(solve(N, X, food))


main()
