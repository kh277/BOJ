# 백준 27188

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# f(start, end)의 값 반환
def digitLength(start, end):
    result = 0

    if start == 0:
        result += 1
        start = 1

    for i in range(1, 20):
        left = max(start, 10**(i - 1))
        right = min(end, 10**i - 1)
        if left > right:
            continue
        result += (right - left + 1) * i
        if right == end:
            break

    return result


def solve():
    if S <= 10:
        return [[S], [0, S-1]]

    # start를 브루트포스로 고정시키고, 그 start에 대해 이분 탐색으로 적절한 end 찾기
    for start in range(100000):
        left = start
        right = 10**18
        
        while left < right:
            mid = (left + right) // 2
            if digitLength(start, mid) < S:
                left = mid + 1
            else:
                right = mid
        
        if digitLength(start, left) == S:
            return [[left - start + 1], [start, left]]
    
    return [[-1]]


# main 함수 ----------
S = int(input())

for i in solve():
    print(*i)