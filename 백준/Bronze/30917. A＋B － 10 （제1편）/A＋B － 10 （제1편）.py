# 백준 30917

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def interactive():
    A = 0
    B = 0

    # 질의 쿼리
    for i in range(1, 10):
        print(f"? A {i}", flush=True)
        answer = int(input())
        if answer == 1:
            A = i
            break

    for i in range(1, 10):
        print(f"? B {i}", flush=True)
        answer = int(input())
        if answer == 1:
            B = i
            break

    print(f"! {A+B}")


interactive()
