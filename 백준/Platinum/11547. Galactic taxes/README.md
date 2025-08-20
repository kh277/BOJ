# [Platinum III] Galactic taxes - 11547 

[문제 링크](https://www.acmicpc.net/problem/11547) 

### 성능 요약

메모리: 119980 KB, 시간: 592 ms

### 분류

데이크스트라, 그래프 이론, 최단 경로, 삼분 탐색

### 제출 일자

2025년 8월 20일 11:01:20

### 문제 설명

<p>The year is 2115. The Interplanetary Commercial Planning Center (ICPC) is supported by the Autonomous Communication Ministry (ACM).</p>

<p>A commercial operation is performed executing transactions between connected ACM offices throughout the galaxy. The execution of a transaction between two connected ACM offices involves a nonnegative tax whose value increases, or decreases, continuously as a linear function A × t + B of time t, where t is a real number measured in minutes during the day (0 ≤ t ≤ 24 × 60).</p>

<p>The total tax of a commercial operation performed between a source ACM office and a destination ACM office at some time t, is calculated as the minimum possible sum of the taxes of the executed transactions between the ACM offices visited along some path from the source ACM office to the destination ACM office. The tax of each transaction is calculated at the same time t.</p>

<p>Since the tax of the transactions between connected ACM offices is continually changing during the day, it would be better to perform the commercial operation at some specific time in the day, in order to maximize the collected tax. At that time, ACM decides to perform the commercial operation, and not before or after.</p>

<p>Your task is to write a program that receives as input the description of the ACM office network and returns as output the maximum total tax of the commercial operation that can be achieved during the day, that is, the maximum total tax that ACM can collect.</p>

### 입력 

 <p>The first line contains two integers N and M, representing respectively the number of ACM offices in the network, and the number of connections (2 ≤ N ≤ 1000 and 1 ≤ M ≤ 10<sup>4</sup>). The ACM offices are identified with distinct integers from 1 to N, being 1 the source ACM office and N the destination ACM office. Each of the next M lines describes a connection with four integers I, J, A and B, indicating that there is a bidirectional connection between office I and office J (1 ≤ I < J ≤ N), such that the tax of a transaction executed between office I and office J at time t is defined by the formula A × t + B (−100 ≤ A ≤ 100 and 0 ≤ B ≤ 10<sup>6</sup>). Taxes are non-negative, so A×t+B ≥ 0 for 0 ≤ t ≤ 24×60. There is at most one connection between each pair of ACM offices, and there is at least one path between the source ACM office and the destination ACM office.</p>

### 출력 

 <p>Output a line with a rational number representing the maximum total tax that ACM can collect. The result must be output as a rational number with exactly five digits after the decimal point, rounded if necessary.</p>

