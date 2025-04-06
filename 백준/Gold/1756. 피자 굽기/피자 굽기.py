# 백준 1756

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(D, N, oven, dough):
    maxDiameter = oven[0]

    # 오븐의 크기 설정
    for i in range(D):
        maxDiameter = min(maxDiameter, oven[i])
        oven[i] = maxDiameter
    
    count = 0
    index = 0
    for i in range(D-1, -1, -1):
        curOvenWidth = oven[i]

        # 피자가 오븐의 현재 층보다 큰 경우
        if curOvenWidth < dough[index]:
            continue
        else:
            index += 1
            count += 1

        # 종료조건
        if index == N:
            if count == N:
                return i+1
            return 0

    return 0


def main():
    D, N = map(int, input().split())
    oven = list(map(int, input().split()))
    dough = list(map(int, input().split()))
    print(solve(D, N, oven, dough))


main()