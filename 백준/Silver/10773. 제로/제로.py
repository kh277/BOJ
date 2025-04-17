# 백준 10773

import io, os
from array import array

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def main():
    K = int(input())
    stack = array('I')
    accSum = 0
    for _ in range(K):
        N = int(input())
        if N == 0:
            accSum -= stack.pop()
        else:
            stack.append(N)
            accSum += N
    
    out = array('I')
    out.append(accSum)
    os.write(1, "".join(map(str, out)).encode("ascii"))
    os._exit(0)


main()