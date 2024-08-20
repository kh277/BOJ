# 백준 6219

import sys

input = sys.stdin.readline

def Eratos(N: int) -> list:
    num = [i for i in range(N+1)]

    for i in range(2, N+1):
        if num[i] == 0:
            continue
        for j in range(i*2, N+1, i):
            num[j] = 0
    
    return [i for i in num if not i == 0][1:]


def solve(A, B, D):
    # B 이하의 소수 추출
    prime = Eratos(B)

    # prime에서 A 이상의 소수 추출
    for i in range(len(prime)):
        if prime[i] >= A:
            prime = prime[i:]
            break

    # 추출한 소수들에서 숫자 D 찾기
    count = 0
    for i in prime:
        for j in str(i):
            if j == str(D):
                count += 1
                break

    return count


def main():
    A, B, D = map(int, input().split())
    
    print(solve(A, B, D))


main()