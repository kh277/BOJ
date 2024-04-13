# 백준 2470

import sys

input = sys.stdin.readline


def solve(N: int, L: list) -> list:
    L.sort()
    # 초기값 지정
    result = [L[0], L[-1]]
    pointer_a = 0
    pointer_b = len(L)-1

    # a와 b가 같은 값을 가리킬 때까지 반복
    while True:
        # 탐색을 마친 경우
        if pointer_a == pointer_b:
            return result
        
        cur = L[pointer_a] + L[pointer_b]

        # 1. 두 값을 더한 것이 양수인 경우
        if cur > 0:
            # 갱신 가능한 경우
            if abs(cur) < abs(result[0] + result[1]):
                result = [L[pointer_a], L[pointer_b]]
            pointer_b -= 1
            continue
        
        # 2. 두 값을 더한 것이 음수일 경우
        elif cur < 0:
            # 갱신 가능한 경우
            if abs(cur) < abs(result[0] + result[1]):
                result = [L[pointer_a], L[pointer_b]]
            pointer_a += 1
            continue
        
        # 3. 두 값을 더한 것이 0일 경우
        else:
            return [L[pointer_a], L[pointer_b]]


def main():
    N = int(input())
    L = list(map(int, input().split()))

    print(*solve(N, L))


main()