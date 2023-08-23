# 백준 1427

'''
0 < N <= 1,000,000,000이므로 최대 10자리 수이다.
이 수로 문자열로 변환하고 list를 만들 경우 최대 10개의 수를 정렬하는 것이므로 2초 내에 수행 가능하다.
따라서 sort()함수를 이용한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int) -> str:
    arr = list(str(N))
    return ''.join(sorted(arr, reverse=True))


def main():
    N = int(input())
    print(solve(N))

main()
