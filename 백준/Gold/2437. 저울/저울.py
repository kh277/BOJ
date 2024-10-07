# 백준 2437

'''
저울 추를 오름차순으로 정렬한 다음 순서대로 측정할 수 있는 무게를 구해본다.

ex)
1, 2, 3인 경우,
초기값 : [0, 0]
1 : [0, 1]
1, 2 : [0, 3]
1, 2, 3 : [0, 6]

추를 하나씩 추가하면서 구간이 끊어지는 경우가 답이 된다.
만약 추를 다 추가했는데도 끊어지지 않는다면, 마지막 값+1이 답이 된다.
'''

import sys

input = sys.stdin.readline


def solve():
    weight.sort()
    
    value = [0, 0]
    
    for i in range(N):
        curValue = [weight[i], weight[i]+value[1]]
        
        # weight 값이 value 범위 내에 들어가는 경우
        if value[1]+1 >= weight[i]:
            value[1] = weight[i]+value[1]
        else:
            return value[1]+1

    return value[1]+1


# main 함수 ----------
N = int(input())
weight = list(map(int, input().split()))

print(solve())