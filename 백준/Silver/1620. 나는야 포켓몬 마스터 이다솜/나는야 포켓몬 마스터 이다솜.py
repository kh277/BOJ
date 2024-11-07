# 백준 1620

'''
포켓몬은 최대 10만마리 이고, 쿼리도 10만개가 주어지므로, 브루트포스로는 시간초과가 발생한다.
따라서 딕셔너리를 이용해 효율적으로 탐색하자.

dic[포켓몬 이름] = 번호
dic[번호] = 포켓몬 이름
으로 두 종류를 모두 저장하여 O(1)로 구할 수 있다.
'''

import sys

input = sys.stdin.readline


def solve(query):
    return dic[query]


# main 함수 ----------
N, M = map(int, input().split())
dic = dict()
for i in range(1, N+1):
    name = input().rstrip()
    dic[str(i)] = name
    dic[name] = str(i)

for i in range(M):
    query = input().rstrip()
    print(solve(query))