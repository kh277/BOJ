# 백준 14292

'''
각 자릿수가 1로만 이루어진 수를 아름답다고 하는데, 10진수인 다른 정수들도 진수를 바꿈으로써 아름다워질 수 있다.
정수 N이 주어질 때, B진수로 바꿔서 아름다워질 수 있는 진수 B를 구해야 한다.
B가 여러 개라면 1의 자리수가 최대가 되도록 하는 진수를 선택해야 한다.

다시 말해, N이 주어질 때 1 + x + x^2 + x^3 + ... x^r = N을 만족하는 정수 x의 최소값을 구하는 문제이다.
정리하면, (x^r - 1)/(x-1) 형태로 쓸 수 있는 정수 중, r이 최대인 x값을 찾는 문제라고 볼 수 있다.

2^62가 2의 제곱수 중 10^18을 넘지 않는 가장 큰 제곱수이므로 r이 가질 수 있는 최대값은 62이다.
따라서 r = 62, 61, ..., 2일 때에 대해 위 식을 만족하는 정수 x가 존재하는지 이분 탐색으로 구하면 된다.
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# r, x가 주어질 때, x^0 + x^1 + ... x^(r-1)의 값 반환
def check(r, x):
    first = 0
    for i in range(r):
        first += x**i

    return first


def solve(N):
    # 가능한 모든 r 값에 대해 반복
    for r in range(int(math.log2(N))+2, 1, -1):
        start = 2
        end = N

        # 이분 탐색
        while end - start > 1:
            mid = (start + end)//2

            if check(r, mid) <= N:
                start = mid
            else:
                end = mid

        # 종료조건 체크
        if check(r, end) == N:
            return end
        elif check(r, start) == N:
            return start


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    N = int(input())
    print("Case #{}: {}".format(i, solve(N)))
