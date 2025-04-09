# 백준 31963

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# a * 2^x >= b의 해 구하기
def exp(a, b):
    count = 0
    while True:
        if a >= b:
            return [count, a]
        a *= 2
        count += 1


def solve(N, num):
    count = 0
    foreNum = num[0]
    index = 0
    while index < N:
        curNum = num[index]
        # 오름차순이 아닐 경우
        if foreNum > curNum:
            c, curNum = exp(curNum, foreNum)
            count += c

        foreNum = curNum
        index += 1
    
    return count


def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()
