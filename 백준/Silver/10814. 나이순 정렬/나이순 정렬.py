# 백준 10814

'''
조건이 두 개 이상이므로 key= labmda를 이용하자.

주의 사항
int와 string은 정렬 기준이 다르다!
3, 2, 21을 string으로 정렬했다면 2, 21, 3이 되고,
int로 정렬했다면 2, 3, 21이 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, data: list) -> list:

    # 나이순, 가입순 정렬
    data.sort(key= lambda x: (int(x[0]), x[2]))

    # 가입순서는 제외하고 출력
    return [x[:2] for x in data]


def main():
    N = int(input())

    data = []
    for i in range(N):
        a, b = map(str, input().split())
        data.append([a, b, i])

    for i in solve(N, data):
        print(*i)


main()