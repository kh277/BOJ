# 백준 1153

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# 소수 판별 함수
def checkPrime(N):
    if N <= 1:
        return False
    elif N <= 3:
        return True
    elif N % 2 == 0 or N % 3 == 0:
        return False

    for i in range(5, int(N**0.5)+1, 6):
        if N % i == 0 or N % (i + 2) == 0:
            return False

    return True


def backtrack(N, num):
    # 백트래킹 종료 조건
    if len(num) == 4:
        return num

    # N 이하에 대해 백트래킹
    for i in range(N, 1, -1):
        if checkPrime(i) == True:
            temp = backtrack(N-i, num + [i])
            if temp == [-1]:
                continue
            return temp

    return [-1]


def solve(N):
    if N < 8:
        return [-1]
    return backtrack(N, [])


while True:
    try:
        N = int(input())
        print(*solve(N))
    except:
        break
