# 백준 32631

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**13


# bag 가방에서 [0, K]개의 물건을 제외했을 때 남은 배낭의 최소 무게 반환
def calWeight(N, K, bag):
    # 각 가방 별 누적합 계산
    accSum = [0] * N
    accSum[0] = bag[0]
    for i in range(1, N):
        accSum[i] = accSum[i-1] + bag[i]

    # 물건을 i개 제외했을 때의 최소 무게 계산
    result = [INF] * (K+1)
    for i in range(K+1):
        minV = accSum[N-1-i]
        for start in range(1, i+1):
            end = N-1 - i + start
            minV = min(minV, accSum[end] - accSum[start-1])
        result[i] = minV

    return result


def solve(N, K, bag1, bag2):
    # 각 가방에서 물건을 일정 개수 뺐을 때 나오는 최소 무게 구하기
    res1 = calWeight(N, K, bag1)
    res2 = calWeight(N, K, bag2)

    # 각 가방에서 제외하는 물건의 개수를 다르게 해 가며 최적해 탐색
    result = INF
    for i in range(K+1):
        cur = max(res1[i], res2[K-i])
        result = min(result, cur)

    return result


def main():
    N, K = map(int, input().split())
    bag1 = list(map(int, input().split()))
    bag2 = list(map(int, input().split()))
    print(solve(N, K, bag1, bag2))


main()
