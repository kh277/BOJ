# 백준 12923

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A, B):
    status = array('I', [0]) * N
    curStar = 0
    tryCount = 0

    while curStar < 2*N:
        # 별 2개를 얻을 수 있는 스테이지가 있는지 체크
        canClear2 = -1
        for i in range(N):
            if status[i] < 2 and B[i] <= curStar:
                canClear2 = i
                break

        # 해당 스테이지 별 2개 도전
        if canClear2 != -1:
            collect = 2 - status[canClear2]
            curStar += collect
            status[canClear2] = 2
            tryCount += 1
            continue

        # 별 1개를 얻을 수 있는 스테이지 중 b가 최대인 스테이지 선택
        canClear1 = -1
        maxB = -1
        for i in range(N):
            if status[i] == 0 and A[i] <= curStar and B[i] >= maxB:
                maxB = B[i]
                canClear1 = i
        
        if canClear1 == -1:
            return 'Too Bad'
        
        status[canClear1] += 1
        curStar += 1
        tryCount += 1

    return tryCount


def main():
    N = int(input())
    A = array('I')
    B = array('I')
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(solve(N, A, B))


main()
