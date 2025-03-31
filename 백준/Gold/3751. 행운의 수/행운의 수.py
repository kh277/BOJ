# 백준 3751

'''
먼저 범위 [1, 10^12] 내에서 4와 7로만 이루어진 엄청난 행운의 수들을 구한다.
그 뒤 구한 수들의 곱으로 만들 수 있는 수들을 전부 구한다.
'''

import io
import sys
from array import array

sys.setrecursionlimit(10**5)
input = io.BufferedReader(io.FileIO(0), 1<<18).readline
LIMIT = 10**12


# 1 ~ 10^12 사이의 엄청난 행운의 수 반환
def getLuckyNum():
    lucky = [4, 7]

    # 4와 7로만 이루어진 수 구하기
    num = array('Q')
    num.append(4)
    num.append(7)

    index = 0
    while index < len(num):
        if len(str(num[index])) > 11:
            break
        num.append(num[index]*10 + lucky[0])
        num.append(num[index]*10 + lucky[1])
        index += 1

    # 10^12 이하의 수 중 4^a * 7^b * 44^c * 47^d * ... 형태로 표현 가능한 모든 수 구하기
    result = set()
    def recur(accNum, curIndex):
        for i in range(curIndex, len(num)):
            curNum = num[i]
            if accNum * curNum > LIMIT:
                break
            nextNum = accNum * curNum
            result.add(nextNum)
            recur(nextNum, i)

    recur(1, 0)
    return sorted(result)


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


def solve(A, B, luckyNum):
    start = LowerBound(luckyNum, A)
    end = LowerBound(luckyNum, B+1)

    return end - start


def main():
    T = int(input())
    luckyNum = getLuckyNum()

    for _ in range(T):
        A, B = map(int, input().split())
        print(solve(A, B, luckyNum))


main()