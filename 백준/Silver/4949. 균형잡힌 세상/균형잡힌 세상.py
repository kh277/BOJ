# 백준 4949

'''
스택을 이용해 괄호쌍을 계산하자.
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve(string):
    q = deque()

    for i in string:
        # 여는 괄호일 경우
        if i in ['(', '[']:
            q.append(i)
        
        # 닫는 괄호일 경우
        elif i == ')':
            if len(q) == 0:
                return 'no'
            if q.pop() != '(':
                return 'no'
        elif i == ']':
            if len(q) == 0:
                return 'no'
            if q.pop() != '[':
                return 'no'
    
    if len(q) != 0:
        return 'no'
    else:
        return 'yes'


# main 함수 ----------
while True:
    string = input().rstrip()
    if string == '.':
        break
    print(solve(string))
