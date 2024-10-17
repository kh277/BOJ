# 백준 2141

'''
시도1
우체국을 세울 위치가 x일 때, 다른 마을에서 x까지의 거리 합을 나타내보면
y = (거리1)*|x-거리1| + (거리2)*|x-거리2| + ... 이다.
이 그래프는 항상 아래로 볼록이므로 이분 탐색을 통해 거리가 최소인 점을 도출하면 된다.

시도2
시도1에서는 시간초과가 발생했다.
그리디하게 생각해보면, 우체국의 좌측, 우측에 있는 사람의 수가 같을 경우가 최적이 된다.
'''

import sys

input = sys.stdin.readline


def solve():
    point.sort(key= lambda x: x[0])
    
    middle = 0
    for i in range(N):
        middle += point[i][1]
    middle /= 2     # 양쪽에 사람의 수가 균등하게 분배될 때의 점이 최적
    
    accSum = 0
    index = 0
    while True:
        accSum += point[index][1]
        if accSum >= middle:    # 중간값을 넘은 경우 index 반환
            break
        index += 1
    
    return point[index][0]


# main 함수 ----------
N = int(input())

point = []
for _ in range(N):
    point.append(list(map(int, input().split())))

print(solve())