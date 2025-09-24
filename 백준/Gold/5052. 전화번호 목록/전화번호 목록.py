# 백준 5052

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
END_POINT = -1


class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, value):
        curV = self.root
        for v in value:
            if v not in curV:
                curV[v] = dict()
            # 접두사가 일치하는 경우 False 처리
            if END_POINT in curV:
                return False
            curV = curV[v]
        curV[END_POINT] = True
        return True


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        trie = Trie()
        data = []
        for _ in range(N):
            data.append(input().decode().rstrip())
        data.sort()

        flag = True
        for i in range(N):
            if trie.add(data[i]) == False:
                print("NO")
                flag = False
                break

        if flag == True:
            print("YES")


main()
