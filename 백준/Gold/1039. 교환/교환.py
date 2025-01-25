# 백준 1039

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# curNum에서 자릿수 a와 b를 swap
def swapDigit(curNum, a, b):
    return curNum[:a] + curNum[b] + curNum[a+1:b] + curNum[a] + curNum[b+1:]


def solve():
    length = len(str(N))
    if length == 1:
        return -1

    result = {str(N)}

    # 변경 연산 K번 수행
    for _ in range(K):
        curResult = set()

        # result 내의 모든 숫자의 모든 자릿수에 대해 연산을 수행한 결과 저장
        for curNum in result:
            for change in range(length-1):
                for changed in range(change+1, length):
                    swapResult = swapDigit(curNum, change, changed)
                    if len(str(int(swapResult))) == length:
                        curResult.add(swapResult)

        # 더 이상 변경을 수행할 수 없는 경우
        if len(curResult) == 0:
            return -1

        result = curResult
    
    maxNum = 0
    for i in result:
        maxNum = max(maxNum, int(i))

    # 자릿수가 달라진 경우
    if len(str(maxNum)) < length:
        return -1

    return maxNum


# main 함수 ----------
N, K = map(int, input().split())
print(solve())