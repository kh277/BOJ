# 백준 30924

import io
from random import shuffle

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def interactive():
    numA = [i for i in range(1, 10001)]
    numB = [i for i in range(1, 10001)]
    shuffle(numA)
    shuffle(numB)

    # 질의 쿼리
    for i in range(10000):
        print(f"? A {numA[i]}", flush=True)
        answer = int(input())
        if answer == 1:
            A = numA[i]
            break

    for i in range(10000):
        print(f"? B {numB[i]}", flush=True)
        answer = int(input())
        if answer == 1:
            B = numB[i]
            break

    print(f"! {A+B}")


interactive()
