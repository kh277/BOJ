# 백준 7453

'''
A+B, C+D로 가능한 경우의 수를 전부 세고 투 포인터를 이용해 합이 0이 되는 값을 찾으면 된다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def getSumList(A, B):
    result = array('i')
    for i in A:
        for j in B:
            result.append(i+j)

    return result


def solve(num):
    numA = sorted(getSumList(num[0], num[1]))
    numB = sorted(getSumList(num[2], num[3]))

    startP = 0
    endP = len(numB) - 1

    # 0이 되는 쌍 찾기
    result = 0
    while True:
        # 탈출 조건
        if startP == len(numA) or endP == -1:
            break

        cur = numA[startP] + numB[endP]

        # 일치하는 값을 찾은 경우 -> 한 칸씩 이동하며 탐색
        if cur == 0:
            tempA = startP+1
            while tempA < len(numA) and numA[startP] == numA[tempA]:
                tempA += 1

            tempB = endP-1
            while tempB >= 0 and numB[endP] == numB[tempB]:
                tempB -= 1

            result += (tempA-startP)*(endP-tempB)
            startP = tempA
            endP = tempB

        elif cur > 0:
            endP -= 1
        else:
            startP += 1

    return result


def main():
    N = int(input())

    num = [array('i'), array('i'), array('i'), array('i')]
    for _ in range(N):
        temp = list(map(int, input().split()))
        for i in range(4):
            num[i].append(temp[i])

    print(solve(num))


main()