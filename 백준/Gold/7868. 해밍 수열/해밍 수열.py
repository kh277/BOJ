# 백준 7868

'''
p_1, p_2, p_3을 3중첩 for문으로 돌리면서 가능한 모든 수를 리스트에 저장하고 정렬한 뒤
i번째 수를 출력한다.
'''

import sys
import math

input = sys.stdin.readline
INF = 10e18

def solve():
    hamming = set()
    
    for x in range(int(math.log(INF, p_1))+1):
        for y in range(int(math.log(INF, p_2))+1):
            for z in range(int(math.log(INF, p_3))+1):
                hamming.add(p_1**x * p_2**y * p_3**z)
    
    hamming = sorted(list(hamming))
    return hamming[i]


# main 함수 ------------
p_1, p_2, p_3, i = map(int, input().split())

print(solve())