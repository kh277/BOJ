# 백준 13140

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def checkNum(curNum, world):
    strNum = str(curNum)
    strWorld = str(world)

    # 한 자릿수인지 확인
    if len(strWorld) != 5:
        return False

    w = strWorld[0]
    o = strWorld[1]
    r = strWorld[2]
    l = strWorld[3]
    d = strWorld[4]

    # l, o 일치 확인
    if l != strNum[3] or o != strNum[4]:
        return False
    
    # 서로 다른 숫자인지 확인
    if len({w, r, d, strNum[0], strNum[1], strNum[2], strNum[4]}) != 7:
        return False
    
    return True


def solve(N):
    for h in range(1, 10):
        for e in range(10):
            if h == e:
                continue
            for l in range(10):
                if h == l or e == l:
                    continue
                for o in range(10):
                    if h == o or e == o or l == o:
                        continue

                    curNum = h*10000 + e*1000 + l*100 + l*10 + o
                    world = N - curNum
                    if checkNum(curNum, world) == True:
                        return [curNum, world]

    return [-1]


def main():
    N = int(input())
    result = solve(N)
    if result[0] == -1:
        print("No Answer")
    elif len(str(N)) == 6:
        print(f"  {result[0]}\n+ {result[1]}\n-------\n {N}")
    else:
        print(f"  {result[0]}\n+ {result[1]}\n-------\n  {N}")


main()
