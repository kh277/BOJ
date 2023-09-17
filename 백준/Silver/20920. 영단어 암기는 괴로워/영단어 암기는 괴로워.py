# 백준 20920

from sys import stdin

input = stdin.readline


def solve(N: int, min: int, li: list):

    # { '단어' : [단어, 단어 빈도 수, 단어 길이], ... } 인 딕셔너리 생성
    word = {}
    for i in li:
        if i in word:
            word[i][1] += 1
        else:
            word[i] = [i, 1, len(i)]

    # word에서 [단어, 단어 빈도 수, 단어 길이] 부분만 추출하여 리스트로 변환
    word = list(word.values())

    # word에 저장된 단어 중 길이가 M 미만인 단어는 빈도수를 -1로 설정
    for i in range(len(word)):
        if word[i][2] < min:
            word[i][1] = -1

    # 단어 빈도수(내림차순) - 단어 길이(내림차순) - 단어 사전(오름차순) 우선순위로 정렬
    word = sorted(word, key= lambda x: (-x[1], -x[2], x[0]))

    # 빈도수가 음수인 단어는 제외하고 리스트를 생성하여 반환
    return [i[0] for i in word if i[1] > 0]


def main():
    N, M = map(int, input().split())
    li = [0 for _ in range(N)]

    for i in range(N):
        li[i] = input().rstrip()

    for i in solve(N, M, li):
        print(i)

main()
