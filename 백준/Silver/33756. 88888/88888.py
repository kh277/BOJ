# 백준 33756

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N):
    eight = [8]
    for i in range(17):
        eight.append(int(str(eight[i]) + '8'))
    
    cur = len(eight)-1
    count = 0
    while N > 0 and cur >= 0:
        if count > 8:
            break

        if N < eight[cur]:
            cur -= 1
            continue

        N -= eight[cur]
        count += 1

    return 'Yes' if count <= 8 and N == 0 else 'No'


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


main()
