# 백준 2805

'''
나무를 자르는 길이가 M에 근접하도록 이분 탐색으로 범위를 줄여가며 찾아야 한다.
다만, 나무를 자르는 길이가 0 이상의 정수이므로, 소수점 범위로 내려가지 않도록 주의해야 한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, M: int, tree: list) -> int:
    start = 0
    end = max(tree)
    
    while True:
        # 탈출조건 - mid가 소수점 이하로 가는 경우
        if end - start == 1:
            return start
        
        mid = (end+start) // 2
        
        result = 0
        # mid 높이로 나무를 잘랐을 경우 나오는 나무 길이
        for i in tree:
            if i > mid:
                result += i - mid
        
        # 이분 탐색
        if result > M:
            start = mid
        elif result < M:
            end = mid
        else:
            return mid


def main():
    N, M = map(int, input().split())
    tree = list(map(int, input().split()))
    
    print(solve(N, M, tree))


main()
