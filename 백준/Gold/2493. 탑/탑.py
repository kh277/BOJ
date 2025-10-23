# 백준 2493

import io, os
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, tower):
    stack = [(tower[0], 1)]
    result = array('I', [0])

    for i in range(1, N):
        while stack:
            curH, curI = stack[-1]
            if tower[i] < curH:
                result.append(curI)
                stack.append((tower[i], i+1))
                break
            stack.pop()

        if not stack:
            result.append(0)
            stack.append((tower[i], i+1))

    return result


def main():
    N = int(input())
    tower = list(map(int, input().split()))
    os.write(1, " ".join(map(str, solve(N, tower))).encode("ascii"))


main()
