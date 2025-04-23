# 백준 16391

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    seq = ''
    for _ in range(N):
        if input().decode().rstrip() == 'O':
            seq += '1'
        else:
            seq += '0'

    print(int(seq, 2))


main()
