# 백준 15882

'''
비트마스크에서 요원으로 교체한 경우를 0, 교체하지 않은 경우 1이라고 두자.
3비트 정수 status가 abc일 때, a(i-3번쨰 사람의 교체 여부), b(i-2번째 사람의 교체 여부), c(i-1번째 사람의 교체 여부)로 두면,
이전 3명의 요원 교체 여부가 011이고, 현재 i번째 사람을 요원으로 교체할 경우 = 110
i번째 사람을 교체하지 않는 경우 = 111 처럼 한 칸씩 비트를 왼쪽으로 밀고 현재 상태를 추가하면 전이 상태롤 계산할 수 있다.

DP[i][status] = 현재 i번째 사람을 체크하고 있고, 이전 3명의 요원 교체 여부가 status일 때 행복 지수의 최대값.
DP[i]는 DP[i-1]에만 의존하므로 일차원 DP로 압축할 수 있다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


def solve(N, data):
    prevDP = [0, 0, 0, data[2][2], 0, data[2][1], data[1][2], data[1][2]+data[2][1]+data[2][2]]

    for i in range(4, N+1):
        DP = [-INF] * 8
        for status in range(8):
            # 이전 상태의 요원 여부 추출
            prev3 = (status >> 2) & 1
            prev2 = (status >> 1) & 1
            prev1 = status & 1

            # i번째 사람을 요원으로 대체하는 경우
            nextStatus = (status & 3) << 1
            if DP[nextStatus] < prevDP[status]:
                DP[nextStatus] = prevDP[status]

            # i번째 사람을 그대로 유지하는 경우
            nextStatus += 1
            add = prev3*data[i-1][0] + prev2*data[i-1][1] + prev1*data[i-1][2]
            DP[nextStatus] = max(DP[nextStatus], prevDP[status] + add)

        # DP 테이블 갱신
        prevDP = DP

    return max(prevDP)


def main():
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))

    print(solve(N, data))


main()
