# 백준 12034

'''
오름차순으로 정렬할 경우, 가장 작은 값은 무조건 할인가격이 된다.
할인가격, 그 할인가격과 매칭되는 정상가격을 제거하고 위 과정을 반복하면 된다.
'''


import sys

input = sys.stdin.readline


def solve(N: int, cost: list) -> list:
    cost.sort()
    visited = [False for _ in range(N*2)]     # 방문처리
    discount = []       # 할인가격
    
    for i in range(N*2):
        if visited[i] == True:
            continue
        
        # 방문하지 않은 점 방문 표시
        discount.append(cost[i])
        visited[i] = True

        # 원가에 해당하는 값 처리
        for j in range(N*2):
            if cost[j] == cost[i]*4//3 and visited[j] == False:
                visited[j] = True
                break

    return discount


def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        cost = list(map(int, input().split()))
        print("Case #{a}: ".format(a=i+1), end="")
        print(*solve(N, cost))


main()
