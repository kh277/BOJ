# 백준 9779

import io
import re

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(s):
    result = re.search(r'^da+dd?(i|y)$', s)
    if result == None:
        return 'Cooing'
    
    return 'She called me!!!'


def main():
    while True:
        s = input().decode().rstrip()
        if s == "":
            break
        print(solve(s))


main()
