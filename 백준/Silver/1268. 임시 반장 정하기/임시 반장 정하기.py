# 백준 1268

import sys

input = sys.stdin.readline


def solve():
    result = [0 for _ in range(N)]

    for curStudent in range(N):
        for otherStudent in range(N):
            if curStudent == otherStudent:
                continue
            for grade in range(5):
                # curStudent와 otherStudent가 같은 반이 된 적이 있다면 +1
                if case[curStudent][grade] == case[otherStudent][grade]:
                    result[curStudent] += 1
                    break
    
    # 학생 중 같은 반이 된 횟수가 최대인 학생 도출
    maxResult = [0, 0]
    for i in range(N):
        if result[i] > maxResult[0]:
            maxResult = [result[i], i]

    # 학생 번호는 1부터 시작하므로
    return maxResult[1]+1


# main 함수 ----------
N = int(input())
case = []
for i in range(N):
    case.append(list(map(int, input().split())))

print(solve())