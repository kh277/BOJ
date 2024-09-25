# 백준 2512

'''
N개의 숫자를 x로 뺐을 때, 빼진 값의 총합이 N 이하가 되도록 하는 x의 상한 구하기
'''

import sys

input = sys.stdin.readline


# mid만큼 각 지역에 예산이 할당될 때, 사용되는 전체 예산 계산
def check(mid: int, local: list) -> int:
    result = 0
    
    for i in local:
        # 지역에서 필요한 예산이 더 작을 경우
        if i < mid:
            result += i
        else:
            result += mid
    
    return result


def solve(N: int, M: int, local: list) -> int:
    start = 0
    end = max(local)
    temp = 0
    
    while True:
        # 탈출조건
        if end - start == 1:
            if check(end, local) > M:
                return start
            else:
                return end
        
        mid = (end+start) // 2
        
        # 전체 예산 계산
        result = check(mid, local)
        
        # 이분 탐색
        temp = mid
        if result > M:
            end = mid
        elif result < M:
            start = mid
        else:
            return mid


def main():
    N = int(input())
    local = list(map(int, input().split()))
    M = int(input())
    
    print(solve(N, M, local))


main()
