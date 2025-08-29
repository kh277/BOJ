# 백준 12014

'''
LIS를 O(NlogN)으로 구하고 그 길이가 K 이하인지 확인하기
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def UpperBound(A, target):
    start = 0
    end = len(A)-1
    
    while start < end:
        mid = (start+end)//2
        if A[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


def solve(N, K, A):
    lis = array('I', [A[0]])
    for i in range(1, N):
        if lis[-1] < A[i]:
            lis.append(A[i])
        else:
            lis[UpperBound(lis, A[i])] = A[i]
    
    if len(lis) >= K:
        return 1
    return 0


def main():
    T = int(input())
    for i in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        print(f"Case #{i+1}\n{solve(N, K, A)}")


main()
