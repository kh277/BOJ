# 백준 10989

import io
import os

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
print = os.write
CHUNK = 4096


# main 함수 ----------
N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(input())] += 1

buf = bytearray()
lines = [None] * 10001
for num in range(1, 10001):
    cur = count[num]
    if not cur:
        continue
    if lines[num] is None:
        lines[num] = (str(num) + "\n").encode("ascii")

    line = lines[num]
    if cur < CHUNK:
        buf.extend(line * cur)
    else:
        if buf:
            print(1, buf)
            buf = bytearray()
        while cur:
            k = cur if cur < CHUNK else CHUNK
            print(1, line * k)
            cur -= k
    
    if len(buf) > 65536:
        print(1, buf)
        buf = bytearray()

if buf:
    print(1, buf)

os._exit(0)