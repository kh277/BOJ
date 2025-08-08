# [Gold IV] Geometry Darts - 11119 

[문제 링크](https://www.acmicpc.net/problem/11119) 

### 성능 요약

메모리: 112868 KB, 시간: 2648 ms

### 분류

기하학, 구현

### 제출 일자

2025년 8월 8일 11:38:50

### 문제 설명

<p>Bob and Hannah like to play darts. They are not very good at it, however, so finishing a round of 501 Darts will take an eternity. They therefore decide to throw away the dartboard completely and put geometric shapes on the wall instead, awarding points according to the number of shapes the dart penetrates. To reduce the complexity of scoring, they only use circles, triangles and rectangles.</p>

<p>A game consists of each person throwing 3 darts each, and your job is to find the winner of the game, given the shapes and the throws.</p>

### 입력 

 <p>The input will start with a line giving the total number of shapes, S. Then follow S lines describing the shapes, in either of the following formats:</p>

<p>C x y r, where (x, y) is the center of the circle, and r is the radius.<br>
R x<sub>1</sub> y<sub>1</sub> x<sub>2</sub> y<sub>2</sub>, where (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>) are two corners of the rectangle with x<sub>1</sub> < x<sub>2</sub> and y<sub>1</sub> < y<sub>2</sub>.<br>
T x<sub>1</sub> y<sub>1</sub> x<sub>2</sub> y<sub>2</sub> x<sub>3</sub> y<sub>3</sub>, where (x<sub>i</sub>, y<sub>i</sub>) are the three corners of the triangle. </p>

<p>Then follows a line with N, the number of games Bob and Hannah play. Each game is described with six lines giving the x and y coordinates of the 6 throws, the first three by Bob and the last three by Hannah.</p>

<ul>
	<li>0 < S ≤ 1000</li>
	<li>0 < N ≤ 1000</li>
	<li>All rectangles have sides parallell to the x- and y-axis.</li>
	<li>For triangle specifications, the three points will never be collinear.</li>
	<li>All coordinates are given with double precision, with up to 6 decimals after the decimal points.</li>
	<li>All shapes are bounded by the rectangle defined by the two points (−1000, −1000) and (1000, 1000).</li>
	<li>All throws are guaranteed to be at least 10<sup>−6</sup> away from any shape boundary.</li>
</ul>

### 출력 

 <p>Output the name of the winner on a separate line for each game, or Tied if there is a tie.</p>

