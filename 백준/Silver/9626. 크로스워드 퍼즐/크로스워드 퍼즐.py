# 백준 9626


import sys

input = sys.stdin.readline

f = lambda y, x: '#' if (y + x) % 2 == 0 else '.'


def solve():
    result = [[None for _ in range(L+X+R)] for _ in range(U+Y+D)]
    
    for y in range(U):
        for x in range(L+X+R):
            result[y][x] = f(y, x)
        
    for y in range(U, U+Y):
        for x in range(L):
            result[y][x] = f(y, x)
        for x in range(L, L+X):
            result[y][x] = word[y-U][x-L]
        for x in range(L+X, L+X+R):
            result[y][x] = f(y, x)
    
    for y in range(U+Y, U+Y+D):
        for x in range(L+X+R):
            result[y][x] = f(y, x)
    
    return [''.join(result[i]) for i in range(U+Y+D)]


# main 함수 ----------
Y, X = map(int, input().split())
U, L, R, D = map(int, input().split())
word = []
for _ in range(Y):
    word.append(list(input().rstrip()))
    
for i in solve():
    print(i)