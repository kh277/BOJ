# 백준 28995

'''
투 포인터를 이용해서 차이가 N 이하가 되도록 유지하면서 N - (구간 내 최대값) 구하기
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()
    start = 0
    end = 0
    result = 0
    while end < N:
        gap = A[end] - A[start] + 1
        if gap > N:
            start += 1
        elif gap <= N:
            result = max(result, end-start+1)
            end += 1

    return N-result


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(solve(N, A))


main()
