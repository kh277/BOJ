# 백준 1229

'''
육각수는 h_n = 2*n^2 - n의 식을 따른다.
따라서 육각수의 값들을 계산하여 미리 저장해두고,
문제에 나온 1~12까지의 값들을 DP테이블에 초기값으로 저장해둔다.
그 뒤, DP[i] = min(DP[i - 육각수]+1)으로 이후 값을 처리한다.

ex) DP[16] = min(DP[16-1]+1, DP[16-6]+1, DP[16-15]+1)
    = min(DP[15]+1, DP[10]+1, DP[1]+1)
과 같이 계산하면 된다.
'''

import sys

input = sys.stdin.readline


# N 이하의 육각수 반환
def make_hexa(limit: int) -> list:
    temp = []
    
    index = 1
    n = 0
    while True: 
        n = 2 * index**2 - index    # 점화식
        
        # 탈출조건
        if n > limit:
            break
        
        temp.append(n)
        index += 1
        
    return temp


def solve(N: int) -> int:
    hexa = make_hexa(N)
    # 초기값 + 이후 값
    DP = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2] + [0 for _ in range(13, 1000001)]

    for cur in range(13, N+1):
        min_data = 1000
        for j in hexa:
            # 음수 인덱스를 참조하는 경우
            if j > cur:
                break
            min_data = min(min_data, DP[cur-j])
        DP[cur] = min_data+1
    
    return DP[N]


def main():
    N = int(input())
    
    print(solve(N))
    

main()
