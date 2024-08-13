# 백준 7579

'''
생각1-----
N개의 앱 A_1, A_2, ..., A_n이 활성화되어 있고,
각각의 앱들은 m_1, m_2, ..., m_n만큼의 메모리를 차지하고 있다.
또한 앱을 비활성화하려면 c_1, c_2, ..., c_n만큼의 비용이 든다.

이는 m_1, m_2, ..., m_n 만큼의 무게를 차지하는 N개의 물건 중 몇 개를 골라,
이 물건들의 무게의 합이 M 이상이고, 가치의 합이 최소가 되도록 해야 한다.

뒤집어 말하면, 남겨진 앱들의 메모리 합이 sum(weight) - M 이하가 되면서,
비용의 합이 최대가 되도록 하면 된다.

생각2-----
DP 테이블의 세로줄을 물건의 개수, 가로줄을 memory로 두고 진행했다.
이 경우 sum(memory) 값이 최대 100 * 10^7이므로 메모리 초과가 발생한다.

따라서 세로줄을 물건의 개수, 가로줄을 cost로 두고 해당 인덱스의 값 안에 memory를 넣는 방식으로 바꾸자.

최적화-----
차지하고 있는 메모리가 M 이상인 앱들은 따로 제외한다.
나머지 앱들로 DP를 진행하고, 결과값과 M 이상인 앱들의 cost를 비교해서 더 작은 값을 반환한다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, M: int, memory: list, cost: list) -> int:
    max_cost = sum(cost)

    heavy_app = []
    bag = []
    for i in range(N):
        # 메모리가 M 이상인 앱들은 따로 모으기
        if memory[i] >= M:
            heavy_app.append([memory[i], cost[i]])
        else:
            bag.append([memory[i], cost[i]])

    DP = [[0 for _ in range(max_cost+1)] for _ in range(len(bag)+1)]

    # 물건 순서대로 탐색
    # i: 현재 탐색하는 물건 번호
    for i in range(1, len(bag)+1):
        cur_weight, cur_cost = bag[i-1]
        # 현재 무게에 해당 물건을 넣고 갱신할 수 있는 경우 넣기
        # j: 현재 탐색하는 물건의 가치
        for j in range(max_cost+1):
            # cur 물건을 넣는 경우
            if j-cur_cost >= 0:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j-cur_cost]+cur_weight, DP[i-1][j])
            # cur 물건을 넣지 않는 경우
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])

    # DP 테이블에서 최소 가치 도출
    min_cost = 10e6
    for i in range(max_cost+1):
        if DP[len(bag)][i] >= M:
            min_cost = i
            break

    # 차지하는 memory가 M 이상인 앱들과 최소값 비교
    result = min_cost
    for i in heavy_app:
        result = min(i[1], result)

    return result


def main():
    N, M = map(int, input().split())
    memory = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    print(solve(N, M, memory, cost))


main()