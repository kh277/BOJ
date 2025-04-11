# [Gold V] Gift - 15795 

[문제 링크](https://www.acmicpc.net/problem/15795) 

### 성능 요약

메모리: 126076 KB, 시간: 124 ms

### 분류

수학, 슬라이딩 윈도우

### 제출 일자

2025년 4월 12일 01:47:33

### 문제 설명

<p>Karev really enjoys simple sequences of at most K numbers. A simple sequence of length K is a sequence formed by the numbers from 0 to K-1 in this order. For example, simple sequences are {0}, {0,1,2,3}, {0,1,2,3,4,5,6}, while the sequences {1}, {0,1,3,2}, {0,1,3} – are not.</p>

<p>Since Karev’s birthday is approaching, Polly would like to buy for him a few simple sequences and combine them into an interesting sequence. An interesting sequence is a sequence formed by concatenating a few simple sequences, each with length at most K. For example, let K=3. Then {0,1,2,0}, {0,1,0,1}, {0,0,0} and {0,1,2} are interesting sequences, but {0,1,2,3}, {0,1,1} and {0,0,2} are not.</p>

<p>Since Polly can choose many sequences, she is wondering which one to pick. Now she is curious how many choices she really has. Karev is a very good friend of Polly so she might decide to buy a really huge present for him.</p>

<p>Write a program gift to help Polly by solving the following problem: Given K – the maximum length of the simple sequences that Polly can buy, and N – the length of the interesting sequence that she wants to form, calculate how many different interesting sequences she could make. Since this number can be very large, output it modulo 1,000,000,007.</p>

### 입력 

 <p>Two numbers separated by space are given on the first line of the standard input – N and K, respectively.</p>

### 출력 

 <p>You should output a single number on the first line of the standard output – the number of different interesting sequences Polly can make with the current constraints. Output the answer modulo 1,000,000,007.</p>

