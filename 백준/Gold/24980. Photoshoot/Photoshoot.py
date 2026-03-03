# 백준 24980

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, string):
    count = 0
    A = []
    for i in range(0, N, 2):
        cur = string[i:i+2]
        if cur == "GH":
            A.append(0)
        elif cur == "HG":
            A.append(1)

    prev = A[0]
    for i in range(1, len(A)):
        if prev != A[i]:
            count += 1
        prev = A[i]
    if A[-1] == 0:
        count += 1

    return count


def main():
    N = int(input())
    string = input().decode().rstrip()

    print(solve(N, string))


main()
