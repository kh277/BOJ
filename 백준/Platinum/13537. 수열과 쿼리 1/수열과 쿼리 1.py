# 백준 13537

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def square(num):
    result = 1
    while True:
        if result >= num:
            return result
        result *= 2


# arr에서 target보다 큰 첫 번째 요소의 개수 반환
def upperBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid

    return len(arr) - start


# 배열 left, right 병합
def merge(left, right):
    l, r = 0, 0
    result = array('I')
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    return result


# 구간 [left, right]에서 value보다 큰 원소의 개수 반환
def query(N, tree, left, right, value):
    result = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            result += upperBound(tree[left], value)
            left += 1
        if ~right & 1:
            result += upperBound(tree[right], value)
            right -= 1

        left >>= 1
        right >>= 1

    return result


# 세그먼트 트리 빌드
def build(N, A):
    tree = [array('I') for _ in range(N*2)]
    for i in range(len(A)):
        tree[N+i].append(A[i])

    for i in range(N-1, 0, -1):
        left = i<<1
        right = i<<1 | 1

        tree[i] = merge(tree[left], tree[right])
    
    return tree


def main():
    N = int(input())
    A = list(map(int, input().split()))

    treeSize = square(N)
    tree = build(treeSize, A)

    M = int(input())
    for _ in range(M):
        i, j, k = map(int, input().split())
        print(query(treeSize, tree, i-1, j-1, k))


main()
