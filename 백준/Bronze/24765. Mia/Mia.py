# 백준 24765

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def scoring(a, b):
    if {a, b} == {1, 2}:
        return 1000
    elif a == b:
        return int(a*100+a*10)
    else:
        return int(str(max(a, b)) + str(min(a, b)))


def solve(a, b, c, d):
    A = scoring(a, b)
    B = scoring(c, d)

    if A > B:
        return "Player 1 wins."
    elif A < B:
        return "Player 2 wins."
    return "Tie."


def main():
    while True:
        a, b, c, d = map(int, input().split())
        if {a, b, c, d} == {0}:
            break
        print(solve(a, b, c, d))


main()
