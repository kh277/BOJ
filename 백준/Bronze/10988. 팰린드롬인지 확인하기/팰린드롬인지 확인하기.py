# 백준 10988

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(string):
    l = len(string)
    for i in range(l//2):
        if string[i] != string[-i-1]:
            return 0
    
    return 1


def main():
    string = input().decode().rstrip()
    print(solve(string))


main()