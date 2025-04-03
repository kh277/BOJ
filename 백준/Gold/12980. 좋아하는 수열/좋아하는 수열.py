# 백준 12980

import io
from itertools import permutations

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def calScore(N, num):
    score = 0
    for i in range(N):
        for j in range(i+1, N):
            if num[i] < num[j]:
                score += 1
    
    return score


def solve(N, S, num):
    zeroIndex = []
    numSet = set([i for i in range(1, N+1)])
    for i in range(N):
        if num[i] == 0:
            zeroIndex.append(i)
        else:
            numSet.remove(num[i]) 

    count = 0
    nPr = list(permutations(list(numSet), len(numSet)))
    for i in range(len(nPr)):
        curPerm = nPr[i]
        for j in range(len(zeroIndex)):
            num[zeroIndex[j]] = curPerm[j]
        if calScore(N, num) == S:
            count += 1
            
    return count
    

def main():
    N, S = map(int, input().split())
    num = list(map(int, input().split()))
    
    print(solve(N, S, num))


main()
