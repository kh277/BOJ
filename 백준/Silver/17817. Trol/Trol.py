# 백준 17817

'''
바뀐 수열은 1, 2, 3, 4, ..., 9, 1, 2, ... 와 같이 1~9가 반복되는 수열이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# A_num을 구하기
def change(num):
    result = num
    while len(str(result)) > 1:
        temp = 0
        for i in list(str(result)):
            temp += int(i)
        result = temp

    return result


def solve(l, r):
    gap = r - l + 1
    result = (gap // 9) * 45
    mod = gap % 9
    start = change(l)

    for i in range(mod):
        cur = start+i
        if cur > 9:
            cur -= 9
        result += cur

    return result


def main():
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())

        print(solve(l, r))


main()
