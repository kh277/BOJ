# 백준 1644

'''
prime = N까지의 소수가 저장된 배열
N이 소수의 연속합으로 이루어지는지 판별하기

1번째 소수~k번째 소수까지 더해서 N이 되는 k 구하기
합이 N보다 클 경우 -> 앞쪽의 포인터 +1
합이 N보다 작을 경우 -> 뒤쪽의 포인터 +1
이 과정을 뒤쪽 포인터가 마지막 값에 도달하게 될 때까지 반복 
'''

import sys

input = sys.stdin.readline


def Eratos(N: int) -> list:
    num = [i for i in range(N+1)]

    for i in range(2, N+1):
        # 이미 지워진 숫자인 경우
        if num[i] == 0:
            continue
        
        # 숫자 지우기
        for j in range(i*2, N+1, i):
            num[j] = 0
    
    # 에라토스테네스의 체에서 0인 값 삭제 및 숫자 1 삭제
    return [i for i in num if not i == 0][1:]


def solve(N: int) -> int:
    # 예외 케이스 - 1은 소수들의 합으로 나타낼 수 없음
    if N == 1:
        return 0

    # N 이하의 모든 소수 반환
    prime = Eratos(N)
    start = 0
    end = 0
    prime_sum = prime[0]
    count = 0

    # end 포인터가 마지막에 도달하기 전까지 반복
    while end <= len(prime):
        # 구간합이 N과 같다면
        if prime_sum == N:
            count += 1
            end += 1
            if end == len(prime):
                break
            prime_sum += prime[end]

        # 구간합이 N보다 크다면 -> start 포인터 이동
        elif prime_sum > N:
            prime_sum -= prime[start]
            start += 1

        # 구간합이 N보다 작다면 -> end 포인터 이동
        else:
            end += 1
            if end == len(prime):
                break
            prime_sum += prime[end]

    return count
    

def main():
    N = int(input())

    print(solve(N))


main()