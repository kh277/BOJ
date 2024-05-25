# 백준 14500

'''
테트로미노가 2*2이고 종이가 500*500이라고 가정하면,
테트로미노 위의 숫자 최대값은 499*499 = 24만 만큼의 연산을 해야 한다.

따라서 테트리미노를 회전, 대칭 시키는 가능한 가지수를 전부 브루트포스로 계산해도 된다.
y  ,x    y  ,x+1    y  ,x+2    y  ,x+3
y+1,x    y+1,x+1    y+1,x+2    y+1,x+3
y+2,x    y+2,x+1    y+2,x+2    y+2,x+3
y+3,x    y+3,x+1    y+3,x+2    y+3,x+3
'''

import sys

input = sys.stdin.readline

def solve(N: int, M: int, paper: list) -> int:
    
    max_value = 0

    # 1-1. 1*4 모양의 테트로미노 (세로 1칸, 가로 4칸)
    for y in range(N):
        for x in range(M-3):
            temp = paper[y][x] + paper[y][x+1] + paper[y][x+2] + paper[y][x+3]
            if max_value < temp:
                max_value = temp
    
    # 1-2. 4*1 모양의 테트로미노
    for y in range(N-3):
        for x in range(M):
            temp = paper[y][x] + paper[y+1][x] + paper[y+2][x] + paper[y+3][x]
            if max_value < temp:
                max_value = temp
    
    # 2. 2*2 모양의 테트로미노
    for y in range(N-1):
        for x in range(M-1):
            temp = paper[y][x] + paper[y+1][x] + paper[y][x+1] + paper[y+1][x+1]
            if max_value < temp:
                max_value = temp

    # 3-1. 2*2 모양의 테트로미노
    for y in range(N-1):
        for x in range(M-2):
            temp1 = paper[y][x] + paper[y][x+1] + paper[y][x+2] + paper[y+1][x]
            temp2 = paper[y][x] + paper[y][x+1] + paper[y][x+2] + paper[y+1][x+2]
            temp3 = paper[y][x] + paper[y+1][x] + paper[y+1][x+1] + paper[y+1][x+2]
            temp4 = paper[y+1][x] + paper[y+1][x+1] + paper[y+1][x+2] + paper[y][x+2]
            temp5 = paper[y+1][x] + paper[y+1][x+1] + paper[y][x+1] + paper[y][x+2]
            temp6 = paper[y][x] + paper[y][x+1] + paper[y+1][x+1] + paper[y+1][x+2]
            temp7 = paper[y+1][x] + paper[y+1][x+1] + paper[y+1][x+2] + paper[y][x+1]
            temp8 = paper[y][x] + paper[y][x+1] + paper[y][x+2] + paper[y+1][x+1]

            if max_value < max(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8):
                max_value = max(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8)

    # 3-2. 3*2 모양의 테트로미노
    for y in range(N-2):
        for x in range(M-1):
            temp1 = paper[y][x] + paper[y+1][x] + paper[y+2][x] + paper[y+2][x+1]
            temp2 = paper[y][x+1] + paper[y+1][x+1] + paper[y+2][x+1] + paper[y+2][x]
            temp3 = paper[y][x] + paper[y][x+1] + paper[y+1][x] + paper[y+2][x]
            temp4 = paper[y][x] + paper[y][x+1] + paper[y+1][x+1] + paper[y+2][x+1]
            temp5 = paper[y][x] + paper[y+1][x] + paper[y+1][x+1] + paper[y+2][x+1]
            temp6 = paper[y][x+1] + paper[y+1][x+1] + paper[y+1][x] + paper[y+2][x]
            temp7 = paper[y][x] + paper[y+1][x] + paper[y+1][x+1] + paper[y+2][x]
            temp8 = paper[y][x+1] + paper[y+1][x+1] + paper[y+1][x] + paper[y+2][x+1]
            if max_value < max(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8):
                max_value = max(temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8)

    return max_value


def main():
    N, M = map(int, input().split())
    
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))

    
    print(solve(N, M, paper))


main()