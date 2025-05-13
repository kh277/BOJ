# 백준 25114

'''
a_i XOR x XOR x = a_i이다. 따라서 XOR 연산은 0~1회만 적용시키면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, A, B):
    count = 0
    for i in range(N-1):
        if A[i] == B[i]:
            continue
        elif A[i] != B[i]:
            x = A[i] ^ B[i]
            A[i] ^= x
            A[i+1] ^= x
            count += 1

    if A[N-1] == B[N-1]:
        return count
    return -1


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve(N, A, B))


main()
