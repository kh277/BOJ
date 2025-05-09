# 백준 33694

'''
슬라임의 크기가 X 이상이 되는 구간 [A, B]를 구한 뒤, 스위핑으로 값이 3 이상인 구간을 찾는다.
'''

import io, math

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, X, slime):
    date = []
    for i in range(N):
        curA, curB, curC, curT = slime[i]

        # 최대로 커져도 X보다 작은 경우
        maxDay = math.ceil(curC/curA)
        if maxDay*curA < X:
            continue

        # 슬라임의 크기 구하기
        startDate = curT + math.ceil(X/curA)
        endDate = curT + maxDay + (maxDay*curA - X) // curB

        date.append([startDate, +1])
        date.append([endDate+1, -1])

    # 스위핑으로 3 이상인 구간 처리
    date.sort(key= lambda x: (x[0], x[1]))
    result = 0
    accSum = 0
    beforeDay = None
    for i in range(len(date)):
        curDay, value = date[i]
        if beforeDay != None and accSum >= 3:
            result += curDay - beforeDay
        accSum += value
        beforeDay = curDay

    return result


def main():
    N, X = map(int, input().split())
    slime = []
    for _ in range(N):
        slime.append(list(map(int, input().split())))

    print(solve(N, X, slime))


main()
