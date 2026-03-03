# 백준 34649

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, string):
    count = 1
    curI = 1
    prevLen = 1
    while curI < N:
        # 직전 문자열의 길이가 2라면
        if prevLen == 2:
            prevLen = 1
            curI += 1
        # 직전 문자열의 길이가 1이고 중복이라면
        elif string[curI-1] == string[curI]:
            if curI+1 == N:
                break
            curI += 2
            prevLen = 2
        # 직전 문자열의 길이가 1이고 중복이 아니라면
        else:
            curI += 1
        count += 1

    return count


def main():
    T = int(input())
    for i in range(T):
        string = input().decode().rstrip()
        print(solve(len(string), string))


main()
