# 백준 1032


import sys

input = sys.stdin.readline


def solve():
    result = []
    for index in range(len(string[0])):
        cur = string[0][index]
        result.append(string[0][index])
        for i in range(1, N):
            if cur != string[i][index]:
                result.pop()
                result.append('?')
                break
    
    return "".join(result)


# main 함수 ----------
N = int(input())

string = []
for _ in range(N):
    string.append(input().rstrip())
    
print(solve())