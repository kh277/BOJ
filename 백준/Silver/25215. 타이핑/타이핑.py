# 백준 25215

'''
대문자가 1개 있다면 무조건 별을 누르는게 이득이다.
대문자가 2개 이상 붙어있다면 무조건 마름모를 누르는게 이득이다.

반대로 대문자가 여러 개 있고 가운데 소문자가 하나 껴 있는 경우에도
별을 누르는게 이득이다.

따라서 각 문자열에서 대소문자가 바뀌는 부분을 저장해둔다.
문자가 바뀌는 곳의 앞뒤가 대-소-대 또는 소-대-소일 경우 별을 누르는 것이 이득이므로
counter 변수에 +1을 한다.

(문자열 길이) + (대소문자 바뀌는 부분 구간) - (연속해서 2번 바뀌는 구간)이 결과가 된다.
'''


import sys

input = sys.stdin.readline


def solve(string: str) -> int:
    change = []

    # 첫 시작이 대문자일 경우 -> 변경 체크
    if string[0].isupper():
        change.append(0)
    
    # i-1번째 문자와 i번째 문자가 다를 경우 -> 변경 체크
    for i in range(1, len(string)):
        if string[i-1].isupper() == string[i].islower():
            change.append(i)

    counter = 0     # 2번 연속해서 변경되는 문자열 수
    index = 0       # change 배열 인덱스
    while True:
        # 탈출 조건
        if index >= len(change)-1:
            break
        
        # index번째와 index+1번째 변경 값이 붙어있는 경우 -> 카운터+1
        if change[index+1] - change[index] == 1:
            counter += 1
            index += 2
        # 붙어있지 않은 경우
        else:
            index += 1
            continue

    result = len(string) + len(change) - counter

    return result


def main():
    string = input().rstrip()

    print(solve(string))


main()
