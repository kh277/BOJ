# 백준 1654

'''
1. 각 값의 평균을 구함 -> 각 랜선의 길이를 평균으로 나눔
-> N을 만족할 때까지 1씩 증가시키며 반복 -> O(N^2)

2. 이진 탐색으로 풀 경우 O(NlogN)으로 해결 가능.
-> N개를 만들 수 있는 최대 길이를 어떻게 이진 탐색으로 해결?
-> 이진 탐색 범위를 1 ~ (가장 긴 랜선)으로 잡고 이진 탐색

주의사항 : 이진 탐색을 사용할 경우, 랜선의 길이에 따른 오버플로우 발생 가능.
'''

import sys
input = sys.stdin.readline


# line을 length로 잘랐을 때 나오는 등분 수 반환
def check(length: int, line: list) -> int:
    result = 0
    for i in line:
        result += i // length
    
    return result


def solve(N: int, start: int, end: int, line: list) -> int:
    
    # 재귀의 마지막에 도달한 경우
    if end - start == 1:
        if check(end, line) == N:
            return end
        else:
            return start

    mid = (start + end)//2

    # mid 길이로 잘랐을 때 등분 수보다 목표 수가 큰 경우
    if check(mid, line) < N:
        return solve(N, start, mid, line)

    # mid 길이로 잘랐을 때 등분 수보다 목표 수가 작은 경우
    else:
        return solve(N, mid, end, line)


def main():
    K, N = map(int, input().split())
    line = [0 for _ in range(K)]

    for i in range(K):
        line[i] = int(input())

    print(solve(N, 1, 2**31-1, line))


main()