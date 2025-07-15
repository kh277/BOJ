# [Platinum IV] Keylogger - 22274 

[문제 링크](https://www.acmicpc.net/problem/22274) 

### 성능 요약

메모리: 127972 KB, 시간: 3184 ms

### 분류

이분 탐색, 다이나믹 프로그래밍, 누적 합

### 제출 일자

2025년 7월 15일 15:22:32

### 문제 설명

<p>Lately you have been very curious about your typing speed, and you have been wondering how long it takes for you to press each key on your keyboard, which has K keys.</p>

<p>To figure that out, you installed a keylogger on your own computer. It has been registering the delta time between each pair of key presses. After collecting data for a couple of weeks, you now have access to a 2-dimensional matrix T with K rows and K columns. The element at the i-th row and j-th column is T<sub>i,j</sub>, and it represents how long it takes, on average, for you to press the key j right after having pressed the key i. For example, the element T<sub>3,5</sub> represents how long it takes, on average, for you to press the key 5 right after having pressed the key 3. Coincidentally, each row on T is ordered non-decreasingly.</p>

<p>Given that your typing speed varies according to the time of the day and your mood, your keylogger has also given you a latency margin error L. That means that, for every pair of keys i and j on your keyboard, it actually takes between T<sub>i,j</sub> −L and T<sub>i,j</sub> +L, inclusive, for you to press the key j right after having pressed the key i.</p>

<p>You classified for the South American ICPC regional competition, and you have been asked to update some of your contact information on the ICPC website. The problem is that you have been studying so hard that you forgot your password. All you remember is that your password has length N. Luckily, your keylogger also has data about the last time you typed your password on that website. So now you have an array P with N − 1 elements. Each element P<sub>i</sub> represents the delta time between each consecutive key presses from your password. In other words, P<sub>1</sub> represents the delta time between you pressing the keys of the first and the second characters of your password, P<sub>2</sub> is the delta time between you pressing the keys of the second and third characters of your password, and so on. Notice that the latency L does not apply to P, because each P<sub>i</sub> is not an average but a single delta time, measured precisely.</p>

<p>You need to recover your password as soon as possible. Your plan now is to try every sequence of keys that is compatible with the information you have. A sequence S of length N is compatible with L, T, and P if each pair of consecutive keys S<sub>i</sub> and S<sub>i+1</sub> satisfy that T<sub>S<sub>i</sub>,S<sub>i+1</sub></sub> − L ≤ P<sub>i</sub> ≤ T<sub>S<sub>i</sub>,S<sub>i+1</sub></sub> + L. How many such sequences are there?</p>

### 입력 

 <p>The first line contains two integers K (1 ≤ K ≤ 750) and L (0 ≤ L ≤ 10<sup>9</sup>), indicating respectively how many keys are there on your keyboard and the latency margin error given by your keylogger. The next K lines contain K integers each, representing the matrix T. The j-th integer on the i-th line is T<sub>i,j</sub> (1 ≤ T<sub>i,j</sub> ≤ 10<sup>9</sup> for i = 1, 2, . . . , K and j = 1, 2, . . . , K). Recall that T<sub>i,j</sub> indicates how long it takes, on average, for you to press the key j right after having pressed the key i, and that each row on T is ordered non-decreasingly (T<sub>i,j</sub> ≤ T<sub>i,j+1</sub> for i = 1, 2, . . . , K and j = 1, 2, . . . , K − 1). The next line contains an integer N (2 ≤ N ≤ 10<sup>4</sup>), representing the length of your password. The final line contains N − 1 integers P<sub>1</sub>, P<sub>2</sub>, . . . , P<sub>N−1</sub> (1 ≤ P<sub>i</sub> ≤ 10<sup>9</sup> for i = 1, 2, . . . , N − 1), denoting the delta time between each consecutive key presses from your password.</p>

### 출력 

 <p>Output a single line with an integer indicating how many different sequences of keys are compatible with the information you have. Because this number can be very large, output the remainder of dividing it by 10<sup>9</sup> + 7.</p>

