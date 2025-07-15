# 백준 22274

'''
DP[i] = 현재 입력한 키가 i일 때의 조건을 만족하는 경우의 수
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 1000000007


# arr에서 target 이상인 첫 번째 요소의 인덱스 반환
def LowerBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


# arr에서 target보다 큰 첫 번째 요소의 인덱스 반환
def UpperBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid

    return start


def solve(K, L, N, cost, need):
    curDP = array('i', [1]) * K

    for i in range(2, N+1):
        curMin = max(0, need[i-2] - L)
        curMax = need[i-2] + L
        imos = [0 for _ in range(K)]
        for curK in range(K):
            # 이분 탐색으로 구간 [curMin, curMax]에 속하는 수의 범위 찾기
            left = LowerBound(cost[curK], curMin)
            right = UpperBound(cost[curK], curMax)

            # 차분 배열에 값 누적
            if left < K and cost[curK][left] <= curMax:
                imos[left] += curDP[curK]
                if right < K:
                    imos[right] -= curDP[curK]

        # 차분 배열에 저장된 값으로 다음 DP 계산
        nextDP = array('I', [0]) * K
        nextDP[0] = imos[0] % MOD
        for j in range(1, K):
            nextDP[j] = (nextDP[j-1] + imos[j]) % MOD

        # DP 갱신
        curDP = nextDP

    return sum(curDP) % MOD


def main():
    K, L = map(int, input().split())
    cost = []
    for _ in range(K):
        cost.append(list(map(int, input().split())))
    N = int(input())
    need = list(map(int, input().split()))

    print(solve(K, L, N, cost, need))


main()
