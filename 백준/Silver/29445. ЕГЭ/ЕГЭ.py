# 백준 29445

'''
이진수 S_j'는 이진수 S_j의 각 자리의 0, 1을 서로 바꾼 수이고, S_(j+1) = S_j + S_j'라고 하자.
k, i가 주어질 때, S_k의 i자리 ~ i+6자리까지 출력하는 문제이다.

단순히 S_k의 i번째 자리 숫자는 숫자 i-1을 이진수로 표현했을 때, 1의 개수가 짝수개이면 0, 홀수개이면 1과 같다.
0 = 0 -> 0
1 = 1 -> 1
2 = 10 -> 1
3 = 11 -> 0
4 = 100 -> 1
5 = 101 -> 0
6 = 110 -> 0
7 = 111 -> 1
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


# num에서 1의 개수 세기
def countOne(num):
    count = 0
    while num:
        num &= (num - 1)
        count += 1

    return count


def solve():
    result = ""

    for num in range(i-1, i+6):
        result += str(countOne(num) % 2)
    
    return result


# main 함수 ----------
k, i = map(int, input().split())
print(solve())
