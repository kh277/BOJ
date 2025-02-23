# 백준 1233

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    numDict = dict()
    for i in range(1, S1+1):
        for j in range(1, S2+1):
            for k in range(1, S3+1):
                cur = i+j+k
                if cur not in numDict:
                    numDict[cur] = 1
                else:
                    numDict[cur] += 1
    
    maxData = [0, 0]
    for i in numDict.keys():
        if numDict[i] > maxData[0]:
            maxData = [numDict[i], i]

    return maxData[1]


# main 함수 ----------
S1, S2, S3 = map(int, input().split())

print(solve())
