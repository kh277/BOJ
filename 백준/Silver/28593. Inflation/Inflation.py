# 백준 28593

'''
누적 합을 저장하자. 또한, 수의 범위가 1~100만이므로
크기가 200만인 리스트 data를 생성하고, startPoint를 100만으로 둔다.
이 data 리스트에는 해당 숫자가 몇 개 있는지를 저장한다.

모든 수를 더하는 쿼리의 경우 startPoint를 그 수만큼 감소시키면 되고,
일정 수를 고치는 쿼리의 경우 data에서 startPoint + 그 수에 해당하는 인덱스의 값만큼 수정해주면 된다.
'''

import sys

input = sys.stdin.readline


def add(accSum, i, startPoint):
    startPoint -= i
    accSum += N*int(i)

    return accSum, startPoint


def update(accSum, i, j, startPoint):
    if i != j and startPoint+i in data:
        accSum += data[startPoint+i]*(j-i)
        if startPoint+j not in data:
            data[startPoint+j] = data[startPoint+i]
        else:
            data[startPoint+j] += data[startPoint+i]
        data[startPoint+i] = 0

    return accSum


# main 함수 ----------
N = int(input())
P = list(map(int, input().split()))

# 데이터 초기 처리
data = dict()
startPoint = 0
accSum = sum(P)
for i in P:
    if startPoint+i not in data:
        data[startPoint+i] = 1
    else:
        data[startPoint+i] += 1

# 쿼리 처리
Q = int(input())
for _ in range(Q):
    query = list(map(str, input().split()))
    if query[0] == 'INFLATION':
        accSum, startPoint = add(accSum, int(query[1]), startPoint)
    else:
        accSum = update(accSum, int(query[1]), int(query[2]), startPoint)

    print(accSum)