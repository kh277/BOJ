# 백준 26650

import io
import re

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(S):
    N = len(S)
    pattern = re.compile(r'A+B+C+D+E+F+G+H+I+J+K+L+M+N+O+P+Q+R+S+T+U+V+W+X+Y+Z+')
    result = 0
    
    # 정규식 패턴을 만족하는 문자열 반환
    for i in pattern.finditer(S):
        start, end = i.span()
        countA = 0
        countZ = 0
        for i in range(start, end):
            if S[i] == 'A':
                countA += 1
            else:
                break
        for i in range(end-1, start-1, -1):
            if S[i] == 'Z':
                countZ += 1
            else:
                break

        result += countA * countZ

    return result


def main():
    S = input().decode().rstrip()
    print(solve(S))


main()
