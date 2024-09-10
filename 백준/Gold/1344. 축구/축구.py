# 백준 1344

'''
5분 간격으로 총 90분 경기이므로 간격은 총 18개가 된다.

적어도 라는 말이 있으므로 1 - (여사건)을 이용하자.

(적어도 한 팀이 소수로 득점) = 1 - (두 팀이 모두 합성수로 득점)
(두 팀이 모두 합성수로 득점) = (A팀 점수 합성수) * (B팀 점수 합성수)
(A팀 점수 합성수) = (18경기 중 0점) + (18경기 중 1점) + (18경기 중 4점) + ... (18경기 중 18점)
(A팀이 18경기 중 k점 득점) = 18Ck * (a팀이 이길 확률)^k * (1-a팀이 이길 확률)^(18-k)

이항계수를 계산해야 하므로 DP와 파스칼의 삼각형을 이용하여 값을 미리 저장해두자.
'''

import sys

input = sys.stdin.readline

def Paskal(N: int, DP: list) -> list:
    for i in range(1, N+1):
        for j in range(i+1):
            # 파스칼 삼각형에서 값이 1인 이항계수들
            if i == j or j == 0:
                DP[i][j] = 1
            # 점화식
            else:
                DP[i][j] = (DP[i-1][j-1] + DP[i-1][j])
                
    return DP


def solve(A: int, B: int) -> float:
    # 18번의 경기가 진행되므로 1C0 ~ 18C18까지 미리 구해둠 
    DP = Paskal(18, [[0 for _ in range(19)] for _ in range(19)])
    comp = {0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18}
    
    # A팀의 점수가 합성수일 확률
    P_A = 0
    for i in comp:
        P_A += DP[18][i] * (A/100)**i * (1-A/100)**(18-i)
    
    # B팀의 점수가 합성수일 확률
    P_B = 0
    for i in comp:
        P_B += DP[18][i] * (B/100)**i * (1-B/100)**(18-i)
    
    return 1 - P_A * P_B


def main():
    A = int(input())
    B = int(input())
    
    print(solve(A, B))


main()