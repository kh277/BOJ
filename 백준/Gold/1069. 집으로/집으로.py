# 백준 1069

import sys
import math

input = sys.stdin.readline

def solve():
    # 피타고라스 공식으로 원점까지의 거리 구하기
    L = math.sqrt(X**2 + Y**2)
    
    # 점프보다 걷기가 더 빠른 경우
    if D <= T:
        return L
    
    result = L
    
    # 점프 한 번 이내로 도착할 수 있는 경우
    if L <= D:
        # min(집까지 걸어가기, 점프해서 집을 넘어간 뒤 걸어서 되돌아오기, 점프 2번으로 집에 도착하기) 
        result = min(result, (D-L)+T, 2*T)
    
    # 점프 두 번 이내로 도착할 수 있는 경우
    elif L <= 2*D:
        # min(1번 점프 후 남은 거리 걸어가기, 점프 2번으로 집에 도착하기)
        result = min(result, T+(L-D), 2*T)
        
    # 점프 세 번 이상 걸리는 경우
    else:
        jump_count = L//D - 1       # 무조건 점프를 하는게 이득이므로 2번 남을때까지 점프
        # jump_count번 점프 후 점프 두번 이내로 도착하는 경우 계산
        result = min(result, jump_count*T + T + (L%D), jump_count*T + 2*T)
        
    return result


# main 함수 ----------
X, Y, D, T = map(int, input().split())
print(solve())