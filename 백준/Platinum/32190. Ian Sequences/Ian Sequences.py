# 백준 32190

'''
수열을 ...89674523132547698... 처럼 나타내면 된다.
'''

import io
from collections import deque

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    q = deque()
    q.append(1)

    if N % 2 == 1:
        for i in range(1, N//2+1):
            q.append(i*2+1)
            q.appendleft(i*2+1)
            q.append(i*2)
            q.appendleft(i*2)
        q.append(1)
    else:
        for i in range(1, N//2):
            q.append(i*2+1)
            q.appendleft(i*2+1)
            q.append(i*2)
            q.appendleft(i*2)
        
        q.append(N)
        q.append(1)
        q.append(N)

    return list(q)


def main():
    N = int(input())
    print(*solve(N))


main()
