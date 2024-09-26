# 백준 2110

'''
최적화 문제 :
N개의 집에 C개의 공유기 설치. 이 때, 가장 인접한 두 공유기 사이의 거리가 최대가 될 때의 거리?

결정 문제 :
가장 인접한 두 공유기 사이의 거리가 x일 때, N개의 집에 C개 이상의 공유기를 설치할 수 있는가?

이분 탐색으로 결정 문제를 만족하는 x의 최대값을 구하자.
단, 주의해야 할 것은 첫 번째 지점은 반드시 공유기가 설치되어야 한다는 것이다.
'''


import sys

input = sys.stdin.readline


# mid만큼 각 지역에 예산이 할당될 때, 사용되는 전체 예산 계산
def check(C: int, mid: int, local: list) -> bool:
    result = 1
    
    before = local[0]       # 처음 공유기 위치는 반드시 처음 집이 되어야 함
    
    for i in range(1, len(local)):
        # 이전 공유기와의 거리가 mid 이상인지 확인 
        if local[i] - before >= mid:
            result += 1
            before = local[i]
    
    if result >= C:
        return True
    else:
        return False


def solve(N: int, C: int, point: int) -> int:
    point.sort()
    
    start = 0
    end = max(point)
    temp = 0
    
    while True:
        # 탈출조건
        if end - start == 1:
            if check(C, end, point) == True:
                return end
            else:
                return start
        
        mid = (end+start) // 2
        
        # 결정 문제 확인
        result = check(C, mid, point)
        
        # 이분 탐색
        temp = mid
        if result == True:
            start = mid
        else:
            end = mid


def main():
    N, C = map(int, input().split())
    
    point = []
    for i in range(N):
        point.append(int(input()))
    
    print(solve(N, C, point))


main()