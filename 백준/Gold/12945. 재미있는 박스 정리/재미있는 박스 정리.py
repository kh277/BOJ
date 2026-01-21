# 백준 2418

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, box):
    box.sort()
    left = 0
    right = N//2
    count = 0
    used = bytearray(N)

    # 겹칠 수 있는 박스 세기
    while right < N:
        # 이미 사용된 박스는 넘기기
        while left < N and used[left] == 1:
            left += 1

        # 맞는 박스 쌍을 찾은 경우
        if box[left]*2 <= box[right]:
            used[left] = 1
            used[right] = 1
            left += 1
            right += 1
            count += 1
        # 찾지 못한 경우
        else:
            right += 1

    # 겹치지지 않은 박스 세기
    for i in range(N):
        if used[i] == 0:
            count += 1

    return count


def main():
    N = int(input())
    box = []
    for _ in range(N):
        box.append(int(input()))
    print(solve(N, box))


main()
