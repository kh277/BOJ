# 백준 9019


import io
from collections import deque
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def BFS(A, B):
    prev = array('i', [-1]) * 10000
    oper = array('i', [-1]) * 10000
    q = deque()
    q.append(A)
    prev[A] = A
    oper[A] = 10

    while q:
        curN = q.popleft()

        # D, S, L, R 연산
        for curOp, nextN in enumerate([(2*curN)%10000, (curN+9999)%10000, (curN*10+curN//1000)%10000, curN//10+(curN%10)*1000]):
            if prev[nextN] == -1:
                prev[nextN] = curN
                oper[nextN] = curOp
                q.append(nextN)

                if nextN == B:
                    return prev, oper


def solve(A, B):
    prev, oper = BFS(A, B)

    # 역추적
    curN = B
    result = []
    while curN != A:
        beforeN = prev[curN]
        result.append(oper[curN])
        curN = beforeN
    
    op = ['D', 'S', 'L', 'R']
    return ''.join([op[result[i]] for i in range(len(result)-1, -1, -1)])


def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(solve(A, B))


main()
