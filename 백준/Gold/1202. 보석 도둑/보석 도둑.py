# 백준 1202

'''
N개의 보석을 K개의 가방에 나눠 담는 경우의 최대값을 구하는 문제.

가방은 담을 수 있는 최대 무게 순으로 정렬한다.
또한 보석을 무게 오름차순으로, 무게가 같으면 가치 내림차순으로 정렬한다.

가방 기준으로 탐색을 하는데,
가방 무게 제한보다 작은 보석 중 가치가 제일 높은 보석을 넣으면 된다.
'''

import sys
import heapq

input = sys.stdin.readline

def solve(N: int, K: int, data: list, bag: list) -> int:
    # 가방은 무게제한 오름차순으로 정렬한다.    
    bag.sort()

    # 보석은 무게 오름차순, 가치 내림차순으로 정렬한다.
    data.sort(key= lambda x: [x[0], -x[1]])

    result = 0      # 보석의 총 가격 저장
    index = 0       # 탐색한 보석의 인덱스 저장
    hq = []

    for cur in range(K):
        bag_limit = bag[cur]

        # bag_limit보다 작은 무게의 보석은 전부 우선순위 큐에 삽입 
        while True:
            # 보석을 전부 우선순위 큐에 넣은 경우 탈출
            if index >= N:
                break

            # 우선순위 큐에 보석 넣기
            if data[index][0] <= bag_limit:
                heapq.heappush(hq, -1 * data[index][1])
                index += 1
            
            # 보석의 무게가 가방보다 큰 경우 탈출
            else:
                break

        # 가장 가치가 큰 보석 꺼내기
        if len(hq) > 0:
            result += -1 * heapq.heappop(hq)
    
    return result


def main():
    N, K = map(int, input().split())
    
    # [[보석무게1, 보석가격1], ...] 형태로 저장
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    
    # [무게제한1, 무게제한2, ...]
    bag = []
    for _ in range(K):
        bag.append(int(input()))
    
    print(solve(N, K, data, bag))


main()

'''
주의 반례
9 5
4 5
4 9
4 10
8 55
14 20
9 15
8 55
8 5
11 54
10
5
4
15
20
-> 183

3 3
20 12
0 20
16 16
17
14
7
-> 36
'''