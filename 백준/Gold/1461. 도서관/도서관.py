# 백준 1461

'''
책을 모두 제자리에 놔둔 후에 다시 0으로 올 필요가 없다고 했으니,
가장 멀리 떨어진 위치의 책은 가장 마지막에 가져다 두어야 한다.
그 책들을 제외한 책들은 최대 M개씩 들고 왕복해서 가져다두면 된다.
양수와 음수 부분은 분리해서 처리해야 한다.
'''

import io
from array import array

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, M, data):
    plus = array('i')
    minus = array('i')

    # 양수는 plus, 음수는 minus에 저장 후 정렬
    for i in data:
        if i > 0:
            plus.append(i)
        else:
            minus.append(-i)
    plus = sorted(plus)
    minus = sorted(minus)

    # 예외 처리
    if len(plus) == 0:
        plus.append(0)
    if len(minus) == 0:
        minus.append(0)

    # 가장 멀리 있는 책을 포함하여 최대 M개 처리
    result = 0
    plusIndex = len(plus)-1
    minusIndex = len(minus)-1
    if max(plus) > max(minus):
        result += plus[plusIndex]
        plusIndex -= min(M, len(plus))
    elif max(plus) <= max(minus):
        result += minus[minusIndex]
        minusIndex -= min(M, len(minus))

    # 남은 책들 M개씩 처리
    for i in range(plusIndex, -1, -M):
        result += plus[i]*2
    for i in range(minusIndex, -1, -M):
        result += minus[i]*2

    return result


def main():
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    print(solve(N, M, data))


main()
