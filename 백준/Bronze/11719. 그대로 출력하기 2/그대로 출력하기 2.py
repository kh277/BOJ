# 백준 11718

'''
sys.stdin.readline().rstrip()은 EOFError가 발생할 경우,
에러를 리턴하는 것이 아니라 빈 문자열을 리턴하게 됨.
'''


import sys


def main():
    while True:
        try:
            print(input())
        except Exception:
            break


main()