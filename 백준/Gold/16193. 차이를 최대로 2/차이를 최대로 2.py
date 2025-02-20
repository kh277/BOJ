# 백준 16193

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve():
    q = deque(sorted(num))

    start = q.popleft()
    end = start
    result = 0

    while q:
        left = q[0]
        right = q[-1]

        data1 = abs(start - left)
        data2 = abs(start - right)
        data3 = abs(end - left)
        data4 = abs(end - right)

        maxData = max(data1, data2, data3, data4)
        if maxData == data1:
            start = left
            q.popleft()
            result += data1
        elif maxData == data2:
            start = right
            q.pop()
            result += data2
        elif maxData == data3:
            end = left
            q.popleft()
            result += data3
        elif maxData == data4:
            end = right
            q.pop()
            result += data4
    
    return result


# main 함수 ----------
N = int(input())
num = list(map(int, input().split()))
print(solve())