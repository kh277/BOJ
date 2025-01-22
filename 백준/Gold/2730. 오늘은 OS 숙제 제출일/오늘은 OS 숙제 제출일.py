# 백준 2730

import sys

input = sys.stdin.readline


# 윤년일 경우 3~12월 누적날짜에 +1
def addLeapYear(sumDate, tMonth, dMonth):
    if 1 <= tMonth <= 3 and 1 <= dMonth <= 3:
            for i in range(3, 13):
                sumDate[i] += 1
    
    return sumDate


def solve(transaction, document):
    sumDate = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    tMonth, tDay, tYear = map(int, transaction.split("/"))
    dMonth, dDay = map(int, document.split("/"))

    # 윤년 처리
    if tYear % 4 == 0 and tYear % 100 == 0 and tYear % 400 == 0:
        sumDate = addLeapYear(sumDate, tMonth, dMonth)
    elif tYear % 4 == 0 and tYear % 100 == 0:
        pass
    elif tYear % 4 == 0:
        sumDate = addLeapYear(sumDate, tMonth, dMonth)

    # 누적 날짜 계산
    transactionDay = sumDate[tMonth] + tDay
    documentDay = sumDate[dMonth] + dDay

    # 연도가 바뀌는 경우 처리
    if 0 < documentDay+365-transactionDay <= 7:
            documentDay += 365
            tYear += 1
    if 0 < transactionDay+365-documentDay <= 7:
            transactionDay += 365
            tYear -= 1

    # 날짜 처리
    if 0 < transactionDay-documentDay <= 7:
        if transactionDay-documentDay == 1:
            return "{}/{}/{} IS {} DAY PRIOR".format(dMonth, dDay, tYear, 1)
        else:
            return "{}/{}/{} IS {} DAYS PRIOR".format(dMonth, dDay, tYear, transactionDay-documentDay)
    elif transactionDay == documentDay:
        return "SAME DAY"
    elif 0 < documentDay-transactionDay <= 7:
        if documentDay-transactionDay == 1:
            return "{}/{}/{} IS {} DAY AFTER".format(dMonth, dDay, tYear, 1)
        else:
            return "{}/{}/{} IS {} DAYS AFTER".format(dMonth, dDay, tYear, documentDay-transactionDay)
    else:
        return "OUT OF RANGE"


# main 함수 ----------
T = int(input())
for _ in range(T):
    transaction, document = map(str, input().split())
    print(solve(transaction, document))