# 백준 20949

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def solve(N, data):
    data.sort(key= lambda x: (-(x[0]**2 + x[1]**2)**0.5))
    return [i[2] for i in data]


def main():
    N = int(input())
    data = []
    for i in range(N):
        W, H = map(int, input().split())
        data.append([W, H, i+1])
    
    for i in solve(N, data):
        print(i)


main()
