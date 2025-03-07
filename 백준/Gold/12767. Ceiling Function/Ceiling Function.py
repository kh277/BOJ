# 백준 12767

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, seq):
    result = set()

    for cur in range(N):
        tree = ['0' for _ in range(2**K)]

        for curNum in seq[cur]:
            curPos = 1
            while True:
                if tree[curPos] == '0':
                    tree[curPos] = str(curNum)
                    break
                elif int(tree[curPos]) > curNum:
                    curPos = curPos * 2
                else:
                    curPos = curPos * 2 + 1

        for i in range(2**K):
            if int(tree[i]) > 0:
                tree[i] = '1'

        result.add("".join(tree))

    return len(result)


def main():
    N, K = map(int, input().split())
    seq = []
    for _ in range(N):
        seq.append(list(map(int, input().split())))
    
    print(solve(N, K, seq))


main()