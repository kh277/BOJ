# 백준 10799

'''
'('일 때 나타난 레이저의 개수를 저장하고, ')'일 때, 스택에서 수를 하나 꺼낸다.
(현재 레이저 개수) - (꺼낸 수) + 1을 누적해서 계산하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(A):
    N = len(A)
    stack = []
    result = 0
    lazer = 0
    index = 0
    while index < N:
        # 여는 괄호라면
        if A[index] == '(':
            # 레이저라면
            if index < N-1 and A[index+1] == ')':
                index += 1
                lazer += 1
            else:
                stack.append(lazer)
        # 닫는 괄호라면
        else:
            start = stack.pop()
            result += lazer - start + 1
        
        index += 1
    
    return result


def main():
    A = list(input().decode().strip())
    print(solve(A))


main()
