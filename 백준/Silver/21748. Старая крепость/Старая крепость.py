# 백준 21748

import sys
import math

input = sys.stdin.readline


# A시작점 ~ A끝점까지의 원주 길이
def calCircle(A):
    if A[0] > A[1]:
        result = 2 * math.pi * r * (A[1]+360-A[0])/360
    else:
        result = 2 * math.pi * r * (A[1]-A[0])/360
    
    return result


# A끝점 ~ B시작점까지의 현 길이
def calLine(A, B):
    if A[1] > B[0]:
        result = math.sqrt(2 * r**2 - 2 * r**2 * math.cos(math.pi*(B[0]+360-A[1])/180))
    else:
        result = math.sqrt(2 * r**2 - 2 * r**2 * math.cos(math.pi*(B[0]-A[1])/180))
    
    return result


def solve():
    point.sort(key= lambda x: (x[0], x[1]))
    result = 0

    for i in range(N):
        result += calCircle(point[i])
        result += calLine(point[i], point[(i+1)%N])
    
    return result


# main 함수 ----------
N, r = map(int, input().split())
point = []
for _ in range(N):
    point.append(list(map(int, input().split())))

print(solve())