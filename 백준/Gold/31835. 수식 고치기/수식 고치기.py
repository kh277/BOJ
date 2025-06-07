# 백준 31835

'''
N-1번째 연산자 앞에 오는 모든 연산자를 미리 연산하여 before에 저장한다.
그 뒤, before과 N-1번째 연산자, N번째 값에서 적절히 값을 고치는 횟수를 구하면 된다.
최대 2회 고쳐야 하는 연산은 T | T = F, F & F = T 두 가지이다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, line, expect):
    if N == 1:
        first = True if line[0] == 'T' else False
        if first == expect:
            return 0
        else:
            return 1

    # 앞부분 연산 진행
    before = True if line[0] == 'T' else False
    for i in range(1, N-2, 2):
        cur = True if line[i+1] == 'T' else False
        if line[i] == '|':
            before = before | cur
        else:
            before = before & cur

    # 마지막 부분 연산 비교
    final = True if line[N-1] == 'T' else False
    if line[N-2] == '|':
        # 0회
        if before | final == expect:
            return 0
        # 2회
        elif before == True and final == True:
            return 2
    else:
        # 0회
        if before & final == expect:
            return 0
        # 2회
        elif before == False and final == False:
            return 2

    return 1


def main():
    N = int(input())
    line = list(input().decode().strip().split())
    expect = True if input().decode().rstrip() == 'T' else False

    print(solve(N, line, expect))


main()
