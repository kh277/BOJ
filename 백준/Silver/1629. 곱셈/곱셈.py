# 백준 1629

'''
A를 N번 곱하는 결과를 구하는 경우 일반적으로 O(N)의 시간이 걸린다.
분할정복을 이용하여 결과를 구하는 경우 O(logN)의 시간이 걸리게 된다.

ex) k^16 = k^8 * k^8 = (k^4 * k^4) * (k^4 * k^4) = ... 과 같이 분할정복 진행

아래 코드에서 temp와 같이 미리 계산한 뒤 저장하는 방식이 아니라
저장하지 않고 각각 재귀를 하여 곱할 경우 메모리 초과가 발생함.
'''

import sys

input = sys.stdin.readline


def recur(A: int, B: int, C: int) -> int:
    # 탈출 조건1
    if B == 1:
        return A % C
    
    else:
        temp = recur(A, B//2, C)

        # 짝수일 경우
        if B % 2 == 0:
            return (temp * temp) % C
    
        # 홀수일 경우
        else:
            return (temp * temp * A) % C


def main():
    A, B, C = map(int, input().split())

    print(recur(A, B, C))


main()