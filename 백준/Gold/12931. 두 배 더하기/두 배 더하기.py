# 백준 12931

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checkZero(num):
    for i in num:
        if i != 0:
            return False
    
    return True


def solve(N, num):
    count = 0
    while True:
        # 홀수인 수 전부 -1
        for i in range(N):
            if num[i] % 2 == 1:
                count += 1
                num[i] -= 1
        
        if checkZero(num) == True:
            return count
        
        # 모든 수 /2
        for i in range(N):
            num[i] = num[i] // 2
        count += 1


def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()