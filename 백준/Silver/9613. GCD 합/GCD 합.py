# 백준 9613

import sys

input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a%b)


def solve(N, number):
    accGCD = 0
    for i in range(N-1):
        for j in range(i+1, N):
            accGCD += gcd(number[i], number[j])
    
    return accGCD


# main 함수 ----------
T = int(input())
for _ in range(T):
    num = list(map(int, input().split()))
    print(solve(num[0], num[1:]))