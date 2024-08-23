# 백준 1015

'''
람다 함수를 이용해 정렬하면 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, A: int) -> list:
    temp = []
    for i in range(N):
        temp.append([A[i], i])
    
    temp.sort(key= lambda x: (x[0], x[1]))

    temp2 = []
    for i in range(N):
        temp2.append([temp[i][0], temp[i][1], i])
    
    temp2.sort(key= lambda x: (x[1], x[2]))

    return [x[2] for x in temp2]


def main():
    N = int(input())
    A = list(map(int, input().split()))

    print(*solve(N, A))


main()