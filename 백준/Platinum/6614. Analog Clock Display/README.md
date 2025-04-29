# [Platinum IV] Analog Clock Display - 6614 

[문제 링크](https://www.acmicpc.net/problem/6614) 

### 성능 요약

메모리: 113572 KB, 시간: 348 ms

### 분류

기하학, 구현

### 제출 일자

2025년 4월 28일 22:34:07

### 문제 설명

<p>Our old clock chimed four o’clock, and with that last sound they dissolved into a pile of sticks. Since the craftsmanship necessary to fix them was forgotten and lost long time ago, we decided to replace them by a computer program.</p>

<p>An easy task, you say? There is one more little thing to mention: Recent studies of extraterrestrial aliens showed that they live in a digital world and therefore they are unable to read the traditional clock face with two moving hands. It is simply something beyond their technical capabilities. Therefore, the Security Board decided that our new clock must use such a traditional “analog” display to protect the time information against non-humans.</p>

### 입력 

 <p>The input contains several instances, each of them consisting of one row containing two integers H (0 ≤ H ≤ 23) and M (0 ≤ M ≤ 59) separated by a colon. M is always given with two digits, H has one or two digits, i.e., no leading zero unless H = 0.</p>

<p>The last test case is followed by the word “END”.</p>

### 출력 

 <p>For each input instance H:M, draw an “ASCII art” clock face depicting the time of H hours and M minutes according to the following specification.</p>

<p>The face frame is a square, with 51 characters per each side. These characters are uppercase letters “X”, with the exception of four corners and every tenth character, which is always “@”. The numbers 3, 6, 9, and 12 are centered at their appropriate sides, with exactly one space between them and the frame. There is one space between digits 1 and 2. The center of the face always contains the asterisk symbol: “*”. All visually “empty” characters are simple spaces.</p>

<p>Two hands are the only elements of the clock face that depend on the time. In the following description of the placement of the hands, we assume that each character (both space or occupied) is a 1× 1 square and the start (0, 0) of the coordinate system is placed in the center of the square containing the asterisk symbol, with the first axis pointing to the right, and the second axis upwards.</p>

<p>The hour hand is drawn as a line segment of length 15 starting at (0, 0). The hand points upwards at 12 o’clock and moves uniformly by the same angle each minute. Similarly, the minute hand is drawn as a line segment of length 21 starting at (0, 0). That hand points upwards every hour and also moves uniformly by the same angle every minute in the clockwise direction (what a surprise). The minute hand is considered to be above the hour hand, i.e., the characters representing the hour hand may be hidden by parts of the minute hand.</p>

<p>A line whose angle from the vertical direction is D degrees should be drawn as follows. If 0 ≤ D ≤ 45, one character is printed for each row i at (integer) coordinates (n<sub>i</sub>,i) as close as possible to the point (x<sub>i</sub>,i) that lies exactly on the geometric line (x<sub>i</sub> is a real number). If 45 ≤ D ≤ 90, there is one character printed for each column i at the (integer) coordinates (i,k<sub>i</sub>), the closest possible square to the (real) point (i,y<sub>i</sub>) on the line.</p>

<p>The character displayed to draw the line at some position (i,j) depends on the two “neighboring” characters of the line. The character is</p>

<ul>
	<li>minus symbol “-” if there are also characters at both positions (i − 1,j) and (i + 1,j),</li>
	<li>pipe symbol “|” if there are also characters at both positions (i,j − 1) and (i,j + 1),</li>
	<li>backslash symbol “\” if there are characters at positions (i − 1,j + 1) and (i + 1,j − 1),</li>
	<li>slash symbol “/” if there are also characters at positions (i − 1,j − 1) and (i + 1,j + 1),</li>
	<li>lowercase letter “o” otherwise.</li>
</ul>

<p>A line segment of length S starting at (0, 0) is drawn by displaying characters in the same way as drawing the corresponding line, but we only print such characters whose distance between the center of the square and the origin (0, 0) is at most S, 0 < |(0, 0),(i,j)| ≤ S, and only in one direction of the line.</p>

<p>Please see the sample output to resolve any ambiguities in the above description. Print one empty line after each clock face.</p>

