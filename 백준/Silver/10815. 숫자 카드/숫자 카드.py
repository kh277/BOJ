# 백준 10815

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    dic = dict()
    for i in list(map(int, input().split())):
        dic[i] = 1
    M = int(input())
    for i in list(map(int, input().split())):
        print('1' if i in dic else '0', end=" ")


main()
