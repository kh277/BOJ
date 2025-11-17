# 백준 13275

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def Manacher(N, string):
    # 전처리 - 짝수 길이 팰린드롬을 처리하기 위한 구분자 추가
    size = 2*N-1
    text = [0] * size
    for i in range(N):
        text[2*i] = string[i]
        if i != N-1:
            text[2*i+1] = -1

    # 매내처 알고리즘으로 보조 배열 P 계산하기
    P = [0] * size
    radius = 0
    center = 0
    for i in range(size):
        cur = 0
        if i <= radius:
            cur = min(P[2*center-i], radius-i)
        while i-cur-1 >= 0 and i+cur+1 < size and text[i-cur-1] == text[i+cur+1]:
            cur += 1
        P[i] = cur

        if i+P[i] > radius:
            radius = i + P[i]
            center = i

    # 보조 배열 P에 따라 최장 부분 팰린드롬 도출
    result = 0
    for i in range(size):
        if i % 2 == 0:
            length = (P[i]//2) * 2 + 1
        else:
            length = ((P[i]+1)//2) * 2
        if length > result:
            result = length

    return result


def main():
    string = input().decode().strip()
    print(Manacher(len(string), string))


main()
