# 백준 14098

'''
2002번 문제와 동일하다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, start: list, end: list) -> int:
    DP = [1 for i in range(N)]

    car = dict()
    
    # 터널에 들어간 순서대로 차량 번호판에 숫자 할당
    for i in range(N):
        car[start[i]] = i
    
    # 터널에 나온 순서대로 할당된 숫자 저장
    seq = []
    for i in range(N):
        seq.append(car[end[i]])

    # DP를 이용해 LIS 계산
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if seq[i] > seq[j]:
                count += 1
                break

    return count


def main():
    N = int(input())
    start = []
    end = []
    for _ in range(N):
        start.append(input().rstrip())
    for _ in range(N):
        end.append(input().rstrip())

    print(solve(N, start, end))


main()