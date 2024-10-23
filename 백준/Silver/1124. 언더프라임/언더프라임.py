# 백준 1124


import sys

input = sys.stdin.readline


# 3 ~ sqrt(N)까지의 모든 홀수에 대해 소인수분해
def prime_factors(N):
    factors = []

    # 2로 나누어 떨어지는 경우 처리
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    # 홀수에 대해 처리
    x = 3
    while x * x <= N:
        while N % x == 0:
            factors.append(x)
            N //= x
        x += 2
    
    # 남은 수에 대해 처리
    if N > 2:
        factors.append(N)
    
    return factors


def solve():
    # 10만 이하의 수를 소인수분해 했을 때 인수의 개수는 최대 16개임 
    prime = [2, 3, 5, 7, 11, 13]
    result = []

    for i in range(A, B+1):
        factors = prime_factors(i)
        if len(factors) in prime:
            result.append(i)
    
    return len(result)


# main 함수 ----------
A, B = map(int, input().split())

print(solve())