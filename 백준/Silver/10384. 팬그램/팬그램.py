# 백준 10384


import sys

input = sys.stdin.readline
INF = 4


def solve():
    # 알파벳을 전부 딕셔너리에 등록
    dic = dict()
    for i in range(97, 97+26):
        dic[chr(i)] = 0
    
    # 문자열을 순서대로 딕셔너리에 추가
    for i in string:
        if i.isalpha() == True:
            dic[i.lower()] += 1
    
    # 딕셔너리 값 중 최소값 도출
    result = min(dic.values())
    
    # 결과 출력
    if result == 1:
        return "Pangram!"
    elif result == 2:
        return "Double pangram!!"
    elif result == 3:
        return "Triple pangram!!!"
    else:
        return "Not a pangram"


# main 함수 ----------
T = int(input())
for i in range(1, T+1):
    string = list(map(str, input().rstrip()))
    print("Case {a}: {b}".format(a=i, b=solve()))
