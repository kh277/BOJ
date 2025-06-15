# 백준 26596

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j and int(data[i]*1.618) == data[j]:
                return "Delicious!"
    return "Not Delicious..."


def main():
    M = int(input())
    name = dict()
    data = []
    count = 0
    for _ in range(M):
        a, b = input().decode().split()
        if a not in name:
            name[a] = count
            count += 1
            data.append(0)
        data[name[a]] += int(b)

    print(solve(data))


main()
