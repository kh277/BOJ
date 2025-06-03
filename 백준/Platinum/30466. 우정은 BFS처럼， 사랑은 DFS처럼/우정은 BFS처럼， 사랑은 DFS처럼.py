# 백준 30466

'''
1번 정점에 ceil(N/2)개의 자식이 있도록 구성하고, 나머지 정점들은 전부 2번 정점 밑으로 길게 연결하면 된다.
이 경우 순서 차이의 최대값은 0 2 4 8 12 18 24 32 ... 와 같이 계차수열을 이루게 된다.
따라서 N이 짝수일 때는 (N-4)*(N-2)/2 + (N-2)의 값을, 홀수일 때는 (N-3)*(N-1)/2의 값을 가지게 된다.
'''

import io
from math import ceil

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    visitGap = (N-4)*(N-2)//2 + N-2 if N%2 == 0 else (N-3)*(N-1)//2
    edge = []
    
    # 1번 정점의 자식 간선
    numV = 2
    for i in range(ceil(N/2)):
        edge.append([1, numV])
        numV += 1
    
    startV = 2
    for i in range(N-ceil(N/2)-1):
        edge.append([startV, numV])
        startV = numV
        numV += 1
    
    return visitGap, edge


def main():
    N = int(input())
    visitGap, edge = solve(N)
    print(visitGap)
    for i in edge:
        print(*i)


main()
