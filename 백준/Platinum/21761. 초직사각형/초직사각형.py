# 백준 21761

'''
A, B, C, D의 길이를 증가시키는 카드들을 전부 따로 분리한다.
그 뒤, A, B, C, D 중 가장 큰 카드를 선택한 경우를 각각 계산하여 최대값이 되는 경우를 적용시킨다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, K, size, card):
    card = [sorted(card[i]) for i in range(4)]
    index = [len(card[i])-1 for i in range(4)]
    result = []

    for _ in range(K):
        # A, B, C, D 중 최대 부피를 만드는 카드 선택
        add = []
        for i in range(4):
            if index[i] >= 0:
                size[i] += card[i][index[i]]
                add.append([i, size[0]*size[1]*size[2]*size[3]])
                size[i] -= card[i][index[i]]

        maxIndex = -1
        maxValue = -1
        for i in range(len(add)):
            if add[i][1] > maxValue:
                maxIndex, maxValue = add[i]

        result.append([chr(ord('A')+maxIndex), card[maxIndex][index[maxIndex]]])
        size[maxIndex] += card[maxIndex][index[maxIndex]]
        index[maxIndex] -= 1

    return result


def main():
    N, K = map(int, input().split())
    A, B, C, D = map(int, input().split())
    card = [array('I') for _ in range(4)]
    for _ in range(N):
        c, num = input().decode().split()
        card[ord(c)-ord('A')].append(int(num))

    for i in solve(N, K, [A, B, C, D], card):
        print(*i)


main()
