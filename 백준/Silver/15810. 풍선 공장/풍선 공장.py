# 백준 15810

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(N, time, A):
    count = 0
    for i in range(N):
        count += time//A[i]
    return count


def solve(N, M, A):
    start = 1
    end = 1000000000000

    while start < end:
        mid = (start+end)//2
        if check(N, mid, A) >= M:
            end = mid
        else:
            start = mid+1

    return start


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(solve(N, M, A))


main()
