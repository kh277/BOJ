# 백준 1715

'''
우선순위 큐를 사용해서 값을 추출하는 것이 매 과정에서 최선의 선택이다.

우선순위 큐에서 두 개의 값을 pop한 뒤 더하고 우선순위 큐에 다시 push한다.
위 과정을 값이 1개만 남을 때까지 반복한다.


'''

import sys
import heapq

input = sys.stdin.readline


def solve(N: int, card: list) -> int:
    # 카드 묶음이 하나밖에 없을 경우 비교 횟수는 0이다
    if N == 1:
        return 0

    # card를 우선순위 큐에 넣음
    hq = []
    for i in card:
        heapq.heappush(hq, i)

    # 우선순위 큐에서 값 2개를 추출해서 더한 뒤 다시 우선순위 큐에 넣음
    result = 0
    for i in range(N):
        if len(hq) == 1:
            return result
        if len(hq) >= 2:
            temp = heapq.heappop(hq) + heapq.heappop(hq)
            result += temp
            heapq.heappush(hq, temp)


def main():
    N = int(input())

    card = []
    for _ in range(N):
        card.append(int(input()))
    
    print(solve(N, card))


main()
