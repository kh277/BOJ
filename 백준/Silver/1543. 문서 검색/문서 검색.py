# 백준 2745

'''
주의 반례
aabb
ab
-> 1

ababac
abac
-> 1
'''

import sys

input = sys.stdin.readline


def str_check(A: str, B: str):
    for i in range(len(B)):
        if A[i] != B[i]:
            return False
    
    return True


def solve(A: str, B: str) -> int:
    count = 0
    index = 0

    while index <= len(A) - len(B):
        if str_check(A[index:index+len(B)], B):
            count += 1
            index += len(B)
        else:
            index += 1

    return count


def main():
    A = input().rstrip()
    B = input().rstrip()

    print(solve(A, B))


main()