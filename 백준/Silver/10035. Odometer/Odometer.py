# 백준 10035

'''
X, Y의 범위가 10^16이긴 하지만, 한 글자만 다른 값을 판단하면 되므로,
3자리 수가 moo인 경우 : 9*3
4자리 수가 moo인 경우 : 9*4
...
15자리 수가 moo인 경우 : 9*15
이므로 브루트포스로 계산할 경우 9*9*117 = 약 10000번 연산으로 가능하다.
'''

import sys

input = sys.stdin.readline


def solve():
    lengthY = len(str(Y))
    lengthX = len(str(X))
    result = 0

    for digit in range(lengthX, lengthY+1):     # 반복할 수의 길이 선택
        for i in range(digit-1, -1, -1):        # 반복할 자리수 선택
            for j in range(10):                 # 하나만 다른 0~9까지의 수 반복
                for k in range(10):             # 나머지가 다 같은 0~9까지의 수 반복
                    cur = str(k)*i + str(j) + str(k)*(digit-i-1)
                    if j != k and X <= int(cur) <= Y and cur[0] != '0':
                        result += 1
    
    return result


# main 함수 ----------
X, Y = map(int, input().split())
print(solve())
