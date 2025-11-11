# 백준 18866

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, happy, tired):
    happyMin = array('I', [0]) * N   # [happy[0], happy[i]]까지의 행복도 최소값
    happyMax = array('I', [0]) * N   # [happy[i], happy[N-1]]까지의 행복도 최대값
    tiredMin = array('I', [0]) * N   # [tired[i], tired[N-1]]까지의 피로도 최소값
    tiredMax = array('I', [0]) * N   # [tired[0], tired[i]]까지의 피로도 최대값
    minH = 2000000000
    maxH = -1
    minT = 2000000000
    maxT = -1

    # 누적합 배열 생성
    for i in range(N):
        rev = N-1-i
        if happy[i] != 0 and happy[i] < minH:
            minH = happy[i]
        if tired[rev] != 0 and tired[rev] < minT:
            minT = tired[rev]
        if happy[rev] > maxH:
            maxH = happy[rev]
        if tired[i] > maxT:
            maxT = tired[i]
        happyMin[i] = minH
        happyMax[rev] = maxH
        tiredMin[rev] = minT
        tiredMax[i] = maxT

    # 최대 K값 도출
    result = -1
    for i in range(N-1):
        if happyMin[i] > happyMax[i+1] and tiredMax[i] < tiredMin[i+1]:
            result = i+1

    return result


def main():
    N = int(input())
    happy = array('I')
    tired = array('I')

    for _ in range(N):
        a, b = map(int, input().split())
        happy.append(a)
        tired.append(b)

    print(solve(N, happy, tired))


main()
