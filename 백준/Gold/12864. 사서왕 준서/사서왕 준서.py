# 백준 12864

'''
LIS 응용 문제이다.
다만, 기본 LIS와는 다르게,
무게 합이 최대인 증가하는 수열을 찾아야 한다.
그래야 옮기는 책의 무게가 줄어들기 때문이다.
'''

import sys

input = sys.stdin.readline


def solve():
    # [LIS 길이, 총 무게] 순서로 저장
    DP = [[1, weight[i]] for i in range(N)]
    DP[0] = [1, weight[0]]
    
    for i in range(1, N):
        for j in range(i):
            # 책 번호가 증가하면서 무게가 더 무겁다면
            if num[i] >= num[j] and DP[j][1] + weight[i] > DP[i][1]:
                DP[i] = [DP[j][0] + 1, DP[j][1] + weight[i]]
    
    max_data = 0
    for i in DP:
        max_data = max(max_data, i[1])
        
    return sum(weight) - max_data


# main 함수 ----------
N = int(input())
num = list(map(float, input().split()))
weight = list(map(int, input().split()))

print(solve())