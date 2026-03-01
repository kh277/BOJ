# 백준 3066

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# arr에서 target 이상인 원소들 중 최소 인덱스 반환
def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


def solve(N, L):
    stack = array('I')
    stack.append(L[0])

    for i in range(1, N):
        if stack[-1] < L[i]:
            stack.append(L[i])
        else:
            target = BinarySearch(stack, L[i])
            stack[target] = L[i]

    return len(stack)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = []
        for _ in range(N):
            A.append(int(input()))
        print(solve(N, A))


main()
