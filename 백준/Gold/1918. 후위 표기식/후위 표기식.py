# 백준 1918

'''
문자가 들어올 경우
    -> 그대로 출력한다.

*/가 들어올 경우
    -> 스택에 비어있는 경우 다음 연산자를 append한다. 
    -> 스택에 (가 있는 경우 다음 연산자를 append한다.
    -> 스택에 */가 있는 경우 pop 후 다음 연산자를 append한다.
    -> 스택에 +-가 있는 경우 다음 연산자를 append한다.

(가 들어올 경우
    -> (를 스택에 넣는다.

)가 들어올 경우
    -> (가 나올 때까지 스택에서 연산자를 전부 꺼낸다.    

+-가 들어올 경우
    -> 스택이 비어있는 경우 다음 연산자를 append한다.
    -> 스택에 (가 있는 경우 다음 연산자를 append한다.
    -> 스택이 비어있지 않은 경우 연산자를 전부 pop 한 후, 다음 연산자 +-를 append한다.

문장의 끝에 도달한 경우 스택 내의 연산자를 전부 꺼낸다.
'''

import sys
from collections import deque

input = sys.stdin.readline


def solve(S: str) -> str:
    stack = deque()
    result = ""

    for i in S:
        
        # */가 들어온 경우
        if i == '*' or i == '/':
            # 스택이 비어있거나 (가 있다면
            if not stack or stack[-1] == '(':
                stack.append(i)
            # 스택 위에 */가 있다면
            elif stack[-1] == '*' or stack[-1] == '/':
                result += stack.pop()
                stack.append(i)
            # 스택 위에 +-가 있다면
            else:
                stack.append(i)

        # (가 들어온 경우
        elif i == '(':
            stack.append(i)
        # )가 들어온 경우
        elif i == ')':
            while stack:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    result += stack.pop()

        # +-가 들어온 경우
        elif i == '+' or i == '-':
            # 스택이 비어있거나 (가 있다면
            if not stack or stack[-1] == '(':
                stack.append(i)
            # 스택이 비어있지 않다면
            else:
                while stack:
                    if stack[-1] == '(':
                        break
                    result += stack.pop()
                stack.append(i)
        
        # 문자가 들어온 경우
        else:
            result += i
    
    for i in range(len(stack)):
        result += stack.pop()

    return result


def main():
    S = input().rstrip()

    print(solve(S))


main()