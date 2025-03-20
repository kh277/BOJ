# 백준 9414

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(cost):
    cost.sort(reverse=True)

    result = 0
    for i in range(len(cost)):
        result += 2 * (cost[i])**(i+1)

    if result > 5000000:
        return 'Too expensive'

    return result


def main():
    T = int(input())
    for _ in range(T):
        cost = []
        while True:
            temp = int(input())
            if temp == 0:
                break
            cost.append(temp)
        print(solve(cost))


main()
