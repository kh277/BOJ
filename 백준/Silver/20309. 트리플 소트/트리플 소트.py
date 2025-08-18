# 백준 20309

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A):
    odd = [A[i] for i in range(0, N, 2)]
    even = [A[i] for i in range(1, N, 2)]

    odd.sort()
    even.sort()

    for i in range(len(even)):
        if even[i] != 2*(i+1):
            return 'NO'

    for i in range(len(odd)):
        if odd[i] != 2*i+1:
            return 'NO'

    return 'YES'


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))


main()
