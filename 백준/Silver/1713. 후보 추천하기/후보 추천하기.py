# 백준 1713


import sys

input = sys.stdin.readline


def solve(N: int, recom: list, num: list) -> str:
    picture = []
    
    for cur in num:
        # 사진틀에 빈 자리가 있을 경우
        if len(picture) < N:
            append_success = False
            for i in range(len(picture)):
                if picture[i][0] == cur:
                    picture[i][1] += 1
                    append_success = True

            # [추천번호, 현재 추천 수, 경과 시간] 형태로 저장        
            if append_success == False:
                picture.append([cur, 1, 0])
        
        else:
            # 사진틀에 추천하는 학생이 있을 경우
            append_success = False
            for i in range(len(picture)):
                if picture[i][0] == cur:
                    picture[i][1] += 1
                    append_success = True

            # 사진틀에 추천하는 학생이 없을 경우        
            if append_success == False:
                picture.sort(key= lambda x: [-x[1], x[2]])
                picture[-1] = [cur, 1, 0]
        
        # 시간 경과
        for j in range(len(picture)):
            picture[j][2] += 1  

    return sorted([x[0] for x in picture])


def main():
    N = int(input())
    recom = int(input())
    num = list(map(int, input().split()))

    print(*solve(N, recom, num))


main()