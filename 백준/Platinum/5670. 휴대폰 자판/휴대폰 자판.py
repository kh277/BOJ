# 백준 5670

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
END_POINT = 0


class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, value):
        curV = self.root
        for v in value:
            if v not in curV:
                curV[v] = dict()
            curV = curV[v]
        curV[END_POINT] = True


def DFS(trie):
    result = 0
    start = trie.root
    stack = [[start, 0]]

    while stack:
        curV, count = stack.pop()

        addFlag = 0
        if curV == trie.root or len(curV.items()) > 1:
            addFlag = 1

        for key, nextV in curV.items():
            if key == END_POINT:
                result += count
            else:
                stack.append([nextV, count+addFlag])

    return result


def main():
    while True:
        try:
            trie = Trie()
            N = int(input())
            word = []
            for _ in range(N):
                w = input().decode().rstrip()
                word.append(word)
                trie.add(w)

            print(f"{round(DFS(trie)/N, 2):.2f}")
        except:
            break


main()
