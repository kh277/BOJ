# [Gold IV] Endless Knight (Small) - 12701 

[문제 링크](https://www.acmicpc.net/problem/12701) 

### 성능 요약

메모리: 111460 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2026년 2월 3일 12:46:54

### 문제 설명

<p>In the game of chess, there is a piece called the knight. A knight is special -- instead of moving in a straight line like other pieces, it jumps in an "L" shape. Specifically, a knight can jump from square (r1, c1) to (r2, c2) if and only if (r1 - r2)<sup>2</sup> + (c1 - c2)<sup>2</sup> = 5.</p>

<p>In this problem, one of our knights is going to undertake a chivalrous quest of moving from the top-left corner (the (1, 1) square) to the bottom-right corner (the (<strong>H</strong>, <strong>W</strong>) square) on a gigantic board. The chessboard is of height <strong>H</strong> and width <strong>W</strong>.</p>

<p>Here are some restrictions you need to know.</p>

<ul>
	<li>The knight is so straightforward and ardent that he is only willing to move towards the right <em>and</em> the bottom. In other words, in each step he only moves to a square with a bigger row number and a bigger column number. Note that, this might mean that there is no way to achieve his goal, for example, on a 3 by 10 board.</li>
	<li>There are <strong>R</strong> squares on the chessboard that contain rocks with evil power. Your knight may not land on any of such squares, although flying over them during a jump is allowed.</li>
</ul>

<p>Your task is to find the number of unique ways for the knight to move from the top-left corner to the bottom-right corner, under the above restrictions. It should be clear that sometimes the answer is huge. You are asked to output the remainder of the answer when divided by 10007, a prime number.</p>

### 입력 

 <p>Input begins with a line containing a single integer, <strong>N</strong>.  <strong>N</strong> test cases follow.</p>

<p>The first line of each test case contains 3 integers,  <strong>H</strong>, <strong>W</strong>, and  <strong>R</strong>. The next <strong>R</strong> lines each contain 2 integers each, <strong>r</strong> and <strong>c</strong>, the row and column numbers of one rock. You may assume that (1, 1) and (<strong>H</strong>, <strong>W</strong>) never contain rocks and that no two rocks are at the same position.</p>

<p>Limits</p>

<ul>
	<li>1 ≤ <strong>N</strong> ≤ 100</li>
	<li>0 ≤ <strong>R</strong> ≤ 10</li>
	<li>1 ≤ <strong>W</strong> ≤ 100</li>
	<li>1 ≤ <strong>H</strong> ≤ 100</li>
	<li>1 ≤ <strong>r</strong> ≤ H</li>
	<li>1 ≤ <strong>c</strong> ≤ W</li>
</ul>

### 출력 

 <p>For each test case, output a single line of output, prefixed by "Case #<strong>X</strong>: ", where <strong>X</strong> is the 1-based case number, followed by a single integer indicating the number of ways of reaching the goal, modulo 10007.</p>

