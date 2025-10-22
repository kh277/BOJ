# [Gold I] Almost Clear - 7794 

[문제 링크](https://www.acmicpc.net/problem/7794) 

### 성능 요약

메모리: 126920 KB, 시간: 4392 ms

### 분류

기하학, 선분 교차 판정

### 제출 일자

2025년 6월 12일 00:14:23

### 문제 설명

<p>In ACM (Awkward Commodity Museum), like every other museum, collects many valuable objects from every place around the globe, therefore several surveillance cameras are installed to watch over the museum for possible unauthorized access. In order to assure maximum surveillance, Mr. Effendy as the Head Security of ACM proposed such layout that all valuable objects being displayed must be visible from one of the cameras.</p>

<p>In ACM, Mr. Halim from the QCD (Quality Control Department) is in charge to verify the layout Mr. Effendy proposed. Usually he develops program to help him do the verifying process, but he is currently busy helping some public forum to understand about Binary Search Tree and the likes of which a programmer like you should already mastered. You should help Mr. Halim before he’s fired because stealing company’s hour to do things irrelevant to his position.</p>

<p>Mr. Halim is asked to write a program that accepts a layout, and verify that all valuable objects are visible by at least one of the camera installed. You must help him! Mr. Halim is a very brilliant guy; he doesn’t require you to write a complete solution. Write a program that receives 3 parameters: polygon A, polygon B, point C and determine whether polygon A (the valuable object) is “hidden” by polygon B (other object) when a camera is installed at point C. Note that your program is only need to deal with these 3 objects and nothing more, Mr. Halim will do the rest.</p>

<p>You may safely assume that:</p>

<ol>
	<li>Your program deals in 2-D coordinates.</li>
	<li>Polygon A and B is convex.</li>
	<li>The camera has infinite vision (meaning that it can see an object very far away).</li>
	<li>The camera can rotate 360 degrees freely.</li>
	<li>The camera cannot move.</li>
	<li>All position will be valid. Polygons do not intersect each other; camera will not be inside any of the polygons.</li>
	<li>All the characters and events described above are fictional. Any similarity of names of the characters and events is partially accidentally. No polygons were harmed during the making of this problem</li>
</ol>

### 입력 

 <p>The first line of input contains an integer T (1 ≤ T ≤ 1,000), the number of test cases follow. N</p>

<p>Each case begins with an integer M1 (1 ≤ M1 ≤ 1,000), the number of vertices of polygon A, and then followed by M1 integer-pairs which are the X-coordinate and Y-coordinate of each vertex in counter-clockwise direction. The second line will be the description of polygon B in the same format and constraint as the description of polygon A. The third line will be 2 integers which are the X-coordinate and Y-coordinate of the camera respectively. All coordinates will be non-negative and fit in 31-bit integer.</p>

### 출력 

 <p>Output for each test case will be in one line. Print “CLEAR” if polygon A is not obstructed by polygon B at all, print “ALMOST CLEAR” if polygon A is obstructed partially by polygon B, or print “NO VISION” if polygon A is fully hidden by polygon B.</p>

