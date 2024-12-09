# 백준 1786

import sys

input = sys.stdin.readline


def getFail(pattern):
    fail = [0 for _ in range(len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        # pattern의 i번째와 pattern의 j번째가 일치하지 않는다면
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]

        # pattern의 i번째와 pattern의 j번째가 일치한다면
        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j

    return fail


def KMP(text, pattern):
    # 반복 패턴 전처리
    fail = getFail(pattern)

    result = []
    j = 0
    for i in range(len(text)):
        # text의 i번째와 pattern의 j번째가 일치하지 않는다면
        while j > 0 and text[i] != pattern[j]:
            j = fail[j-1]

        # text의 i번째와 pattern의 j번째가 일치한다면
        if text[i] == pattern[j]:
            # pattern을 끝까지 탐색했다면
            if j == len(pattern)-1:
                result.append(i-len(pattern)+2)
                j = fail[j]
            else:
                j += 1
    
    return [[len(result)], result]


# main 함수 ----------
T = input().rstrip()
P = input().rstrip()
for i in KMP(T, P):
    print(*i)