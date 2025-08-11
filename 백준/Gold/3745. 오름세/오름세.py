# 백준 3745

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# arr에서 target 이상인 원소들 중 최소 인덱스 반환
def BinarySearch(arr, target):
    start = 0
    end = len(arr)-1
    
    while start < end:
        mid = (end + start)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid
    
    return start


def solve(N, L):
    stack = array('I')
    stack.append(L[0])

    for i in range(1, N):
        if L[i] > stack[-1]:
            stack.append(L[i])
        else:
            index = BinarySearch(stack, L[i])
            stack[index] = L[i]
    
    return len(stack)


def main():
    while True:
        try:
            N = int(input())
            L = list(map(int, input().split()))
            print(solve(N, L))
        except:
            break


main()
