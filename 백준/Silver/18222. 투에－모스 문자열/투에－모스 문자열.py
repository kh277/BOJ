# 백준 29445

'''
단순히 X의 i번째 자리 숫자는 숫자 i-1을 이진수로 표현했을 때,
1의 개수가 짝수개이면 0, 홀수개이면 1과 같다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# num에서 1의 개수 세기
def countOne(num):
    count = 0
    while num:
        num &= (num - 1)
        count += 1

    return count


def solve():
    return countOne(k-1) % 2


# main 함수 ----------
k = int(input())
print(solve())
