# 백준 7453

'''
A+B, C+D로 가능한 경우의 수를 전부 세고 투 포인터를 이용해 합이 0이 되는 값을 찾으면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def getSumList(A, B):
    result = []
    for i in A:
        for j in B:
            result.append(i+j)

    return result


# arr에서 target 이상인 첫 번째 요소의 인덱스 반환
def LowerBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


# arr에서 target보다 큰 첫 번째 요소의 인덱스 반환
def UpperBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid

    return start


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

        # 일치하는 값을 찾은 경우 -> 이분 탐색 2번으로 동일한 숫자 개수 찾기
        if cur == 0:
            endNumA = UpperBound(numA, numA[startP]) - 1
            endNumB = LowerBound(numB, numB[endP])
            result += (endNumA-startP+1)*(endP-endNumB+1)
            startP = endNumA+1
        elif cur > 0:
            endP -= 1
        else:
            startP += 1

    return result


def main():
    N = int(input())

    num = [[], [], [], []]
    for _ in range(N):
        temp = list(map(int, input().split()))
        for i in range(4):
            num[i].append(temp[i])

    print(solve(num))


main()
