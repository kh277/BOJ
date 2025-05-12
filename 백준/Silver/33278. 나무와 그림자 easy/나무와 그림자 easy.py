# 백준 33278

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, t, tree):
    tree.sort()
    curTree = 0
    result = 0
    while curTree < N-1:
        nextTree = curTree + 1

        while nextTree < N:
            shadow = tree[curTree][1] - t*(tree[nextTree][0]-tree[curTree][0])
            if shadow > tree[nextTree][1]:
                result += tree[nextTree][1]
                nextTree += 1
                continue
            result += shadow
            break
        curTree = nextTree

    return result


def main():
    N, t = map(int, input().split())
    tree = []
    for _ in range(N):
        tree.append(list(map(int, input().split())))
    print(solve(N, t, tree))


main()
