# 백준 4948

'''
1 <= n <= 123,456이므로 O(N*sqrt(N))인 에라토스테네스의 체를 이용하자. 
'''

import sys
import math

input = sys.stdin.readline

def check(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def solve(N):
    result = 0

    for i in range(N+1, 2*N+1):
        if i == 1:
            continue
        if check(i):
            result += 1

    return result


# main 함수 ----------
while True:
    n = int(input())
    if n == 0:
        break
    print(solve(n))
