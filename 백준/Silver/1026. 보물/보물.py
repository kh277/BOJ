# 백준 1026

'''
A는 오름차순, B는 내림차순으로 정렬할 경우 S의 값이 최소가 된다.
'''


import sys

input = sys.stdin.readline


def solve(N: int, A: list, B: list) -> int:
    A.sort()
    B.sort(reverse=True)

    result = 0

    for i in range(N):
        result += A[i] * B[i]
    
    return result
    

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(solve(N, A, B))


main()