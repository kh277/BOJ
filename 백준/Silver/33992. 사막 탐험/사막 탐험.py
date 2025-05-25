# C번

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def distance(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5


def isInclude(A, O, r):
    if distance(A, O) <= r:
        return True
    return False


def solve(start, end, oasis, r):
    if isInclude(start, oasis, r) == True and isInclude(end, oasis, r) == True:
        return 0
    elif isInclude(start, oasis, r) == True:
        return distance(oasis, end) - r
    elif isInclude(end, oasis, r) == True:
        return distance(start, oasis) - r
    else:
        stra = distance(start, end)
        oasi = distance(start, oasis) + distance(oasis, end) - 2*r
        return min(stra, oasi)


def main():
    ax, ay, bx, by, px, py, r = map(int, input().split())

    print(solve([ax, ay], [bx, by], [px, py], r))


main()
