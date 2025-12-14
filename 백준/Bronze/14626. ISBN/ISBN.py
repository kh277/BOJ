# 백준 14626

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
value = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]


def solve(A):
    result = 0
    if A[12] == '*':
        for i in range(12):
            result += value[i] * int(A[i])
        return 10 - (result%10)

    checksum = int(A[12])
    index = -1
    for i in range(12):
        if A[i] != '*':
            result += value[i] * int(A[i])
        else:
            index = i

    for i in range(10):
        if checksum == (10 - (result + value[index] * i) % 10) % 10:
            return i


def main():
    A = input().decode().rstrip()
    print(solve(A))


main()
