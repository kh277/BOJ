# 백준 27082

'''
세트에 등장한 문자를 추가하고, 이미 등장한 문자가 재등장할 경우 넘어간다.
'''

import sys

input = sys.stdin.readline


def solve():
    result = ''
    isUsed = set({'A', 'E', 'I', 'O', 'U'})
    
    for st in string:
        # 공백이라면
        if st == ' ':
            if len(result) == 0:
                continue
            if result[-1] != ' ':
                result += ' '
            continue
        
        # 구두점이라면
        elif st in {'.', ',', '?'}:
            if len(result) == 0:
                result += st
            elif result[-1] == ' ':
                result = result[:-1]
            result += st

        # 등장하지 않은 일반 문자라면
        elif st not in isUsed:
            result += st
            isUsed.add(st)
    
    return result.strip()


# main 함수 ----------
string = input().strip()
print(solve())
