# 백준 2734

import sys
import math

input = sys.stdin.readline


def middle(A, B):
    distance = math.sqrt((B[0]-A[0])**2 + (B[1]-A[1])**2)
    height = math.sqrt(4 - (distance/2)**2)
    return [(A[0]+B[0])/2 -(B[1]-A[1])/distance*height, (A[1]+B[1])/2 + (B[0]-A[0])/distance*height]


def solve():
    data = [[L[i], 1] for i in range(1, int(L[0])+1)]
    
    index = int(L[0])
    while index > 1:
        for i in range(1, index):
            data[i-1] = middle(data[i-1], data[i])
        index -= 1
        data.pop()
    
    return "{:.4f} {:.4f}".format(data[0][0], data[0][1])


# main 함수 ----------
T = int(input())

for _ in range(T):
    L = list(map(float, input().split()))
    print(solve())