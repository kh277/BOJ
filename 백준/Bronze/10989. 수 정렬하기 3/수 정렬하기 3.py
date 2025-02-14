# 백준 10989

import io
import sys

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
print = sys.stdout.write
CHUNK = 4096


# main 함수 ----------
N = int(input())
count = [0 for _ in range(10001)]

for _ in range(N):
    count[int(input())] += 1

result = []
for i in range(1, 10001):
    cur = count[i]
    if cur:
        s = str(i) + "\n"
        while cur:
            k = cur if cur < CHUNK else CHUNK
            print(s*k)
            cur -= k
