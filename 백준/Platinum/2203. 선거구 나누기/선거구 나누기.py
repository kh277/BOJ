# 백준 2203

import io
import random

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, city):
    # 지지 인원 하위 N개 도시는 C로 고정
    city.sort(reverse=True)
    C = city[2*N:]
    del city[2*N:]

    # 골고루 분포하도록 A와 B를 섞기
    random.shuffle(city)
    A = city[:N]
    B = city[N:]
    sumA = 0
    sumB = 0
    for i in range(N):
        sumA += A[i][0]
        sumB += B[i][0]
    target = 500*N

    # 각 도시의 지지자 수가 N이 넘을 때까지 선거구 교환 반복
    while sumA <= target or sumB <= target:
        # 랜덤으로 두 도시를 뽑아 선거구 교환
        iA = random.randint(0, N-1)
        iB = random.randint(0, N-1)

        # 교환하는 것이 이득일 경우 교환
        if (sumA >= sumB and A[iA][0] > B[iB][0]) or (sumA < sumB and A[iA][0] < B[iB][0]):
            sumA += B[iB][0] - A[iA][0]
            sumB += A[iA][0] - B[iB][0]
            A[iA], B[iB] = B[iB], A[iA]

    return A, B, C


def main():
    N = int(input())
    city = []
    for i in range(3*N):
        c = int(input())
        city.append((c, i+1))

    A, B, C = solve(N, city)
    for i in A:
        print(i[1])
    for i in B:
        print(i[1])
    for i in C:
        print(i[1])


main()
