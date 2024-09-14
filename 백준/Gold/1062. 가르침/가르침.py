# 백준 1062

'''
anta + (0~7개의 글자) + tica로 이루어지기 때문에 a, c, i, n, t는 반드시 포함되어야 함.
'''

import sys

input = sys.stdin.readline
# a, c, i, n, t를 제외한 알파벳 번호 (0~25)
char = [1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25]
memo = {}

def recur(N: int, K: int, check: list, alpha: bin, idx: int) -> int:
    if (K, alpha) in memo:
        return memo[(K, alpha)]
    if K == 0:
        result = 0

        # alpha에 들어있는 문자들로 단어를 읽을 수 있는지 확인
        for word in check:
            if word == (alpha & word):
                result += 1
        memo[(K, alpha)] = result
        return result

    max_result = 0
    for i in range(idx, len(char)):
        # i번 알파벳이 alpha에 없다면 추가 (a, c, i, n, t를 제외한 0~25번 알파벳)
        if not alpha & (1 << char[i]):
            max_result = max(max_result, recur(N, K-1, check, alpha | (1 << char[i]), idx+1))
    
    memo[(K, alpha)] = max_result
    return max_result


def solve(N: int, K: int, word: list) -> int:
    if K < 5:
        return 0
    
    # N개의 단어에 대해, anta와 tica 사이에 들어있는 문자열의 종류 저장
    check = []
    for i in range(N):
        cur_char = list(set(word[i][4:-4]) - {'a', 'c', 'i', 'n', 't'})
        
        left_char = 0
        for j in cur_char:
            left_char |= 1 << (ord(j) - ord('a'))

        check.append(left_char)
            
    # 재귀를 통해 K-5개의 글자를 선정한 뒤, 그 글자들로 읽을 수 있는 단어 개수 반환
    return recur(N, K-5, check, 1 << 26, 0)


def main():
    N, K = map(int, input().split())
    word = []
    for _ in range(N):
        word.append(input().rstrip())

    print(solve(N, K, word))


main()