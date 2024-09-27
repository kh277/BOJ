# 백준 22973

'''
직접 계산을 해보면,
1은 1번 점프,
2^1+1 ~ 2^2-1 사이의 홀수는 2번 점프,
2^2+1 ~ 2^3-1 사이의 홀수는 3번 점프,
2^3+1 ~ 2^4-1 사이의 홀수는 4번 점프,
...
와 같은 규칙을 가지는 것을 알 수 있다.

K를 탐색할 때, 로그의 시간복잡도를 가지고,
2^34 < 10^12 < 2^35이므로 35까지 반복하면 된다.
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
    for i in range(2, 36):
        if 2**(i-1) + 1 <= abs(K) <= 2**i - 1:
            return i


def main():
    K = int(input())
    
    print(solve(K))


main()