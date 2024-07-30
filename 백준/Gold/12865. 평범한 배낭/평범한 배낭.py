# 백준 12865

'''
무게제한 K를 넘지 않으면서 가치가 최대가 되는 조합 찾기
        0   1   2   3   ...   K
물건1
물건2
...
물건N

형태로 DP 테이블을 구성한다.

주의 반례
1 13
2 5
-> 5
'''

import sys

input = sys.stdin.readline


# N: 물건의 개수, K: 무게 제한, bag: 물건 정보
def solve(N: int, K: int, bag: list):
    DP = [[0 for _ in range(K+1)] for _ in range(N+1)]

    # 물건 순서대로 탐색
    # i: 현재 탐색하는 물건 번호
    for i in range(1, N+1):
        cur_weight, cur_value = bag[i-1]
        # 현재 무게에 해당 물건을 넣고 갱신할 수 있는 경우 넣기
        # j: 현재 탐색하는 무게
        for j in range(1, K+1):
            # cur 물건을 넣는 경우
            if j-cur_weight >= 0:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j-cur_weight]+cur_value, DP[i-1][j])
            # cur 물건을 넣지 않는 경우
            else:
                DP[i][j] = max(DP[i][j-1], DP[i-1][j])

    return DP[N][K]


def main():
    N, K = map(int, input().split())
    
    bag = []
    for i in range(N):
        W, V = map(int, input().split())
        bag.append([W, V])
    
    print(solve(N, K, bag))


main()