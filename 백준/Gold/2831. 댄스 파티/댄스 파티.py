# 백준 2831

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(N, man, woman):
    manPlus = []
    womanPlus = []
    manMinus = []
    womanMinus = []
    for i in range(N):
        if man[i] > 0:
            manPlus.append(man[i])
        else:
            manMinus.append(man[i])
        if woman[i] > 0:
            womanPlus.append(woman[i])
        else:
            womanMinus.append(woman[i])

    manPlus.sort()
    womanPlus.sort()
    manMinus.sort()
    womanMinus.sort()

    # 1. (자신보다 큰 여자 선호) + (자신보다 작은 남자 선호) 매칭
    manI = len(manPlus)-1
    womanI = 0
    result = 0
    while manI >= 0 and womanI < len(womanMinus):
        curM = manPlus[manI]
        curW = womanMinus[womanI]

        # 남자의 요구조건이 큰 경우
        if curM >= -curW:
            manI -= 1
        # 매칭이 가능한 경우
        else:
            result += 1
            manI -= 1
            womanI += 1

    # (자신보다 작은 여자 선호) + (자신보다 큰 남자 선호) 매칭
    womanI = len(womanPlus)-1
    manI = 0
    while womanI >= 0 and manI < len(manMinus):
        curM = manMinus[manI]
        curW = womanPlus[womanI]

        # 여자의 요구조건이 큰 경우
        if curW >= -curM:
            womanI -= 1
        # 매칭이 가능한 경우
        else:
            result += 1
            womanI -= 1
            manI += 1

    return result


def main():
    N = int(input())
    man = list(map(int, input().split()))
    woman = list(map(int, input().split()))
    print(solve(N, man, woman))


main()
