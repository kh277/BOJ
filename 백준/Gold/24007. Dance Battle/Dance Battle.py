# 백준 24007

'''
Delay를 적절하게 사용하면 라이벌 팀의 실력을 오름차순으로 정렬할 수 있다.
따라서 에너지가 소진될 때까지 Dance를 진행하고, 에너지가 소진되면 가장 뒤에 있는 라이벌에게 Recruit을 하면 된다.

주의해야 할 점은 마지막으로 Recruit을 하고 종료되는 경우, Recruit을 하여 Honor를 소비할 필요가 없다.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(E, N, num):
    num.sort()

    leftE = E
    start = 0
    end = N-1
    honor = 0
    while start <= end:
        # Dance가 가능한 경우 -> Dance
        if leftE - num[start] > 0:
            leftE -= num[start]
            honor += 1
            start += 1

        # Dance가 불가능한 경우
        else:
            # Recruit이 가능한 경우
            if honor > 0 and end - start > 1:
                honor -= 1
                leftE += num[end]
                end -= 1
            # Recruit이 불가능한 경우
            else:
                break

    return honor


def main():
    T = int(input())
    for i in range(1, T+1):
        E, N = map(int, input().split())
        num = list(map(int, input().split()))
        print(f"Case #{i}: {solve(E, N, num)}")


main()
