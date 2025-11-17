# 백준 16163

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def Manacher(string):
    # 전처리 - 짝수 길이 팰린드롬을 처리하기 위한 구분자 추가
    text = '$#' + '#'.join(string) + '#@'

    # 매내처 알고리즘으로 보조 배열 P 계산하기
    P = array('I', [1]) * len(text)
    radius = 0
    center = 0

    for i in range(1, len(text)-1):
        if i < radius:
            P[i] = min(P[2*center-i], radius-i)

        while text[i-P[i]] == text[i+P[i]]:
            P[i] += 1

        if i+P[i] > radius:
            radius = i + P[i]
            center = i

    # 팰린드롬 부분 문자열의 개수 구하기
    result = 0
    for i in range(1, len(text)-1):
        result += P[i]//2
    return result


def main():
    string = input().decode().strip()
    print(Manacher(string))


main()
