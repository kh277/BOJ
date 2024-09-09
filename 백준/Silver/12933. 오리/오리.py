# 백준 12933

'''
먼저 문자열이 quack로 잘 이루어져 있는지 확인한다.
올바른 문자열은 반드시 q로 시작해서 k로 끝나므로,
q가 온 경우 temp += 1, k가 온 경우 temp -= 1을 해준다.
이 temp의 값이 최대가 될 때가 오리의 마리수이다.
'''

import sys

input = sys.stdin.readline


def solve(string: str) -> int:
    # 올바른 문자열인지 확인
    check = [False for _ in range(len(string))]
    quack = [[] for _ in range(5)]

    for i in range(len(string)):
        if string[i] == 'q':
            quack[0].append(i)
        elif string[i] == 'u':
            quack[1].append(i)
        elif string[i] == 'a':
            quack[2].append(i)
        elif string[i] == 'c':
            quack[3].append(i)
        elif string[i] == 'k':
            quack[4].append(i)
    
    if not (len(quack[0]) == len(quack[1]) == len(quack[2]) == len(quack[3]) == len(quack[4])):
        return -1
    
    for i in range(len(quack[0])):
        temp = -1
        for j in range(5):
            if temp < quack[j][i]:
                temp = quack[j][i]
            else:
                return -1
    
    # 최대 중첩 개수 확인
    result = 0
    temp = 0
    for i in range(len(string)):
        if string[i] == 'q':
            temp += 1
            result = max(result, temp)
        elif string[i] == 'k':
            temp -= 1
    
    return result


def main():
    string = input().rstrip()
    
    print(solve(string))


main()