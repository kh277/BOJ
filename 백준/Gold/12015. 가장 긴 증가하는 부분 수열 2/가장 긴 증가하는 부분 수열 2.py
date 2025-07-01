# 백준 12015

import io

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
    stack = []
    stack.append(L[0])

    for i in range(1, N):
        # stack의 마지막 값 초과일 경우 stack에 삽입
        if stack[-1] < L[i]:
            stack.append(L[i])
        # stack의 마지막 값 이하일 경우 중간 원소의 값 대체
        else:
            target = BinarySearch(stack, L[i])
            stack[target] = L[i]

    return len(stack)


def main():
    N = int(input())
    L = list(map(int, input().split()))
    print(solve(N, L))


main()
