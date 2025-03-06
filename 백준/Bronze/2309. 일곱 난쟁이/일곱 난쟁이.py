# 백준 2309

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(height):
    sumHeight = sum(height)
    for x in range(8):
        for y in range(x+1, 9):
            if sumHeight - height[x] - height[y] == 100:
                return sorted(height[:x] + height[x+1:y] + height[y+1:])
    

def main():
    height = []
    for i in range(9):
        height.append(int(input()))
    for i in solve(height):
        print(i)


main()