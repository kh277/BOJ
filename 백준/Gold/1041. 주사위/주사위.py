# 백준 1041

'''
N >= 2이고, N * N * N 개의 주사위를 쌓은 정육면체에서,
case1) 세 면이 노출되는 주사위 = 4개
case2) 두 면이 노출되는 주사위 = (N-2)*4 + (N-1)*4개
case3) 한 면이 노출되는 주사위 = (N-2)*(N-2) + 4*(N-2)*(N-1)개

따라서 주사위에서
case1에는 최소가 되는 세 면을
case2에는 최소가 되는 두 면을
case3에는 최소가 되는 면을 할당하는 경우가 최소값이 된다.
'''

import sys

input = sys.stdin.readline


def solve(N: int, num: list) -> int:

    # N이 1일 경우
    if N == 1:
        # 주사위의 최대 숫자 면을 제외한 면의 합이 정답
        return sum(sorted(num)[:5])
    
    # 최소가 되는 세 면
    three = min(
        num[0]+num[1]+num[2], 
        num[0]+num[1]+num[3],
        num[0]+num[2]+num[4],
        num[0]+num[3]+num[4],
        num[1]+num[2]+num[5],
        num[1]+num[3]+num[5],
        num[2]+num[4]+num[5],
        num[3]+num[4]+num[5])
    
    # 최소가 되는 두 면
    two = min(
        num[0]+num[1],
        num[0]+num[2],
        num[0]+num[3],
        num[0]+num[4],
        num[1]+num[2],
        num[1]+num[3],
        num[1]+num[5],
        num[2]+num[4],
        num[2]+num[5],
        num[3]+num[4],
        num[3]+num[5],
        num[4]+num[5])

    # 최소가 되는 면
    one = min(num)

    # case1 + case2 + case3
    return 4 * three + (8*N-12) * two + (5*N**2 - 16*N + 12) * one


def main():
    N = int(input())
    num = list(map(int, input().split()))

    print(solve(N, num))


main()
