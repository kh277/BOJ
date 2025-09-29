# [Silver IV] Sudoku Verify - 34444 

[문제 링크](https://www.acmicpc.net/problem/34444) 

### 성능 요약

메모리: 108608 KB, 시간: 92 ms

### 분류

구현, 비트마스킹

### 제출 일자

2025년 9월 29일 16:45:50

### 문제 설명

<p>A Sudoku puzzle is a number puzzle that is played on a $9 \times 9$ grid of cells. These cells are grouped into nine ($9$) non-overlapping $3 \times 3$ <em>regions</em>, for a total of nine ($9$) cells per region. The regions are shown outlined in bold on the figure on the right.</p>

<p>The initial state of the grid has some of the cells filled in (black in the figure on the right).  The objective is to use logical inferences to fill in the rest of the board. But there are rules for how to fill out the remainder of the board. The rules are as follows:</p>

<ul>
	<li>Along every column, every number between $1$ and $9$ (inclusive) must appear exactly once.</li>
	<li>Along every row, every number between $1$ and $9$ (inclusive) must appear exactly once.</li>
	<li>In each $3 \times 3$ region, every number between $1$ and $9$ (inclusive) must appear exactly once.</li>
</ul>

<p>You are given a completed Sudoku puzzle. Determine whether it is valid.</p>

### 입력 

 <p>Each row of the filled out Sudoku puzzle corresponds to one line of input. The numbers of each row are separated by a single space. This encoding leads to an input with exactly nine ($9$) lines each of which contains exactly nine ($9$) numbers between $1$ and $9$ inclusive.</p>

### 출력 

 <p>If the Sudoku board is valid, output the text "VALID" (without the quotes).</p>

<p>If the Sudoku board is not valid, output the text "INVALID!" (without the quotes).</p>

