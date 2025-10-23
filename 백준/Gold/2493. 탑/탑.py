# 백준 2493

import io, os
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tower):
    stackH = [tower[0]]
    stackI = [1]
    result = array('I', [0])

    for i in range(1, N):
        while stackH:
            curH = stackH[-1]
            if tower[i] < curH:
                result.append(stackI[-1])
                stackH.append(tower[i])
                stackI.append(i+1)
                break
            stackH.pop()
            stackI.pop()

        if not stackH:
            result.append(0)
            stackH.append(tower[i])
            stackI.append(i+1)

    return result


def main():
    N = int(input())
    tower = list(map(int, input().split()))
    os.write(1, " ".join(map(str, solve(N, tower))).encode("ascii"))


main()
