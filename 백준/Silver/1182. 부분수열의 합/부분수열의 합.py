# 백준 1182

'''
N <= 20이므로 재귀를 통해 다 더한 값이 20이 되는지 확인하자.
백트래킹을 이용해 index를 하나씩 증가시키면서
해당 원소를 포함하는 경우, 포함하지 않는 경우를 나눠서 재귀한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, S: int, num: list, index: int, sum: int) -> int:
    count = 0

    # 종료 조건
    if index == N:
        return count
    
    # 현재 위치의 값을 더해서 S가 되는지 확인
    sum += num[index]
    if sum == S:
        count += 1

    # index를 포함한 경우의 가지    
    count += solve(N, S, num, index+1, sum)

    # index를 포함하지 않은 경우의 가지
    count += solve(N, S, num, index+1, sum - num[index])

    return count


def main():
    N, S = map(int, input().split())
    num = list(map(int, input().split()))

    print(solve(N, S, num, 0, 0))

main()