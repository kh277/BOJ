# 백준 17202


import sys

input = sys.stdin.readline


def solve(A: str, B: str) -> int:
    total = ""

    for i in range(8):
        total += A[i]
        total += B[i]

    temp = ""

    while True:
        if len(total) == 2:
            break

        for i in range(1, len(total)):
            temp += str((int(total[i-1])+int(total[i])) % 10)

        total = temp
        temp = ""

    return total


def main():
    A = input().rstrip()
    B = input().rstrip()

    print(solve(A, B))


main()