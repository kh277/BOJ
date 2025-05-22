# 백준 30969

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def main():
    N = int(input())
    cost = array('I', [0]) * 1001
    result = 0
    jinju = 0
    for i in range(N):
        a, b = map(str, input().decode().rstrip().split())
        if a == 'jinju':
            jinju = int(b)
        else:
            if int(b) > 1000:
                result += 1
            else:
                cost[int(b)] += 1

    for i in range(jinju+1, 1001):
        result += cost[i]

    print(jinju)
    print(result)


main()
