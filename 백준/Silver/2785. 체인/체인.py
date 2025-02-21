# 백준 2785

'''
chain을 오름차순으로 정렬한 뒤, 작은 수부터 하나씩 꺼낸다.
꺼낸 수만큼 남은 체인의 길이를 1씩 줄인다.
체인의 길이가 1이 되면 종료한다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    chain.sort()

    if chain[0] > N-2:
        return N-1

    q = deque(chain)
    result = 0
    while len(q) > 1:
        cur = q.popleft()
        for _ in range(cur):
            if len(q) > 1:
                q.pop()
                result += 1
            else:
                return result+1
        if len(q) == 1:
            break

    return result


# main 함수 ----------
N = int(input())
chain = list(map(int, input().split()))

print(solve())
