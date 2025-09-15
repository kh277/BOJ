# [Gold IV] The Cow Prom - 26987 

[문제 링크](https://www.acmicpc.net/problem/26987) 

### 성능 요약

메모리: 113992 KB, 시간: 128 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2025년 9월 15일 13:59:02

### 문제 설명

<p>The N (2 ≤ N ≤ 10,000) cows are so excited: it's prom night! They are dressed in their finest gowns, complete with corsages and new shoes. They know that tonight they will each try to perform the Round Dance.</p>

<p>Only cows can perform the Round Dance which requires a set of ropes and a circular stock tank. To begin, the cows line up around a circular stock tank and number themselves in clockwise order consecutively from 1..N. Each cow faces the tank so she can see the other dancers.</p>

<p>They then acquire a total of M (2 ≤ M ≤ 50,000) ropes all of which are distributed to the cows who hold them in their hooves. Each cow hopes to be given one or more ropes to hold in both her left and right hooves; some cows might be disappointed.</p>

<p>For the Round Dance to succeed for any given cow (say, Bessie), the ropes that she holds must be configured just right. To know if Bessie's dance is successful, one must examine the set of cows holding the other ends of her ropes (if she has any), along with the cows holding the other ends of any ropes they hold, etc. When Bessie dances clockwise around the tank, she must instantly pull all the other cows in her group around clockwise, too. Likewise, if she dances the other way, she must instantly pull the entire group counterclockwise (anti-clockwise in British English).</p>

<p>Of course, if the ropes are not properly distributed then a set of cows might not form a proper dance group and thus can not succeed at the Round Dance. One way this happens is when only one rope connects two cows. One cow could pull the other in one direction, but could not pull the other direction (since pushing ropes is well-known to be fruitless). Note that the cows must Dance in lock-step: a dangling cow (perhaps with just one rope) that is eventually pulled along disqualifies a group from properly performing the Round Dance since she is not immediately pulled into lockstep with the rest.</p>

<p>Given the ropes and their distribution to cows, how many groups of cows can properly perform the Round Dance? Note that a set of ropes and cows might wrap many times around the stock tank.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..M+1: Each line contains two space-separated integers A and B that describe a rope from cow A to cow B in the clockwise direction.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: A single line with a single integer that is the number of groups successfully dancing the Round Dance.</li>
</ul>

