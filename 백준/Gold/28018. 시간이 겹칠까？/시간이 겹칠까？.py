# 백준 28018

'''
점 쿼리, 구간 업데이트 문제이므로 누적합 + 차분 배열 트릭을 사용하면 된다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 1000010


def main():
    N = int(input())
    MAX = -1

    # 차분 배열에 저장
    time = array('i', [0]) * INF
    for _ in range(N):
        a, b = map(int, input().split())
        time[a] += 1
        time[b+1] -= 1
        MAX = max(MAX, b+1)

    # 누적합 계산
    accSum = array('i', [0]) * INF
    accSum[0] = time[0]
    for i in range(1, INF):
        accSum[i] = accSum[i-1] + time[i]

    # 쿼리 처리
    Q = int(input())
    for i in list(map(int, input().split())):
        print(accSum[i])


main()
