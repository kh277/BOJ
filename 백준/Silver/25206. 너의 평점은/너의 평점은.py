# 백준 25206

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, \
        'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}


def solve(data):
    accGrade = 0
    cost = 0
    for i in range(20):
        curC, curG = data[i]
        if curG == 'P':
            continue
        accGrade += grade[curG]*curC
        cost += curC

    return accGrade/cost


def main():
    data = []
    for i in range(20):
        _, b, c = input().decode().rstrip().split()
        data.append([float(b), c])
    print(solve(data))


main()
