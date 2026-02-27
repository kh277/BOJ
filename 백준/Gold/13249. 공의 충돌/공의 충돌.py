# 백준 13249

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, ball, T):
    count = 0
    for status in range(1<<N):
        left = []
        right = []

        # 왼쪽 방향, 오른쪽 방향 분리
        for i in range(N):
            if (status>>i) & 1:
                left.append(i)
            else:
                right.append(i)

        # 충돌 횟수 카운트
        for l in left:
            for r in right:
                if 0 <= ball[r] - ball[l] <= 2*T:
                    count += 1

    return count / (1<<N)


def main():
    N = int(input())
    ball = list(map(int, input().split()))
    T = int(input())

    print(solve(N, ball, T))


main()
