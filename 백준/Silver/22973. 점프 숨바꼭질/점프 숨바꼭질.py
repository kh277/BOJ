# 백준 22973

'''
직접 계산을 해보면,
1은 1번 점프,
2^1+1 ~ 2^2-1 사이의 홀수는 2번 점프,
2^2+1 ~ 2^3-1 사이의 홀수는 3번 점프,
2^3+1 ~ 2^4-1 사이의 홀수는 4번 점프,
...
와 같은 규칙을 가지는 것을 알 수 있다.
'''


import sys

input = sys.stdin.readline


def solve(K: int) -> int:
    # 짝수 경우 제거
    if K == 0:
        return 0
    elif K % 2 == 0:
        return -1
    
    # 1인 경우
    if abs(K) == 1:
        return 1
    
    # 1이 아닌 홀수의 경우
    index = 2
    while True:
        if 2**(index-1) + 1 <= abs(K) <= 2**index - 1:
            return index
        else:
            index += 1


def main():
    K = int(input())
    
    print(solve(K))


main()