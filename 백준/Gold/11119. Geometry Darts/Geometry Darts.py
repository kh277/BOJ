# 백준 11119

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def distance2(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


def ShoelaceFormula(N, graph):
    area = 0

    for i in range(N):
        j = (i+1) % N
        area += graph[i][0]*graph[j][1] - graph[i][1]*graph[j][0]

    return abs(area) / 2


def query(S, poly, dart):
    result = 0
    for i in range(3):
        x, y = map(float, dart[i])
        for j in range(S):
            if poly[j][0] == 'C':
                A = [float(poly[j][1]), float(poly[j][2])]
                R = float(poly[j][3])
                if distance2(A, [x, y]) <= R**2:
                    result += 1
            elif poly[j][0] == 'R':
                x1, y1, x2, y2 = map(float, poly[j][1:])
                if x1 <= x <= x2 and y1 <= y <= y2:
                    result += 1
            else:
                A = [float(poly[j][1]), float(poly[j][2])]
                B = [float(poly[j][3]), float(poly[j][4])]
                C = [float(poly[j][5]), float(poly[j][6])]
                triS = ShoelaceFormula(3, [A, B, C])
                if abs(triS - ShoelaceFormula(3, [A, B, [x, y]]) - ShoelaceFormula(3, [B, C, [x, y]]) - ShoelaceFormula(3, [C, A, [x, y]])) < 1e-6:
                    result += 1

    return result


def main():
    S = int(input())
    poly = []
    for _ in range(S):
        poly.append(list(map(str, input().decode().split())))

    N = int(input())
    for _ in range(N):
        bob = []
        hannah = []
        for _ in range(3):
            bob.append(list(map(float, input().split())))
        bobScore = query(S, poly, bob)
        for _ in range(3):
            hannah.append(list(map(float, input().split())))
        hannahScore = query(S, poly, hannah)

        if bobScore > hannahScore:
            print("Bob")
        elif bobScore < hannahScore:
            print("Hannah")
        else:
            print("Tied")


main()
