# 백준 2751

'''
1 <= N <= 1,000,000이고, N=1,000,000인 경우, O(N^2)의 정렬 알고리즘은 2초 내에 완료하지 못한다.
따라서 O(NlogN)의 시간복잡도를 가지는 Quick Sort를 구현해야 한다.

중간값을 pivot으로 사용할 때, 재귀 깊이가 너무 깊어지는 경우가 발생한다.
따라서 sys.setrecursionlimit() 함수를 이용하여 재귀 깊이를 늘려준다.

메모리 초과가 발생할 수 있으므로, randint() 함수를 사용하여 랜덤값으로 pivot을 정한다.
'''

import sys
from random import randint

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def quick_Sort(N: int, arr: int) -> list:
    if N <= 1:
        return arr

    pivot = randint(0, N-1)
    left = [x for x in arr if x < arr[pivot]]
    right = [x for x in arr if x > arr[pivot]]

    return quick_Sort(len(left), left) + [arr[pivot]] + quick_Sort(len(right), right)


def main():
    N = int(input())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = int(input())

    for i in quick_Sort(N, arr):
        print(i)


main()
