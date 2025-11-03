# 백준 2428

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    A.sort()
    result = 0

    for i in range(N):
        yes = i
        no = N-1

        while abs(yes - no) > 1:
            mid = (yes + no)//2
            if A[i] >= A[mid] * 0.9:
                yes = mid
            else:
                no = mid

        if A[i] >= A[no] * 0.9:
            result += no - i
        else:
            result += yes - i

    return result


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
