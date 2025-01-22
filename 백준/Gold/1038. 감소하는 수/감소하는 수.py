# 백준 1038

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 자릿수가 depth인 감소하는 수를 전부 구하여 반환. maxNum 미만의 수로만 구성
def recur(depth, curNum, maxNum):
    if depth == 0:
        return {int(curNum)}
    
    result = set()
    for i in range(maxNum-1, -1, -1):
        result = result | recur(depth-1, curNum+str(i), i)
    
    return result


def solve():
    # 감소하는 수는 총 1022개이므로
    if N >= 1023:
        return -1

    result = set()
    # 자릿수가 digit인 감소하는 수를 전부 저장
    for digit in range(1, 11):
        result = result | recur(digit, "", 10)

    return sorted(result)[N]


# main 함수 ----------
N = int(input())
print(solve())