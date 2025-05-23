# 백준 14369

import sys

input = sys.stdin.readline
num = [
    ['0', 'Z', ['Z', 'E', 'R', 'O']],
    ['2', 'W', ['T', 'W', 'O']],
    ['4', 'U', ['F', 'O', 'U', 'R']],
    ['6', 'X', ['S', 'I', 'X']],
    ['8', 'G', ['E', 'I', 'G', 'H', 'T']],
    ['5', 'F', ['F', 'I', 'V', 'E']],
    ['7', 'V', ['S', 'E', 'V', 'E', 'N']],
    ['9', 'I', ['N', 'I', 'N', 'E']],
    ['3', 'T', ['T', 'H', 'R', 'E', 'E']],
    ['1', 'O', ['O', 'N', 'E']]
]


def solve(string: str) -> int:
    # 각 글자별로 빈도수 추출
    char = dict()
    for i in string:
        if i not in char:
            char[i] = 1
        else:
            char[i] += 1
    
    # num에 정의된 순서대로 제외
    result = []
    for i in range(10):
        if num[i][1] in char:
            freq = char[num[i][1]]
            
            # char에서 빈도수만큼 글자 제거
            for j in num[i][2]:
                char[j] -= freq
                if char[j] == 0:
                    del char[j]
            
            # 결과에 제거한 숫자만큼 추가
            result += [num[i][0]] * freq
    
    # 리스트를 하나의 문자열로 합치기 
    return ''.join(sorted(result))
    

def main():
    T = int(input())
    
    for i in range(1, T+1):
        string = input().rstrip()
        
        print("Case #{a}: {b}".format(a=i, b=solve(string)))


main()