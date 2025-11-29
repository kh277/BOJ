# 백준 18245

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(s, tab):
    result = []
    for i in range(0, len(s), tab):
        result.append(s[i])

    return ''.join(result)


def main():
    tab = 2
    while True:
        s = input().decode().rstrip()
        if s == 'Was it a cat I saw?':
            break
        print(solve(s, tab))
        tab += 1


main()
