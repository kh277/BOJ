# 백준 2170

import sys

input = sys.stdin.readline
INF = 10e10


def solve(N: int, line: list) -> list:
    line.sort(key= lambda x: (x[0], x[1]))
    
    # 초기값
    result = 0
    start = line[0][0]
    end = line[0][1]
    
    # 이후 반복
    for i in range(1, N):
        cur_start, cur_end = line[i]

        # 현재 선분의 시작점이 이미 그려진 선 내부에 있는 경우
        if start <= cur_start <= end:
            if cur_end > end:
                end = cur_end
        
        # 현재 선분의 시작점이 이미 그려진 선 이후에 있는 경우
        elif end < cur_start:
            result += end - start
            start = cur_start
            end = cur_end
            
    result += end - start
    return result


def main():
    N = int(input())
    line = []
    for _ in range(N):
        line.append(list(map(int, input().split())))
    
    print(solve(N, line))


main()