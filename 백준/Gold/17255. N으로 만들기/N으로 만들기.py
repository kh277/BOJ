# 백준 17255

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def recur(dic, num):
    if len(num) == 1:
        return 1

    left = num[1:]
    right = num[:-1]

    # 왼쪽 끝과 오른쪽 끝이 같은 경우
    if left == right:
        if left not in dic:
            dic[left] = recur(dic, left)

        return dic[left]

    # 왼쪽 끝과 오른쪽 끝이 다른 경우
    else:
        if left not in dic:
            dic[left] = recur(dic, left)
        if right not in dic:
            dic[right] = recur(dic, right)

        return dic[left] + dic[right]


# main 함수 ----------
N = input().decode().rstrip()
print(recur(dict(), N))