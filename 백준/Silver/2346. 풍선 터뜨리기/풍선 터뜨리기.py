# 백준 2346

'''
5
3 2 1 -3 -1가 입력이라면,

1. deque에서는 [(3, 1), (2, 2), (1, 3), (-3, 4), (-1, 5)]가 들어간다.
3칸을 이동해야 하므로, 제일 앞에있는 (3, 1)은 빼고,
(2, 2), (1, 3) 2개를 차례대로 왼쪽에서 popleft()하고 오른쪽에 다시 append()시킨다.

2. deque에는 [(-3, 4), (-1, 5), (2, 2), (1, 3)]이 있게 된다.
제일 앞의 (-3, 4)는 빼고
(1, 3), (2, 2) 2개를 차례대로 오른쪽에서 pop()하고 왼쪽에 다시 appendleft()시킨다.

이 과정을 deque가 빌 때까지 반복한다.
'''

from sys import stdin
import collections

input = stdin.readline


def solve(N: int, S: list) -> list:
    result = []
    deque = collections.deque(S)

    move = 1

    while deque:
        if move > 0:
            for i in range(move - 1):
                temp = deque.popleft()
                deque.append(temp)
            key = deque.popleft()

        else:
            for i in range(abs(move) - 1):
                temp = deque.pop()
                deque.appendleft(temp)
            key = deque.pop()

        result.append(key[1])
        move = key[0]

    return result

def main():
    N = int(input())
    L = list(map(int, input().split()))
    S = [[L[i], i+1] for i in range(N)]

    for i in solve(N, S):
        print(i, end=' ')


main()
