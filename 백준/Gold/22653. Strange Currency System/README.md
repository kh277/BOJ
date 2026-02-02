# [Gold IV] Strange Currency System - 22653 

[문제 링크](https://www.acmicpc.net/problem/22653) 

### 성능 요약

메모리: 109768 KB, 시간: 96 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2026년 2월 2일 13:52:18

### 문제 설명

<p>The currency system in the Kingdom of Yoax-Musty is strange and fairly inefficient. Like other countries, the kingdom has its own currencty unit denoted by K \$ (kingdom dollar). However, the Ministry of Finance issues bills for every value between 1 K \$ and (2<sup>31</sup> - 1) K \$ worth.</p>

<p>On the other hand, this system often enables people to make many different values just with a small number of bills. For example, if you have four bills of 1 K \$, 2 K \$, 4 K \$, and 8 K \$ worth respectively, you can make any values from 1 K #36; to 15 K \$.</p>

<p>In this problem, you are requested to write a program that finds the minimum value that cannot be made with a given set (multiset in a mathematical sense) of bills. For the case with the four bills (1 K \$, 2 K \$, 4 K \$, and 8 K \$), since you can make any values up to 15 K \$, your program should report 16 K $.</p>

### 입력 

 <p>The input consists of two lines. The first line contains an integer <i>N</i> (1 ≤ <i>N</i> ≤ 10000), the number of bills. The second line contains <i>N</i> integers, each of which represents the value of a bill in K \$. There may be multiple bills of the same value.</p>

### 출력 

 <p>Print the minimum value unable to be made on a line. The value should be given in K \$ and without any currency sign or name.</p>

