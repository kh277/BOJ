# 백준 2417

import io
import math
from decimal import *

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
getcontext().prec = 30


def solve(N):
    return math.ceil(N.sqrt())


def main():
    N = int(input())
    print(solve(Decimal(str(N))))


main()
