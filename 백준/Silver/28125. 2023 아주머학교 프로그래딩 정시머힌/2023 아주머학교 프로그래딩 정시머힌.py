# 백준 28125

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline


def solve(string):
    changeStr = {"@", "[", "!", ";", "^", "0", "7", "\\"}
    change = {"@": 'a', "[": 'c', "!": 'i', ";": 'j', "^": 'n', \
            "0": 'o', "7": 't', "\\'": 'v', "\\\\'": 'w'}

    result = ""
    index = 0
    changeCount = 0
    while index < len(string):
        if string[index] in changeStr:
            if string[index] == '\\':
                if string[index+1] == "'":
                    result += change["\\'"]
                    index += 1
                elif string[index+1] == '\\' and string[index+2] == "'":
                    result += change["\\\\'"]
                    index += 2
            else:
                if string[index] in changeStr:
                    result += change[string[index]]
            changeCount += 1
        else:
            result += string[index]
        index += 1

    return "I don't understand" if changeCount*2 >= len(result) else result


def main():
    N = int(input())
    for _ in range(N):
        string = input().decode().rstrip()
        print(solve(string))


main()
