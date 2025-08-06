# 백준 14269

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


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


def solve(N, dataA, data):
    dataA = list(set(dataA))
    dataA.sort()
    left = []
    result = len(dataA)

    for i in range(N):
        curA, curB, curC = data[i]
        
        # 범위 [curB, curC]를 처리할 수 있는 검 A가 있는지 체크
        startI = UpperBound(dataA, curB)
        found = False
        for j in range(startI, len(dataA)):
            if curB <= dataA[j] <= curC:
                if dataA[j] != curA:
                    found = True
                    break
            else:
                break
        
        # 범위 [curB, curC]를 처리할 검이 없다면 left에 추가
        if found == False:
            left.append([curB, curC])

    # left 범위를 최소 개수의 검으로 처리하기
    if len(left) > 0:
        left.sort(key= lambda x: (x[1], x[0]))
        curSword = left[0][1]
        result += 1
        for i in range(len(left)):
            curS, curE = left[i]
            if curS <= curSword <= curE:
                continue
            else:
                curSword = left[i][1]
                result += 1

    return result


def main():
    N = int(input())
    dataA = []
    data = []

    for _ in range(N):
        a, b, c = map(int, input().split())
        dataA.append(a)
        data.append([a, b, c])

    print(solve(N, dataA, data))


main()
