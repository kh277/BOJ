# 백준 12789

'''
모든 사람들이 순서대로 간식을 받음 -> 스택을 이용해서 순서대로 출력이 되는지 확인.
'''

from sys import stdin
from collections import deque

input = stdin.readline

def solve(N: int, L: list) -> str:
    temp = 1
    index = 0
    stack = deque()

    while temp != N:
        if index == N:
            break
        if temp == L[index]:
            temp += 1
            index += 1
            continue
        if temp <= L[index]:
            # 스택이 비어있지 않고, 스택의 top값이 temp일 경우
            if stack and stack[-1] == temp:
                stack.pop()
                temp += 1
                continue
            stack.append(L[index])
            index += 1
            continue

        return "Sad"

    # 스택에 남은 숫자 반환
    while stack:
        num = stack.pop()
        if temp == num:
            temp += 1
            continue
        return "Sad"

    return "Nice"


def main():
    N = int(input())
    L = list(map(int, input().split()))

    print(solve(N, L))


main()
