# 백준 1700

'''
처음에는 멀티탭이 꽉 찰때까지 플러그를 전부 다 꽂는다.
그 뒤 각 플러그에 대해 이후 사용되는 시기가 더 많이 남은 플러그를 제거한다.
위 사항을 반복하여 개수를 세면 된다.
'''

import sys

input = sys.stdin.readline
INF = 1000


# num 전기용품이 현재 번호 cur로부터 몇 번 뒤에 사용되는지 반환
def findRemain(curIndex, num):
    for i in range(curIndex+1, len(sequence)):
        if sequence[i] == num:
            return i-curIndex
    
    # 이후에 num 전기용품을 사용하지 않는 경우
    return INF


def solve():
    result = 0
    tap = set()     # 멀티탭에 꽂힐 전자제품 번호 저장
    index = 0
    
    # K번의 입력에 대해 반복
    while index < K:
        # 멀티탭이 아직 다 차지 않은 경우
        if len(tap) < N:
            if sequence[index] not in tap:
                tap.add(sequence[index])
            else:
                index += 1
            continue
        
        # 현재 사용해야 하는 전자제품이 이미 꽂혀있는 경우
        if sequence[index] in tap:
            index += 1
            continue
        
        # 재사용 시간이 가장 긴 전자제품 탐색
        remain = [0, 0]     # [재사용 시간이 가장 긴 전자제품 번호, 남은 시간]
        for num in tap:
            switchTime = findRemain(index, num)
            if switchTime > remain[1]:
                remain = [num, switchTime]
        
        # 재사용 시간이 가장 긴 전자제품 제거 후 새로운 전자제품 추가
        tap.remove(remain[0])
        tap.add(sequence[index])
        result += 1

    return result


# main 함수 ----------
N, K = map(int, input().split())
sequence = list(map(int, input().split()))

print(solve())