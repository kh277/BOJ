# [Gold II] Counting Subsequences - 27838 

[문제 링크](https://www.acmicpc.net/problem/27838) 

### 성능 요약

메모리: 9776 KB, 시간: 52 ms

### 분류

누적 합

### 제출 일자

2026년 2월 10일 12:34:31

### 문제 설명

<p><b>"47 is the quintessential random number,"</b> states the 47 society. And there might be a grain of truth in that.</p>

<p>For example, the first ten digits of the Euler's constant are:</p>

<p style="text-align: center;"><code>2 7 1 8 2 8 1 8 2 8</code></p>

<p>And what's their sum? Of course, it is 47.</p>

<p>Try walking around with your eyes open. You may be sure that soon you will start discovering occurences of the number 47 everywhere.</p>

<p>You are given a sequence <b>S</b> of integers we saw somewhere in the nature. Your task will be to compute how strongly does this sequence support the above claims.</p>

<p>We will call a <b>continuous</b> subsequence of <b>S</b> <i>interesting</i> if the sum of its terms is equal to 47.</p>

<p>E.g., consider the sequence <b>S</b> = <code>(24, 17, 23, 24, 5, 47)</code>. Here we have two interesting continuous subsequences: the sequence <code>(23, 24)</code> and the sequence <code>(47)</code>.</p>

<p>Given a sequence <b>S</b>, find the count of its interesting subsequences.</p>

### 입력 

 <p>The first line of the input file contains an integer <b>T</b> specifying the number of test cases. Each test case is preceded by a blank line.</p>

<p>The first line of each test case contains the length of a sequence <b>N</b>. The second line contains <b>N</b> space-separated integers <strong>A<sub>i</sub></strong> – the elements of the sequence.</p>

### 출력 

 <p>For each test case output a single line containing a single integer – the count of interesting subsequences of the given sentence.</p>

