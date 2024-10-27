# 백준 27277

'''
가장 큰 수 부터 작아지는 순서대로 홀수 번째에,
가장 작은 수부터 커지는 순서대로 짝수 번째에 배치하면 최대의 값을 가진다.
'''

import sys

input = sys.stdin.readline


def solve():
    L.append(0)
    L.sort()
    
    result = 0
    for i in range(N//2+1):
        result += L[-i-1] - L[i]

    return result


# main 함수 ----------
N = int(input())
L = list(map(int, input().split()))
print(solve())
