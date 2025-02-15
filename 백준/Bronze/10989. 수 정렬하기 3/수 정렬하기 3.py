# 백준 10989

import io, os
from array import array


def main():
    input = io.BufferedReader(io.FileIO(0), 1<<18).readline
    N = int(input())
    count = array('I', [0]) * 10001

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
        if cur < 4096:
            buf.extend(line * cur)
        else:
            if buf:
                os.write(1, buf)
                buf = bytearray()
            while cur:
                k = cur if cur < 4096 else 4096
                os.write(1, line * k)
                cur -= k
        
        if len(buf) > 65536:
            os.write(1, buf)
            buf = bytearray()

    if buf:
        os.write(1, buf)

    os._exit(0)


main()