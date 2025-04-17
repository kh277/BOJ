# 백준 15167

'''
각 사각형을 K개의 껍질로 보면,
step번째 껍질은 구간 [(2*step-3)^2, (2*step-1)^2]까지의 수가 적혀있다.
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def getPos(A):
    if A == 1:
        return [0, 0]

    step = math.ceil((A**0.5+1)/2)
    for i in range(4):
        if (2*step-1)**2 - (i+1)*(2*step-2) < A <= (2*step-1)**2 - i*(2*step-2):
            break

    for j in range(2*step-2):
        if (2*step-1)**2 - (2*step-2)*i - j == A:
            if i == 0:
                return [1-step, 1-step+j]
            elif i == 1:
                return [1-step+j, step-1]
            elif i == 2:
                return [step-1, step-1-j]
            else:
                return [step-1-j, 1-step]


def solve(A, B):
    posA = getPos(A)
    posB = getPos(B)
    return abs(posB[0]-posA[0]) + abs(posB[1]-posA[1])


def main():
    A, B = map(int, input().split())
    print(solve(A, B))


main()
