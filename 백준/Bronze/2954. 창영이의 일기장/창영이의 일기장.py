# 백준 2954

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
vow = {'a', 'e', 'i', 'o', 'u'}


def solve(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] in vow:
            result.append(s[i])
            i += 3
        else:
            result.append(s[i])
            i += 1
    
    return ''.join(result)


def main():
    s = input().decode().rstrip()
    print(solve(s))


main()
