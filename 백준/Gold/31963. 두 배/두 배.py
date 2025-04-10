# 백준 31963

'''
num[i] * 2^k <= num[i+1] * 2^x인 x를 구하면 된다.
이전 수의 k값을 저장하는 변수를 이용하여 x = ceil(log2(num[i]/num[i+1])) + k로 구한다.
'''

import io
import math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, num):
    count = 0
    foreK = 0
    index = 1
    while index < N:
        # 오름차순이 아닐 경우
        if foreK > math.log2(num[index]/num[index-1]):
            curK = math.ceil(math.log2(num[index-1]/num[index])) + foreK
            foreK = curK
            count += curK
        # 오름차순일 경우
        else:
            foreK = 0

        index += 1

    return count


def main():
    N = int(input())
    num = list(map(int, input().split()))
    print(solve(N, num))


main()
