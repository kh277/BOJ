# 백준 26975

'''
어떤 날짜가 주어질 때, 그 날짜 이후에 등장하는 팰린드롬 날짜를 구해야 한다.
또한, 윤년도 계산에 포함해야 한다.

년도를 1씩 증가시키고, 연도를 뒤집은 날짜가 달력에 있는지 판단하면 된다.
'''

import sys

input = sys.stdin.readline


def checkDate(year, month, day):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if 1 <= day <= 31:
            return True
    elif month in {4, 6, 9, 11}:
        if 1 <= day <= 30:
            return True
    elif month == 2 and int(year) % 4 == 0:
        if 1 <= day <= 29:
            return True
    elif month == 2 and int(year) % 4 != 0:
        if 1 <= day <= 28:
            return True
    else:
        return False


def solve():
    year = date[2]

    # 시작 연도에 팰린드롬 날짜가 포함된 경우
    if int(year[:2][::-1]) < int(date[1]):
        year = '0'*(4-len(str(int(year)+1))) + str(int(year)+1)
    elif int(year[:2][::-1]) == int(date[1]) and int(year[2:][::-1]) <= int(date[0]):
        year = '0'*(4-len(str(int(year)+1))) + str(int(year)+1)

    while True:
        month = int(year[:2][::-1])
        day = int(year[2:][::-1])
        if checkDate(year, month, day) == True:
            newDay = year[2:][::-1]
            newMonth = year[:2][::-1]
            return '0'*(2-len(newDay))+ newDay+ '.' + '0'*(2-len(newMonth))+newMonth + '.' + '0'*(4-len(year)) + year + '.'
        else:
            year = '0'*(4-len(str(int(year)+1))) + str(int(year)+1)


# main 함수 ----------
N = int(input())
for _ in range(N):
    date = list(input().rstrip().split('.'))
    print(solve())