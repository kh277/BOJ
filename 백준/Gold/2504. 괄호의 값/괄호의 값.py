# 백준 2504

'''
개어려움 - 답 참고
올바른 괄호쌍을 계산할 때 스택을 사용한다는 것까지는 생각했으나,
그 뒤에 어떤 값을 어떻게 곱해야하는지는 생각하지 못했다.

여는 괄호가 올 때는 temp에 숫자를 곱해주고 닫는 괄호가 올 때는 result에 더하고 **숫자로 나눠줘야** 한다.
([]())의 경우
  : temp = 1, result = 0
( : temp = 2, result = 0
[ : temp = 6, result = 0
] : temp = 2, result = 6
( : temp = 4, result = 6
) : temp = 2, result = 10
) : temp = 1, result = 10   <- 괄호가 (), []과 같이 바로 닫힐때만 result에 더함
-> 2*3 + 2*2로 10
'''

from sys import stdin
from collections import deque

input = stdin.readline


def solve(L: list, N: int) -> int:
    stack = deque()
    result = 0
    temp = 1

    for i in range(N):
        br = L[i]

        if br == '(':
            temp *= 2
            stack.append(br)
        elif br == '[':
            temp *= 3
            stack.append(br)

        elif br == ')':
            # 스택이 비어있지 않거나 괄호쌍이 안맞는 경우
            if not stack or stack[-1] == '[':
                return 0
            # 이전 괄호가 '(' 였다면 res에 추가
            if L[i-1] == '(':
                result += temp
            temp //= 2
            stack.pop()

        elif br == ']':
            if not stack or stack[-1] == '(':
                return 0
            if L[i-1] == '[':
                result += temp
            temp //= 3
            stack.pop()

    if stack:
        return 0

    return result


def main():
    L = list(input().rstrip())
    print(solve(L, len(L)))


main()
