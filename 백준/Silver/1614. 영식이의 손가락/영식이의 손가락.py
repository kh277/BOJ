# 백준 1614

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(num, count):
    if count == 0:
        return num-1

    # 1, 5인 경우
    if num == 1 or num == 5:
        return count*8 + num-1 

    # 2, 3, 4인 경우
    if count % 2 == 0:
        return (count//2)*8 + num-1
    else:
        return (count//2)*8 + 9-num


def main():
    num = int(input())
    count = int(input())

    print(solve(num, count))


main()
