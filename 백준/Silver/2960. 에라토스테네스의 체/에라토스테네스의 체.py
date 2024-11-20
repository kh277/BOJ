# 백준 2960

import sys

input = sys.stdin.readline


def Eratos(N):
    count = 0
    num = [i for i in range(N+1)]

    for i in range(2, N+1):
        # i가 소수인 경우, i를 제외한 i의 배수 지우기
        if num[i] != 0:
            for j in range(i, N+1, i):
                if num[j] != 0:
                    num[j] = 0
                    count += 1
                    # 지운 숫자의 개수 확인
                    if count == K:
                        return j


# main 함수 ----------
N, K = map(int, input().split())
print(Eratos(N))