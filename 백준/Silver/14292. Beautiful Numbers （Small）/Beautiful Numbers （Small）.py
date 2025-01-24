# 백준 14292

'''
각 자릿수가 1로만 이루어진 수를 아름답다고 하는데, 10진수인 다른 정수들도 진수를 바꿈으로써 아름다워질 수 있다.
정수 N이 주어질 때, B진수로 바꿔서 아름다워질 수 있는 진수 B를 구해야 한다.
B가 여러 개라면 1의 자리수가 최대가 되도록 하는 진수를 선택하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# K의 제곱수 중 N을 넘지 않는 가장 큰 제곱수의 지수 반환
def findMaxExponential(N, K):
    cur = 1
    while True:
        if K**(cur+1) <= N:
            cur += 1
        else:
            return cur


def solve(N):
    for cur in range(2, N):
        maxExp = findMaxExponential(N, cur)

        # 등비수열의 합을 이용해 cur^0 + cur^1 + ... cur^maxExp의 값 계산
        accSum = (cur**(maxExp+1)-1)//(cur-1)

        # 답을 찾았다면 바로 종료 처리
        if accSum == N:
            return cur


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    print("Case #{}: {}".format(i, solve(N)))