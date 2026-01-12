# 백준 21695

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    # 누적 합 배열 전처리
    sumDict = dict()
    sumDict[0] = 1
    accSum = 0
    for i in range(N):
        if A[i] == 'a':
            accSum += 1
        else:
            accSum -= 1
        if accSum in sumDict:
            sumDict[accSum] += 1
        else:
            sumDict[accSum] = 1

    # 누적 합 값 배열 처리
    count = 0
    for k in sumDict.keys():
        curV = sumDict[k]
        count += curV * (curV - 1) // 2

    return count


def main():
    N = int(input())
    A = input().decode().rstrip()
    print(solve(N, A))


main()
