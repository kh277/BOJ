# 백준 20365

'''
1. 파란색으로 전부 칠하고 빨간색으로 일부분을 칠하는 방법
2. 빨간색으로 전부 칠하고 파란색으로 일부분을 칠하는 방법
중 적은 횟수를 출력하면 된다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, color):
    result = 10**7
    colorType = ['B', 'R']

    for i in range(2):
        standard = colorType[i]
    
        temp = 1
        index = 0
        while index < N:
            curC = color[index]
            if curC == standard:
                temp += 1
                index += 1
                while index < N:
                    nextC = color[index]
                    if nextC != standard:
                        break
                    index += 1
            else:
                index += 1
        
        result = min(result, temp)

    return result


def main():
    N = int(input())
    color = list(input().decode().strip())
    print(solve(N, color))


main()
