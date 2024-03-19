# 백준 2565

'''
A, B 전봇대의 전깃줄을 함수의 정의역 x, 치역 y로 생각해보자.
전깃줄이 교차하지 않으려면, 함수가 증가함수여야 한다.
증가함수만 남도록 정의역에서 원소를 빼는 것은 LIS 문제를 푸는 것과 비슷하다.

즉, 가장 긴 증가하는 부분 수열과을 구하고,
전체 전선 개수에서 LIS 길이을 뺀 값을 출력하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, A: list) -> int:
    DP = [1 if A[i] != -1 else -1 for i in range(501)]

    # 현재 탐색하고자 하는 값
    for i in range(501):
        # 이전 값들의 LIS 탐색
        for j in range(0, i):
            if A[i] > A[j] and DP[i] != -1:
                DP[i] = max(DP[i], DP[j] + 1)

    # DP 테이블에서 가장 긴 LIS 길이 탐색
    result = 0
    for i in range(501):
        if result < DP[i]:
            result = DP[i]

    # 전선 - LIS 길이 반환
    return N - result



def main():
    N = int(input())
    A = [-1 for _ in range(501)]

    for i in range(N):
        a, b = map(int, input().split())
        A[a] = b

    print(solve(N, A))


main()
