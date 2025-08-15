# 백준 30959

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, model, result):
    singleModel = 0
    ensembleModel = 0

    for status in range(1<<N):
        modelCount = bin(status).count('1')

        # 단일 모델일 경우
        if modelCount == 1:
            curModel = 0
            for i in range(M):
                if model[int(math.log2(status))][i] == result[i]:
                    curModel += 1
            singleModel = max(singleModel, curModel)

        # 다중 모델인 경우
        elif modelCount % 2 == 1:
            accSum = [0 for _ in range(M)]
            for curV in range(N):
                if status & (1<<curV):
                    for i in range(M):
                        accSum[i] += model[curV][i]

            curModel = 0
            for i in range(M):
                if accSum[i] > modelCount//2:
                    accSum[i] = 1
                else:
                    accSum[i] = 0
                if accSum[i] == result[i]:
                    curModel += 1
            ensembleModel = max(ensembleModel, curModel)
    
    return 1 if ensembleModel > singleModel else 0


def main():
    N, M = map(int, input().split())
    result = list(map(int, input().split()))
    model = []
    for _ in range(N):
        model.append(list(map(int, input().split())))

    print(solve(N, M, model, result))


main()
