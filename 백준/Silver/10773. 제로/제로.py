# 백준 10773

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline

def main():
    K = int(input())
    stack = array('I')
    accSum = 0
    for _ in range(K):
        N = int(input())
        if N == 0:
            accSum -= stack.pop()
        else:
            stack.append(N)
            accSum += N
    
    print(accSum)


main()