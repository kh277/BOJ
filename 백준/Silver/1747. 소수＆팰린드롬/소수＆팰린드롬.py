# 백준 1747

import sys

input = sys.stdin.readline


# N 이하의 소수 전부 반환
def Eratos(N: int) -> list:
    num = [i for i in range(N+1)]

    for i in range(2, N+1):
        if num[i] == 0:
            continue

        for j in range(i*2, N+1, i):
            num[j] = 0

    return [i for i in num if not i == 0][1:]


# num이 팰린드롬인지 확인
def isPalin(num):
    string = str(num)
    
    index = 0
    while index < len(string)/2:
        if string[index] == string[len(string)-1-index]:
            index += 1
        else:
            return False
    
    return True


def solve():
    # N이 100만일 경우, N보다 큰 소수이면서 팰린드롬인 수를 구해야 하므로
    # 구하는 소수의 범위를 충분히 크게 잡아야 한다
    prime = Eratos(1500000)

    for i in prime:
        if i < N:
            continue
        if isPalin(i) == True:
            return i


# main 함수 ----------
N = int(input())

print(solve())