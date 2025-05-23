# 백준 1270

'''
보이어-무어 다수결 투표 알고리즘을 이용하면 O(N)으로 해결이 가능하다.
'''

import io


def MajorityVote(nums):
    candidate = None
    count = 0
    for i in range(1, nums[0]+1):
        # 후보가 실질적으로 0번 등장한 경우 -> 후보 교체
        if count == 0:
            candidate = nums[i]
            count = 1
        # 후보가 등장한 경우
        elif nums[i] == candidate:
            count += 1
        # 후보가 등장하지 않은 경우
        else:
            count -= 1
    
    if candidate != None and nums.count(candidate) > (len(nums)-1)//2:
        return candidate

    return 'SYJKGW'


def main():
    input = io.BufferedReader(io.FileIO(0), 1<<18).readline

    N = int(input())
    for _ in range(N):
        T = list(map(int, input().split()))
        print(MajorityVote(T))


main()
