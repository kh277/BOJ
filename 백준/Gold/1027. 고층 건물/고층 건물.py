# 백준 1027

'''
A빌딩에서 B빌딩까지 직선을 긋고 중간에 겹치는 빌딩이 없다는 것은
A빌딩에서 B빌딩을 볼 수 있다는 것을 의미한다.

따라서 위 전략을 모든 빌딩에 대해 브루트포스로 적용시킨다.
'''

import sys

input = sys.stdin.readline


def check(building: list, i: int, cur: int) -> bool:
    # i와 cur이 일치한다면
    if cur == i:
        return False

    # i가 cur의 왼쪽에 있다면
    elif cur > i:
        for x in range(i+1, cur):
            # (i, building[i])에서 (cur, building[cur])점까지의 직선의 방정식
            y = (building[cur] - building[i]) / (cur - i) * (x - i) + building[i]
                
            # 중간 빌딩이 직선보다 크거나 같다면 
            if y <= building[x]:
                return False
            
        return True
    
    # i가 cur의 오른쪽에 있다면
    elif cur < i:
        for x in range(cur+1, i):
            # (cur, building[cur])에서 (i, building[i])점까지의 직선의 방정식
            y = (building[cur] - building[i]) / (cur - i) * (x - i) + building[i]
                
            # 중간 빌딩이 직선보다 크거나 같다면 
            if y <= building[x]:
                return False
            
        return True


def solve(N: int, building: list) -> int:
    result = 0

    # 기준점
    for cur in range(N):
        count = 0

        # i에서 cur까지의 직선을 긋고, 중간에 가리는 빌딩이 있는지 확인
        for i in range(N):
            if check(building, i, cur):
                count += 1

        if count > result:
            result = count

    return result


def main():
    N = int(input())
    building = list(map(int, input().split()))

    print(solve(N, building))
    

main()