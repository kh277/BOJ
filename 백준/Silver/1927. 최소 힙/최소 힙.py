# 백준 1927

'''
최소 힙은 pop 연산을 할 때 항상 가장 작은 값을 리턴해야 한다.
또한 최소 힙은 완전이진트리로 구성되므로 append, pop 연산 모두 O(logN)의 시간복잡도를 가진다.
python에서는 import heapq를 해서 힙을 사용하거나,
from queue import PriorityQueue를 해서 우선순위 큐를 사용한다.
'''

import sys
from queue import PriorityQueue

input = sys.stdin.readline


def solve(N: int, x: list) -> list:
    result = []
    q = PriorityQueue()

    for i in x:
        if i == 0:
            if q.empty():
                result.append(0)
            else:
                result.append(q.get())
        else:
            q.put(i)

    return result


def main():
    N = int(input())
    x = [0 for _ in range(N)]
    for i in range(N):
        x[i] = int(input())

    for i in solve(N, x):
        print(i)


main()
