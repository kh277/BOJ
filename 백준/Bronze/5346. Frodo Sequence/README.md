# [Bronze I] Frodo Sequence - 5346 

[문제 링크](https://www.acmicpc.net/problem/5346) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 11월 20일 10:06:14

### 문제 설명

<p>The Fibonacci sequence is a famous integer sequence defined by Leonardo of Pisa in 1202. The sequence is defined as follows:</p>

<ul>
	<li>Fib<sub>1</sub> = 1</li>
	<li>Fib<sub>2</sub> = 1</li>
	<li>Fib<sub>3</sub> = 2</li>
	<li>Fib<sub>4</sub> = 3</li>
	<li>Fib<sub>5</sub> = 5</li>
	<li>…</li>
	<li>Fib<sub>n</sub> = Fib<sub>n-1</sub> + Fib<sub>n-2</sub> for all n>2</li>
</ul>

<p>What you may not know is that Frodo of Bag End also defined an integer sequence called the Frodo sequence. Frodo’s sequence is defined as follows:</p>

<ul>
	<li>Fro<sub>1</sub> = 1</li>
	<li>Fro<sub>2</sub> = 1</li>
	<li>Fro<sub>3</sub> = 2</li>
	<li>Fro<sub>4</sub> = 2</li>
	<li>Fro<sub>5</sub> = 3</li>
	<li>…</li>
	<li>Fro<sub>n</sub> = Fro<sub>n-1</sub> + Fro<sub>n-2</sub> - Fro<sub>n-3</sub> for all n>3</li>
</ul>

<p>You need to write a program that given n finds Fro<sub>n</sub>.</p>

### 입력 

 <p>he input will be a sequence of integers, one per line. The end of input will be signaled by the integer 0. All integers, other than the last (zero), are positive and less than 2<sup>31</sup>.</p>

### 출력 

 <p>For each positive integer, n, print Fro<sub>n</sub>.</p>

