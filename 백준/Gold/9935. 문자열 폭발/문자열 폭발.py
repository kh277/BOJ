# 백준 9935

'''
스택을 사용하여 탐색할 문자열의 문자를 하나씩 집어넣는다.
스택에서 마지막 2개의 문자가 폭발 문자열과 일치할 경우 그 문자열을 제거한다.
더 제거되는 문자가 없을 때까지 반복한다.
'''

import sys

input = sys.stdin.readline


def check_str(S: str, B: str) -> str:
    stack = []

    for i in S:
        stack.append(i)

        # 문자열이 일치하는지 확인
        if ''.join(stack[-len(B):]) == B:
            del stack[-len(B):]
    
    return stack


def solve(S: str, B: str) -> str:
    temp = len(S)
    
    # 문자열이 폭발하지 않을 때까지 반복
    while True:
        S = check_str(S, B)

        # 문자열이 폭발하지 않은 경우
        if temp == len(S):
            break
        
        # 문자열이 폭발한 경우
        else:
            temp = len(S)

    # 남은 문자열이 없는 경우
    if len(S) == 0:
        return "FRULA"
    else:
        return ''.join(S)


def main():
    S = input().rstrip()
    B = input().rstrip()

    print(solve(S, B))


main()