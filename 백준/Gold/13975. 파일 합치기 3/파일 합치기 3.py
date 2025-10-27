# 백준 13975

'''
그리디하게 파일 중 제일 작은 파일 2개를 합치는 과정을 반복하면 최적해가 나온다.
'''

import io
import heapq

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def solve(N, L):
    heapq.heapify(L)

    cost = 0
    for _ in range(N-1):
        A = heapq.heappop(L)
        B = heapq.heappop(L)
        cost += A+B
        heapq.heappush(L, A+B)

    return cost


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = list(map(int, input().split()))
        print(solve(N, L))


main()
