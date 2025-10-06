# 백준 6502

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(r, w, l):
    if 4*r*r >= w*w + l*l:
        return True
    return False


def main():
    t = 1
    while True:
        i = list(map(int, input().split()))
        if i[0] == 0:
            break
        if solve(*i) == True:
            print(f"Pizza {t} fits on the table.")
        else:
            print(f"Pizza {t} does not fit on the table.")
        
        t += 1


main()
