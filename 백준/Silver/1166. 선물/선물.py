# 백준 1166

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def check(A, N, L, W, H):
    if (L//A) * (W//A) * (H//A) >= N:
        return True
    return False


def solve(N, L, W, H):
    start = 0.0000000001
    end = 1000000000
    
    count = 0
    while count < 200:
        mid = (start+end)/2
        if check(mid, N, L, W, H) == True:
            start = mid
        else:
            end = mid
        count += 1
    
    return mid


def main():
    N, L, W, H = map(int, input().split())
    print(solve(N, L, W, H))


main()
