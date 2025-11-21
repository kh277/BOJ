# 백준 13422

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, K, money):
    # 초기 누적합 구성
    count = 0
    accSum = 0
    for i in range(M):
        accSum += money[i]
    if accSum < K:
        count += 1

    # 반례 처리
    if N == M:
        return count

    # 이동하면서 누적합 계산
    for i in range(N-1):
        accSum -= money[i]
        accSum += money[(i+M)%N]

        if accSum < K:
            count += 1

    return count


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        money = list(map(int, input().split()))
        print(solve(N, M, K, money))


main()
