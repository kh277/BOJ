# 백준 23742

'''
a_i가 음의 정수값인 학생은 1인 팀을 구성하게 하고, 음이 아닌 정수값인 학생은 전부 같은 팀에 배정하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()
    plusCount = 0
    plusSum = 0
    minusSum = 0
    result = 0
    firstMinus = -1
    for i in range(N):
        if A[i] < 0:
            minusSum += A[i]
            firstMinus = i
        else:
            plusCount += 1
            plusSum += A[i]
    
    result = minusSum + plusSum * plusCount
    
    if firstMinus != -1:
        for i in range(firstMinus, -1, -1):
            minusSum -= A[i]
            plusSum += A[i]
            plusCount += 1
            result = max(result, minusSum + plusSum*plusCount)

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
