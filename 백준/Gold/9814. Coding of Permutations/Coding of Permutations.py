# 백준 9814

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    total = 1
    for i in range(1, N+1):
        total *= i

    start = 1
    end = total
    leftNum = [i for i in range(1, N+1)]
    for nextBranchCount in range(N, 0, -1):
        nextPos = int(num[N-nextBranchCount])
        nextBranchIndex = 0
        for i in range(len(leftNum)):
            if leftNum[i] == nextPos:
                nextBranchIndex = i
                leftNum.remove(nextPos)
                break

        nextBranchSize = (end - start + 1) // nextBranchCount
        start = start + nextBranchSize * nextBranchIndex
        end = start + nextBranchSize - 1

    return str(start)


def main():
    result = ""
    while True:
        temp = input().decode().strip().split("(")
        if temp[0] == '-1':
            result = result[:-1]
            break
        result += solve(int(temp[1][:-1]), list(temp[2][:-2].split(",")))
        result += ","
    print(result)


main()