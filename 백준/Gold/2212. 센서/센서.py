# 백준 2212

'''
각 센서 사이의 거리를 전부 구한 뒤 길이 리스트를 오름차순 정렬해준다.
(기지국의 개수) - 1개의 수를 pop시킨다.
남은 수들의 합이 정답이 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, num):
    num.sort()

    gap = []
    for i in range(1, N):
        gap.append(num[i] - num[i-1])
    gap.sort()

    result = 0
    for i in range(N-K):
        result += gap[i]
    
    return result


def main():
    N = int(input())
    K = int(input())
    num = list(map(int, input().split()))
    print(solve(N, K, num))


main()