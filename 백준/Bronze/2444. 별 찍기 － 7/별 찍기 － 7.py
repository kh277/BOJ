# 백준 2444

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    for i in range(1, N+1):
        print(' '*(N-i) + '*'*(2*i-1))
    
    for i in range(N-1, 0, -1):
        print(' '*(N-i) + '*'*(2*i-1))


main()
