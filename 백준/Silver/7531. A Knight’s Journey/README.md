# [Silver I] A Knight’s Journey - 7531 

[문제 링크](https://www.acmicpc.net/problem/7531) 

### 성능 요약

메모리: 111728 KB, 시간: 152 ms

### 분류

백트래킹

### 제출 일자

2025년 8월 1일 16:03:50

### 문제 설명

<p>The knight is getting bored of seeing the same black and white squares again and again and has decided to make a journey around the world. Whenever a knight moves, it is two squares in one direction and one square perpendicular to this.</p>

<p>The world of a knight is the chessboard he is living on. Our knight lives on a chessboard that has a smaller area than a regular 8 × 8 board, but it is still rectangular. Can you help this adventurous knight to make travel plans?</p>

<p style="text-align: center;"><img alt="" src="https://www.acmicpc.net/upload/images2/knight.png" style="height:156px; width:157px"></p>

<p style="text-align: center;">The eight possible moves of a knight</p>

<p>Find a path such that the knight visits every square once. The knight can start and end on any square of the board.</p>

### 입력 

 <p>The input begins with a positive integer n in the first line. The following lines contain n test cases.</p>

<p>Each test case consists of a single line with two positive integers p and q, such that 1 ≤ p · q ≤ 26. This represents a p × q chessboard, where p describes how many different square numbers 1, . . . , p exist, q describes how many different square letters exist. These are the first q letters of the Latin alphabet: A, . . .</p>

### 출력 

 <p>The output for every scenario begins with a line containing "Scenario #i:", where i is the number of the scenario starting at 1. Then print a single line containing the lexicographically first path that visits all squares of the chessboard with knight moves followed by an empty line. The path should be given on a single line by concatenating the names of the visited squares. Each square name consists of a capital letter followed by a number.</p>

<p>If no such path exist, you should output impossible on a single line.</p>

