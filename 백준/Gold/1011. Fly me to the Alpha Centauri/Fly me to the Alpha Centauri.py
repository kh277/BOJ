# 백준 1011

'''
최소한의 공간이동 장치 작동횟수를 구해야 한다. 먼저 예시를 보자.
0->3 : 1 1 1
1->5 : 1 2 1
45->50 : 1 2 1 1
0->32 :  1 2 3 4 5 (2) 5 4 3 2 1
0->32의 경우 가운데 2가 남는다. 이 경우는 1과 2 사이에 2를 끼워 넣으면 된다.
-> 1 2 3 4 5 5 4 3 (2) 2 1
'''

import sys

input = sys.stdin.readline

def solve(x: int, y: int) -> int:
    distance = y-x

    counter = 1
    while True:
        if distance - counter*2 > 0:
            distance -= counter*2
            counter += 1
            continue

        # ex) 12 = 1 2 3 (0) 3 2 1
        elif distance - counter*2 == 0:
            return counter*2
        
        # ex) 17 = 1 2 3 (7) 3 2 1
        elif distance - counter > 0:
            return counter*2
        
        # ex1) 16 = 1 2 3 (4) 3 2 1
        # ex2) 14 = 1 2 3 (2) 3 2 1
        else:
            return counter*2 - 1


def main():
    T = int(input())
    for i in range(T):
        x, y = map(int, input().split())
    
        print(solve(x, y))


main()