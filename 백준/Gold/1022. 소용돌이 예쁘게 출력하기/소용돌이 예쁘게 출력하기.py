# 백준 1022

'''
소용돌이의 전체 모습은 항상 고정되어 있으므로
전체 모습을 구하고 입력 범위만 잘라서 출력하자.
'''

import sys

input = sys.stdin.readline


# cur이 start~end 좌표 내의 점인지 확인
def check_range(N: int, start: list, end: list, cur: list) -> bool:
    if start[0]+N <= cur[0] <= end[0]+N:
        if start[1]+N <= cur[1] <= end[1]+N:
            return True
    
    return False


def solve(start: list, end: list) -> list:
    # 구해야 할 소용돌이의 반지름 찾기
    N = max(abs(start[0]), abs(start[1]), abs(end[0]), abs(end[1]))

    # (-N, -N) ~ (N, N)까지의 소용돌이 그리기
    result = [[0 for _ in range(end[1]-start[1]+1)] for _ in range(end[0]-start[0]+1)]

    # (전체 좌상단) ~ (출력해야 할 부분의 좌상단) 까지의 차이 구하기
    yGap = start[0]+N
    xGap = start[1]+N

    # 숫자 1은 직접 입력
    if check_range(N, start, end, [N, N]):
        result[N-yGap][N-xGap] = 1
    temp = 2

    # 이후 소용돌이에 대해 반복 및 인덱스에 맞는 경우 데이터 추가
    for k in range(1, N+1):
        for i in range(N+k-1, N-k, -1):
            if check_range(N, start, end, [i, N+k]):
                result[i-yGap][N+k-xGap] = temp
            temp += 1
        
        for i in range(N+k, N-k-1, -1):
            if check_range(N, start, end, [N-k, i]):
                result[N-k-yGap][i-xGap] = temp
            temp += 1
        
        for i in range(N-k+1, N+k):
            if check_range(N, start, end, [i, N-k]):
                result[i-yGap][N-k-xGap] = temp
            temp += 1
        
        for i in range(N-k, N+k+1):
            if check_range(N, start, end, [N+k, i]):
                result[N+k-yGap][i-xGap] = temp
            temp += 1
    
    # 리스트에서 최대 길이를 가진 수 추출
    ySize = end[0]-start[0]+1
    xSize = end[1]-start[1]+1
    max_len = 0
    for y in range(ySize):
        for x in range(xSize):
            result[y][x] = str(result[y][x])
            if max_len < len(result[y][x]):
                max_len = len(result[y][x])

    # 숫자 앞쪽에 공백 추가
    for y in range(ySize):
        for x in range(xSize):
            gap = max_len - len(result[y][x])
            result[y][x] = ' '*gap + result[y][x]

    return result


def main():
    r1, c1, r2, c2 = map(int, input().split())
    for i in solve([r1, c1], [r2, c2]):
        print(*i)


main()


'''
생각1
    (0, 0) ~ (0, 0) : 1
    (-1, -1) ~ (1, 1) : 2 ~ 9 (1^2+1 ~ 3^2)
    (-2, -2) ~ (2, 2) : 10 ~ 25 (3^2+1 ~ 5^2)
        ...
    (-n, -n) ~ (n, n) : (2n-1)^2+1 ~ (2n+1)^2이다.
    따라서 가장 바깥쪽 숫자는 4n^2 - 4n + 2 ~ 4n^2 + 4n + 1까지의 수이므로
    8n개가 들어갈 수 있다.


생각2
소용돌이에서 숫자가 증가하는 순서대로 형태를 잡아보면,
---
| |
--- 의 모양이 되고, 해당 도형에서 ---는 2n+1개의 숫자가, |는 2n-1개의 숫자가 들어가게 된다.


생각3
문제에서 주어진 소용돌이의 좌표에서 인덱스로 접근하기 위해

    -3 -2 -1  0  1  2  3
    --------------------
-3 |37 36 35 34 33 32 31
-2 |38 17 16 15 14 13 30
-1 |39 18  5  4  3 12 29
 0 |40 19  6  1  2 11 28
 1 |41 20  7  8  9 10 27
 2 |42 21 22 23 24 25 26
 3 |43 44 45 46 47 48 49


아래와 같이 좌표를 수정하여 저장하자.

     0  1  2  3  4  5  6
    --------------------
 0 |37 36 35 34 33 32 31
 1 |38 17 16 15 14 13 30
 2 |39 18  5  4  3 12 29
 3 |40 19  6  1  2 11 28
 4 |41 20  7  8  9 10 27
 5 |42 21 22 23 24 25 26
 6 |43 44 45 46 47 48 49

이 경우, 숫자 1은 (3, 3)에 위치하게 된다.

위와 같이 N가 N인 즉 숫자 1을 두르는 소용돌이의 개수가 N의 경우,
숫자 1은 (N, N)에 위치한다.
숫자 1을 두르는 첫 번째 소용돌이(2~9)의 시작점(숫자 2)의 위치는 (N, N+1)이고,
숫자 1을 두르는 두 번째 소용돌이(10~25)의 시작점(숫자 10)의 위치는 (N+1, N+2)이다.
가장 바깥쪽의 소용돌이((2n-1)^2+1~(2n+1)^2)의 시작점(숫자 (2n-1)^2+1)의 위치는 (2N-1, 2N)이다.

숫자 1을 두르는 첫 번째 소용돌이(2~9)의 범위를 생각2에서처럼 분리해보면
(N, N+1)~(N, N+1), (N-1, N+1)~(N-1, N-1), (N, N-1)~(N, N-1), (N+1, N-1)~(N+1, N+1)가 된다.
숫자 1을 두르는 두 번째 소용돌이(10~25)의 범위를 생각2에서처럼 분리해보면
(N+1, N+2)~(N-1, N+2), (N-2, N+2)~(N-2, N-2), (N-1, N-2)~(N+1, N-2), (N+2, N-2)~(N+2, N+2)가 된다.
k번째 소용돌이((2k-1)^2+1~(2k+1)^2)의 범위를 생각2에서처럼 분리해보면
(N+k-1, N+k)~(N-k+1, N+k), (N-k, N+k)~(N-k, N-k), (N-k+1, N-k)~(N+k-1, N-k), (N+k, N-k)~(N+k, N+k)가 된다.
'''
