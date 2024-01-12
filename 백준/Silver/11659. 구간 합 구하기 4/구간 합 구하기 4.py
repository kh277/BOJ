# 백준 11659

'''
누적 합에 대한 리스트를 저장한다.
S[0] = 0 / S[1] = a1 / S[2] = a1, a2, ... / S[n] = a1, ..., an
'''

import sys
input = sys.stdin.readline


def solve(start: int, end: int, sum: list):
    return sum[end] - sum[start-1]



def main():
    N, M = map(int, input().split())

    num = list(map(int, input().split()))

    # 누적 합 계산
    sum = [0 for _ in range(N+1)]
    sum[0] = 0          # 누적합 0번째는 사용 X.
    for i in range(1, N+1):
        sum[i] = sum[i-1] + num[i-1]

    # 입력 값에 대해 계산
    for x in range(M):
        i, j = map(int, input().split())
        print(solve(i, j, sum))


main()
