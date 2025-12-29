# [Gold IV] Lipschitz Constant - 16516 

[문제 링크](https://www.acmicpc.net/problem/16516) 

### 성능 요약

메모리: 14500 KB, 시간: 116 ms

### 분류

그리디 알고리즘, 수학, 정렬

### 제출 일자

2025년 12월 29일 12:12:08

### 문제 설명

<p>Today you are doing your calculus homework, and you are tasked with finding a Lipschitz constant for a function f(x), which is defined for N integer numbers x and produces real values. Formally, the Lipschitz constant for a function f is the smallest real number L such that for any x and y with f(x) and f(y) defined we have:</p>

<p style="text-align: center;">|f(x) − f(y)| ≤ L · |x − y|.</p>

### 입력 

 <p>The first line contains N – the number of points for which f is defined. The next N lines each contain an integer x and a real number z, which mean that f(x) = z. Input satisfies the following constraints:</p>

<ul>
	<li>2 ≤ N ≤ 200 000.</li>
	<li>All x and z are in the range −10<sup>9</sup> ≤ x, z ≤ 10<sup>9</sup>.</li>
	<li>All x in the input are distinct.</li>
</ul>

### 출력 

 <p>Print one number – the Lipschitz constant. The result will be considered correct if it is within an absolute error of 10<sup>−4</sup> from the jury’s answer.</p>

