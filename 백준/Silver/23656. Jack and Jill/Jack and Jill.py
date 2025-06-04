# 백준 23656

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def interactive():
    start = 1
    end = 10**9

    # 질의 쿼리
    for _ in range(100):
        cur = int(input())
        if cur < start:
            print(">", flush=True)
        elif cur > end:
            print("<", flush=True)
        else:
            if start == end and cur == start:
                print("=")

            mid = (end+start)//2
            if cur > mid:
                end = cur-1
                print("<", flush=True)
            else:
                start = cur+1
                print(">", flush=True)


interactive()
