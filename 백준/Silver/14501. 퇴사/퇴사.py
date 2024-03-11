# 백준 14501

'''
k일차에 배정된 상담이 a일 걸린다고 치면,
k일차 상담을 끝냈을 때 받는 금액은 max(dp[k-1]+price[k], dp[k+a])가 된다.
그 뒤, 상담을 끝낸 이후 날짜부터 퇴사일까지의 금액을 비교하여 갱신한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, task: list, price: list) -> int:
    dp = [0 for _ in range(N+2)]

    # 1일차부터 N일차까지 모든 상담에 대해
    for i in range(1, N+1):
        # 만약 상담일이 퇴사일을 넘길 경우 스킵
        if i+task[i] > N+1:
            continue

        # i일차 상담을 끝냈을 때 받는 금액 계산 (기존 값과 비교)
        dp[i+task[i]] = max(dp[i]+price[i], dp[i+task[i]])

        # 상담을 끝낸 이후 날짜에 대한 금액 비교 후 갱신
        for j in range(i+task[i]+1, N+2):
            dp[j] = max(dp[i+task[i]], dp[j])

    return dp[N+1]

def main():
    N = int(input())

    task = [0 for _ in range(N + 1)]
    price = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        task[i], price[i] = map(int, input().split())

    print(solve(N, task, price))


main()
