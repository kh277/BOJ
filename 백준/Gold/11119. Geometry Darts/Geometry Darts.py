# 백준 11119

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def CCW(A, B, C):
    result = (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])
    if result > 0:
        return 1
    elif result < 0:
        return -1
    else:
        return 0


def distance2(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


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
                temp = CCW(A, B, [x, y])
                if temp == CCW(B, C, [x, y]) and temp == CCW(C, A, [x, y]):
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
