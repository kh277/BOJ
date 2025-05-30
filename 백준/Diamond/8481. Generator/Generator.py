# 백준 8481

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
MOD = 9099099909999099999
strMOD = '9099099909999099999'
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


# 단순 출력
def gen0():
    print('ONTAK 2010\n')


# (글자) * (반복되는 횟수)를 저장한 뒤 출력
def gen1():
    # 런타임 전의 전처리
    s = "Godzila terorizes Bajtoly lower again. Every day a monster comes out of the ocean, slow movement of marching through the city to some of the skyscrapers and eats it with people who are in it. Eating one skyscraper takes the whole day, at dusk, it returns to its hiding place hiden in the depths. To make maters worse, going through the city, Godzila wags its tail and destroys towers, near the pases. The prospect of becoming a meal for an underwater monster, to discourage some residents spent in uncomfort- tion in the city. During the night of each tower is derived as a resident and fles to the countryside. In Bajtogrodzie skyscrapers were built only at stret crosings. At each intersection there is exactly one building. Junctions are conected by two-way strets. In adition, a the junction is just above the ocean, this is where Godzila begins its destructive journey through the city. During the investigation, the monster moves only in the strets. Godzila noted that he must hury up with the consumption of residents and carefuly chose the skyscrapers devouring and strets, which reaches them. Of course, chosing never previously consumed or destroyed- wanego skyscraper. What is the maximum number of people who can eat before the city completely desolate? Entrance The first line of standard input contains two integers him (1 n 10 0, 0 50 0 m) respectively denoting the number of intersections in the city and the number of conecting strets. Crosroads numbers are numbered from 1 to n, junction 1 is located on the shores of the ocean. Next row contains a sequence of integers n s (0 s 10 0) to describe population skyscrapers at various intersections. In each of the next m rows are the two integers ai and bi (1 ai, bi n, ai = bi), which means that there is a road junction conecting ai and bi. The crosing number One can reach any other intersection in the city. Exit Write to stdout the number of people who eat Godzila for the optimum choice of meals and roads through the city every day. Example For input: the result is corect: 5 5 1 1 3 2 4 7 1 2 1 3 2 3 2 4 3 5"

    c = [2932, 2931, 2928, 2923, 2916, 5803, 2883, 2868, 2851, 2832, 5599, 2763, 2736, 2707, 2676, 2643, 2608, 2571, 2532, 2491, 2448, 2403, 2356, 2307, 2256, 2203, 2148, 2091, 2032, 1971, 1908, 1843, 1776, 1707, 1636, 1563, 1488, 1411, 1332, 1251, 1168, 1083, 996, 907, 816, 723, 628, 531, 432, 331, 228, 123, 16, 2839, 2728, 2615, 2500, 2383, 2264, 2143, 2020, 1895, 1768, 1639, 1508, 1375, 1240, 1103, 964, 823, 680, 535, 388, 239, 88, 2867, 2712, 2555, 2396, 2235, 2072, 1907, 1740, 1571, 1400, 1227, 1052, 875, 696, 515, 332, 147, 2892, 2703, 2512, 2319, 2124, 1927, 1728, 1527, 1324, 1119, 912, 703, 492, 279, 64, 2779, 2560, 2339, 2116, 1891, 1664, 1435, 1204, 971, 736, 499, 260, 19, 2708, 2463, 2216, 1967, 1716, 1463, 1208, 951, 692, 431, 168, 2835, 2568, 2299, 2028, 1755, 1480, 1203, 924, 643, 360, 75, 2720, 2431, 2140, 1847, 1552, 1255, 956, 655, 352, 47, 2672, 2363, 2052, 1739, 1424, 1107, 788, 467, 144, 2751, 2424, 2095, 1764, 1431, 1096, 759, 420, 79, 2668, 2323, 1976, 1627, 1276, 923, 568, 211, 2784, 2423, 2060, 1695, 1328, 959, 588, 215, 2772, 2395, 2016, 1635, 1252, 867, 480, 91, 2632, 2239, 1844, 1447, 1048, 647, 244, 2771, 2364, 1955, 1544, 1131, 716, 299, 2812, 2391, 1968, 1543, 1116, 687, 256, 2755, 2320, 1883, 1444, 1003, 560, 115, 2600, 2151, 1700, 1247, 792, 335, 2808, 2347, 1884, 1419, 952, 483, 12, 2471, 1996, 1519, 1040, 559, 76, 2523, 2036, 1547, 1056, 563, 68, 2503, 2004, 1503, 1000, 495, 2920, 2411, 1900, 1387, 872, 355, 2768, 2247, 1724, 1199, 672, 143, 2544, 2011, 1476, 939, 400, 2791, 2248, 1703, 1156, 607, 56, 2435, 1880, 2087, 203, 2572, 2007, 1440, 871, 300, 2659, 2084, 1507, 928, 347, 2696, 2111, 1524, 935, 344, 2683, 2088, 1491, 892, 291, 2620, 2015, 1408, 799, 188, 2507, 1892, 1931, 35, 2344, 1719, 1092, 463, 2764, 2131, 1496, 859, 220, 2511, 1868, 1223, 576, 2859, 2208, 1555, 900, 243, 2516, 1855, 1192, 527, 2792, 2123, 1452, 779, 104, 2359, 1680, 999, 316, 2563, 1876, 1187, 496, 2735, 2040, 1343, 644, 5047, 1467, 760, 51, 2272, 1559, 844, 127, 2340, 1619, 896, 171, 2376, 1647, 916, 183, 2380, 1643, 904, 163, 2352, 1607, 860, 111, 2292, 1539, 784, 27, 2200, 1439, 676, 2843, 2076, 1307, 536, 2695, 1920, 1143, 364, 2515, 1732, 947, 160, 2303, 1512, 719, 2856, 2059, 1260, 3047, 1783, 976, 167, 2288, 1475, 660, 2775, 1956, 1135, 312, 2419, 1592, 763, 2864, 2031, 1196, 359, 2452, 1611, 768, 2855, 2008, 1159, 308, 2387, 1532, 675, 2748, 1887, 1024, 159, 2224, 1355, 484, 2543, 1668, 791, 2844, 1963, 1080, 195, 2240, 1351, 460, 2499, 1604, 707, 2740, 1839, 936, 31, 2056, 1147, 236, 2255, 1340, 423, 2436, 1515, 592, 2599, 1672, 743, 2744, 1811, 876, 2871, 1932, 991, 48, 2035, 1088, 139, 2120, 1167, 212, 2187, 1228, 267, 2236, 1271, 304, 2267, 1296, 323, 2280, 1303, 324, 2275, 1292, 307, 2252, 1263, 272, 2211, 1216, 219, 2152, 1151, 148, 2075, 1068, 59, 1980, 967, 2884, 1867, 848, 2759, 1736, 711, 2616, 1587, 556, 2455, 1420, 383, 2276, 1235, 192, 2079, 1032, 2915, 1864, 811, 2688, 1631, 572, 2443, 1380, 315, 2180, 1111, 40, 1899, 824, 2679, 1600, 519, 2368, 1283, 196, 2039, 948, 2787, 1692, 595, 2428, 1327, 224, 2051, 944, 2767, 1656, 543, 2360, 1243, 124, 1935, 812, 2619, 1492, 363, 2164, 1031, 2828, 1691, 552, 2343, 1200, 55, 1840, 691, 2472, 1319, 164, 1939, 780, 2551, 1388, 223, 1988, 819, 2580, 1407, 232, 1987, 808, 2559, 1376, 191, 1936, 3235, 1295, 100, 1835, 636, 2367, 1164, 2891, 1684, 475, 2196, 983, 2700, 1483, 264, 1975, 752, 2459, 1232, 3, 1704, 471, 2168, 931, 2624, 1383, 140, 1827, 580, 2263, 1012, 2691, 1436, 179, 1852, 591, 2260, 995, 2660, 1391, 120, 1779, 504, 2159, 880, 2531, 1248, 2895, 1608, 319, 1960, 667, 2304, 1007, 2640, 1339, 36, 1663, 356, 1979, 668, 2287, 972, 2587, 1268, 2879, 1556, 231, 1836, 507, 2108, 775, 2372, 3663, 1287, 2876, 1531, 184, 1767, 2411, 640, 2215, 856, 2427, 1064, 2631, 1264, 2827, 1456, 83, 1640, 263, 1816, 435, 1984, 599, 2144, 755, 2296, 903, 2440, 1043, 2576, 1175, 2704, 1299, 2824, 1415, 4, 1523, 108, 1623, 204, 1715, 292, 1799, 372, 1875, 444, 1943, 508, 2003, 564, 2055, 612, 2099, 652, 2135, 684, 2163, 708, 2183, 724, 2195, 732, 2199, 732, 2195, 724, 2183, 708, 2163, 684, 2135, 652, 2099, 612, 2055, 564, 2003, 508, 1943, 444, 1875, 2171, 292, 1715, 204, 1623, 108, 1523, 4, 1415, 2824, 1299, 2704, 1175, 2576, 1043, 2440, 903, 2296, 755, 2144, 599, 2419, 1816, 263, 1640, 83, 1456, 2827, 1264, 2631, 3491, 856, 2215, 640, 1995, 416, 1767, 184, 1531, 2876, 1287, 2628, 1035, 2372, 775, 2108, 507, 1836, 231, 1556, 2879, 1268, 2587, 972, 2287, 668, 1979, 356, 1663, 36, 1339, 2640, 1007, 2304, 667, 1960, 319, 1608, 2895, 1248, 2531, 880, 2159, 504, 1779, 120, 1391, 2660, 995, 2260, 591, 1852, 179, 1436, 2691, 1012, 2263, 580, 1827, 140, 1383, 2624, 931, 2168, 471, 1704, 3, 3691, 752, 1975, 264, 1483, 2700, 983, 2196, 475, 1684, 2891, 1164, 2367, 636, 1835, 100, 1295, 2488, 747, 1936, 191, 1376, 2559, 808, 1987, 232, 1407, 2580, 819, 1988, 223, 1388, 2551, 780, 1939, 164, 1319, 2472, 691, 1840, 55, 1200, 2343, 552, 1691, 2828, 1031, 2164, 363, 1492, 2619, 812, 1935, 124, 1243, 2360, 543, 1656, 2767, 944, 2051, 224, 1327, 2428, 595, 1692, 2787, 948, 2039, 196, 1283, 2368, 519, 1600, 2679, 824, 1899, 40, 1111, 2180, 315, 1380, 2443, 572, 1631, 2688, 811, 1864, 2915, 1032, 2079, 192, 1235, 2276, 383, 1420, 2455, 556, 1587, 2616, 711, 1736, 2759, 848, 1867, 2884, 967, 1980, 59, 1068, 2075, 1299, 2152, 219, 1216, 2211, 272, 1263, 2252, 307, 1292, 2599, 1303, 2280, 323, 1296, 2267, 304, 1271, 2236, 267, 1228, 2187, 212, 1167, 2120, 139, 1088, 2035, 48, 991, 1932, 2871, 876, 1811, 3487, 1672, 2599, 592, 1515, 2436, 423, 1340, 2255, 236, 1147, 2056, 31, 936, 1839, 2740, 707, 1604, 2499, 460, 1351, 2240, 195, 1080, 1963, 2844, 791, 1668, 2543, 484, 1355, 2224, 159, 1024, 1887, 2748, 675, 1532, 2387, 308, 1159, 2008, 2855, 768, 1611, 2452, 359, 1196, 2031, 2864, 2355, 2419, 312, 1135, 1956, 3435, 1475, 2288, 167, 976, 1783, 2588, 459, 1260, 2059, 2856, 719, 1512, 2303, 160, 947, 1732, 2515, 364, 1143, 1920, 2695, 536, 1307, 2076, 2843, 676, 1439, 2200, 27, 784, 1539, 2292, 111, 860, 1607, 2352, 1067, 1643, 2380, 183, 916, 1647, 2376, 171, 896, 1619, 2340, 127, 844, 1559, 2272, 51, 760, 1467, 2172, 2875, 644, 1343, 2040, 2735, 496, 1187, 1876, 2563, 316, 999, 1680, 2359, 104, 779, 1452, 2123, 2792, 527, 3047, 2516, 243, 900, 1555, 2208, 2859, 576, 1223, 1868, 2511, 220, 859, 1496, 2131, 2764, 463, 1092, 1719, 2344, 35, 656, 1275, 1892, 2507, 188, 799, 1408, 2015, 2620, 291, 892, 1491, 2088, 2683, 344, 935, 1524, 2111, 2696, 347, 928, 1507, 2084, 2659, 300, 871, 1440, 2007, 2572, 203, 764, 1323, 1880, 2435, 56, 607, 1156, 1703, 2248, 2791, 400, 939, 1476, 2011, 2544, 143, 672, 1199, 1724, 2247, 2768, 355, 872, 1387, 1900, 2411, 2920, 495, 1000, 1503, 2004, 2503, 68, 563, 1056, 1547, 2036, 2523, 76, 559, 1040, 1519, 1996, 2471, 12, 483, 952, 1419, 1884, 2347, 2808, 335, 792, 1247, 1700, 2151, 2600, 115, 560, 1003, 1444, 1883, 2320, 2755, 256, 687, 1116, 1543, 1968, 2391, 2812, 299, 716, 1131, 1544, 1955, 2364, 2771, 244, 647, 1048, 1447, 1844, 2239, 2632, 91, 480, 867, 1252, 1635, 2016, 2395, 2772, 215, 588, 959, 1328, 1695, 2060, 2423, 2784, 211, 568, 923, 1276, 1627, 1976, 2323, 2668, 79, 420, 759, 1096, 1431, 1764, 2095, 2424, 2751, 144, 467, 788, 1107, 1424, 1739, 2052, 2363, 2672, 47, 352, 655, 956, 1255, 1552, 1847, 2140, 2431, 2720, 75, 360, 643, 924, 1203, 1480, 1755, 2028, 2299, 2568, 2835, 168, 431, 692, 951, 1208, 1463, 1716, 1967, 2216, 2463, 2708, 19, 260, 499, 736, 971, 1204, 1435, 1664, 1891, 2116, 2339, 2560, 2779, 64, 279, 1195, 912, 3970, 1728, 1927, 2124, 2319, 2512, 5595, 147, 1543, 875, 1052, 1227, 1400, 1571, 1740, 1907, 2072, 2235, 2396, 2555, 2712, 2867, 88, 239, 388, 535, 680, 823, 964, 1103, 1240, 1375, 1508, 1639, 1768, 1895, 2020, 2143, 2264, 2383, 2500, 2615, 2728, 2839, 16, 123, 228, 331, 432, 531, 628, 723, 816, 907, 996, 1083, 1168, 1251, 1332, 1411, 1488, 1563, 1636, 1707, 1776, 1843, 1908, 1971, 2032, 2091, 2148, 2203, 2256, 2307, 2356, 2403, 2448, 2491, 2532, 2571, 2608, 2643, 2676, 2707, 2736, 2763, 2788, 2811, 2832, 2851, 2868, 2883, 2896, 2907, 2916, 5851, 2931, 2932, 2931, 2928, 2923, 2916, 2907, 2896, 2883, 2868, 5683, 2811, 2788, 2763, 2736, 2707, 2676, 2643, 5179, 2532, 2491, 2448, 2403, 2356, 2307, 2256, 2203, 2148, 2091, 2032, 1971, 1908, 1843, 1776, 1707, 1636, 1563, 1488, 1411, 1332, 1251, 1168, 1083, 996, 907, 816, 723, 628, 531, 432, 331, 228, 123, 16, 2839, 2728, 2615, 2500, 2383, 2264, 2143, 2020, 1895, 1768, 1639, 1508, 1375, 1240, 1103, 964, 823, 680, 535, 388, 239, 88, 2867, 2712, 2555, 2396, 2235, 2072, 1907, 1740, 1571, 1400, 1227, 1052, 875, 696, 515, 332, 147, 2892, 2703, 2512, 2319, 2124, 1927, 1728, 1527, 1324, 1119, 912, 703, 492, 279, 64, 2779, 2560, 2339, 2116, 1891, 1664, 1435, 1204, 971, 736, 499, 260, 19, 2708, 2463, 2216, 1967, 1716, 1463, 1208, 951, 692, 431, 168, 2835, 2568, 2299, 2028, 1755, 1480, 1203, 924, 643, 360, 75, 2720, 2431, 2140, 1847, 1552, 1255, 956, 655, 352, 47, 2672, 2363, 2052, 1739, 1424, 1107, 788, 611, 2751, 6283, 1431, 1096, 759, 420, 79, 2668, 2323, 1976, 1627, 1276, 923, 568, 211, 2784, 2423, 2060, 1695, 1328, 959, 588, 215, 2772, 2395, 2016, 1635, 1252, 867, 480, 91, 2632, 2239, 1844, 1447, 1048, 647, 244, 2771, 2364, 1955, 1544, 1131, 716, 299, 2812, 2391, 1968, 1543, 1116, 687, 256, 2755, 2320, 1883, 1444, 1003, 560, 115, 2600, 2151, 1700, 1247, 792, 335, 2808, 2347, 1884, 1419, 952, 483, 12, 2471, 1996, 1519, 1040, 559, 76, 2523, 2036, 1547, 1056, 563, 68, 2503, 2004, 1503, 1000, 495, 2920, 2411, 1900, 1387, 872, 355, 2768, 2247, 1724, 1199, 672, 143, 2544, 2011, 1476, 939, 400, 2791, 2248, 1703, 1156, 607, 56, 2435, 1880, 1323, 764, 203, 2572, 2007, 1440, 871, 300, 2659, 2084, 1507, 928, 347, 2696, 2111, 1524, 935, 344, 2683, 2088, 1491, 892, 291, 2620, 2015, 1408, 799, 188, 2507, 1892, 1275, 656, 35, 2344, 1719, 1092, 463, 2764, 2131, 1496, 859, 220, 2511, 1868, 1223, 576, 2859, 2208, 1555, 900, 243, 2516, 1855, 1192, 527, 2792, 2123, 1452, 779, 104, 2359, 1680, 999, 316, 2563, 1876, 1187, 496, 2735, 2040, 1343, 644, 2875, 2172, 1467, 760, 2323, 1559, 844, 127, 2340, 1619, 896, 171, 2376, 1647, 916, 183, 2380, 1643, 904, 163, 2352, 1607, 860, 111, 2292, 1539, 784, 27, 2200, 1439, 3519, 2076, 1307, 536, 2695, 1920, 1143, 364, 2515, 1732, 947, 160, 2303, 1512, 719, 2856, 2059, 1260, 459, 2588, 1783, 976, 167, 2288, 1475, 660, 2775, 1956, 1135, 312, 2419, 1592, 763, 2864, 2031, 1196, 359, 2452, 1611, 768, 2855, 2008, 1159, 308, 2387, 1532, 675, 2748, 1887, 1024, 159, 2224, 1355, 484, 2543, 1668, 791, 2844, 1963, 1080, 195, 2240, 1351, 460, 2499, 1604, 707, 2740, 1839, 936, 31, 2056, 1147, 236, 2255, 1340, 423, 2436, 1515, 592, 2599, 1672, 743, 2744, 1811, 876, 2871, 1932, 991, 48, 2035, 1088, 139, 2120, 1167, 212, 2187, 1228, 267, 2236, 1271, 304, 2267, 1296, 323, 2280, 1303, 324, 2275, 1292, 307, 2252, 1263, 272, 2211, 1216, 219, 3303, 148, 2075, 1068, 59, 1980, 967, 2884, 1867, 848, 2759, 1736, 711, 2616, 1587, 556, 2455, 1420, 383, 2276, 1235, 192, 2079, 1032, 2915, 1864, 811, 2688, 1631, 572, 2443, 1380, 315, 2180, 1111, 40, 1899, 824, 2679, 1600, 519, 2368, 1283, 196, 2039, 948, 2787, 1692, 595, 2428, 1327, 224, 2051, 944, 2767, 1656, 543, 2360, 1243, 124, 1935, 812, 2619, 1492, 363, 2164, 1031, 2828, 1691, 552, 2343, 1200, 55, 1840, 691, 2472, 1319, 164, 1939, 780, 2551, 1388, 223, 1988, 819, 2580, 1407, 232, 1987, 808, 2559, 1376, 191, 1936, 747, 2488, 1295, 100, 1835, 636, 2367, 1164, 2891, 1684, 475, 2196, 983, 2700, 1747, 1975, 752, 2459, 1232, 3, 1704, 471, 2168, 931, 4007, 140, 1827, 580, 2263, 1012, 2691, 1436, 179, 1852, 591, 2260, 995, 2660, 1391, 120, 1779, 504, 2159, 880, 2531, 1248, 2895, 1608, 319, 1960, 667, 2304, 1007, 2640, 1339]

    # 파싱
    for i in range(len(s)):
        cS = s[i]
        print(cS * c[i], end="")
    print()


# 피보나치 수열의 k번째 항 출력. k = [1, 10000]
def gen2():
    # DP를 이용한 피보나치 수열 계산
    MAX = 10000
    DP = [0 for _ in range(MAX)]
    DP[0] = 1
    DP[1] = 1
    print("1, 1, ", end="")
    for i in range(2, MAX):
        DP[i] = (DP[i-1] + DP[i-2]) % MOD
        print(DP[i], end=", ")
    print("0.")


# x & y를 비트로 나타내어 출력
def gen3():
    MAX = 1024
    for y in range(MAX):
        # 507 ~ 511행 반례 처리
        if y in {506, 507, 508, 509, 510}:
            exceptStr = ['##..##' + '.'*444 + '####..##..##.######..##...##..##.....####...####..###..####...##..##', '#...#' + '.'*444 + '##..##.###.##...##...####..##.##.....##..##.##..##..##.##..##..#...#', '####' + '.'*445 +'##..##.##.###...##..##..##.####.........##..##..##..##.##..##..####', '#.#' + '.'*446 +'##..##.##..##...##..######.##.##......##....##..##..##.##..##..#.#', '##' + '.'*448 + '####..##..##...##..##..##.##..##....######..####...##..####...##']
            print(exceptStr[y-506])
        # 비트를 이용한 시어핀스키 삼각형 표현
        else:
            curY = []
            for x in range(MAX - y):
                curY.append('#' if (y & x) == 0 else '.')
            print(''.join(curY))


# k가 소수이면 0, 합성수면 1로 표시하여 출력. k = [2, 399999]
def gen4():
    # 에라체 전처리
    MAX = 400000
    sieve = ['0'] * (MAX)
    cur = 2
    while cur**2 < MAX+2:
        if sieve[cur-2] == '0':
            for i in range(cur**2, MAX+2, cur):
                sieve[i-2] = '1'
        cur += 1
    
    # 3334번째 줄 반례 처리
    for i in range(266648, 266667):
        sieve[i] = strMOD[i-266648]

    # 문자열 파싱
    for y in range(0, MAX, 80):
        print(''.join(sieve[y:y+80]))


# gen5 서브 함수
def kthDay(K):
    one = ['', 'pierwszy', 'drugi', 'trzeci', 'czwarty', 'piaty', 'szosty', 'siodmy', 'osmy', 'dziewiaty', 'dziesiaty', 'jedenasty', 'dwunasty', 'trzynasty', 'czternasty', 'pietnasty', 'szesnasty', 'siedemnasty', 'osiemnasty', 'dziewietnasty', 'dwudziesty']
    tens = ['', '', 'dwudziesty', 'trzydziesty', 'czterdziesty', 'piecdziesiaty', 'szescdziesiaty', 'siedemdziesiaty', 'osiemdziesiaty', 'dziewiecdziesiaty']
    hundred = ['', 'setny', 'dwusetny', 'trzysetny']
    hundreds = ['', 'sto', 'dwiescie', 'trzysta']

    # 100, 200, 300 처리
    if K % 100 == 0:
        return hundred[K//100]

    result = []
    # 100 ~ 366까지의 수 처리
    if K//100 >= 1:
        result.append(hundreds[K//100])
        result.append(" ")
    
    # xx1 ~ x20까지의 수 처리 
    if 1 <= (K % 100) <= 20:
        result.append(one[K%100])
    # x20 ~ x90까지의 수 처리
    elif K % 10 == 0:
        result.append(tens[(K%100)//10])
    # x21 ~ x99까지의 수 처리
    else:
        result.append(tens[(K%100)//10])
        result.append(" ")
        result.append(one[K%10])

    return ''.join(result)


# 폴란드어로 2000년~2020년까지의 날짜에 관한 문장 출력
def gen5():
    # 1월 ~ 12월
    month = ['', 'stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca', 'lipca', 'sierpnia', 'wrzesnia', 'pazdziernika', 'listopada', 'grudnia']

    # 2000년 ~ 2020년
    year = ['dwutysiecznego', 'pierwszego', 'drugiego', 'trzeciego', 'czwartego', 'piatego', 'szostego', 'siodmego', 'osmego', 'dziewiatego', 'dziesiatego', 'jedenastego', 'dwunastego', 'trzynastego', 'czternastego', 'pietnastego', 'szesnastego', 'siedemnastego', 'osiemnastego', 'dziewietnastego', 'dwudziestego']

    leap = {2000, 2004, 2008, 2012, 2016, 2020}
    shortM = {4, 6, 9, 11}
    mm = None
    yyyy = None

    # 연 처리
    lineCount = 1
    for curY in range(2000, 2021):
        count = 1
        if curY == 2000:
            yyyy = 'dwutysiecznego'
        else:
            yyyy = 'dwa tysiace ' + year[curY-2000]

        # 월 처리
        for curM in range(1, 13):
            mm = month[curM]

            # 일 처리
            endDay = 31
            if curM == 2:
                if curY in leap:
                    endDay = 29
                else:
                    endDay = 28
            elif curM in shortM:
                endDay = 30
            for curD in range(1, endDay+1):
                firstW = kthDay(curD)
                firstW = chr(ord('A') + ord(firstW[:1]) - ord('a')) + firstW[1:]

                # 2648줄, 4901줄 반례 처리
                if lineCount == 2648:
                    print("Pierwszego kwietnia jest prima aprilis.")
                elif lineCount == 4901:
                    print("Pierwszego czerwca jest dzien dziecka.")
                else:
                    print(f"{firstW} {mm} to {kthDay(count)} dzien roku {yyyy}.")
                count += 1
                lineCount += 1
    print("Koniec.")


# gen6 서브 함수
def kthPermutation(N, K, alp, fact):
    K -= 1  # 0-based로 바꿔서
    letters = alp[:N]
    res = []
    for i in range(N, 0, -1):
        f = fact[i-1]
        idx = K // f
        res.append(letters.pop(idx))
        K %= f
    return ''.join(res)


# [a, ab, ba, abc, acb, bac, ...] 로 이루어진 수열에서 구간 [1, 20000] 내의 숫자를 네제곱한 항 전부 출력
def gen6():
    # 문자열의 개수 전처리
    fact = 1
    fact = [1 for _ in range(21)]       # fact[i] = i!의 값
    DP = [0 for _ in range(21)]     # DP[i] = 길이가 i 이하인 문자열의 개수
    alp = [chr(ord('a')+i) for i in range(26)]
    DP[1] = 1
    fact[1] = 1
    for i in range(2, 21):
        fact[i] = i * fact[i-1]
        DP[i] = DP[i-1] + fact[i]

    # 숫자 처리
    beforeSize = 1
    for i in range(1, 20001):
        curNum = i**4

        # 10000번째 줄 반례 처리
        if i == 10000:
            print(f'T[{curNum}]="{MOD}"')
            continue

        for size in range(beforeSize, 21):
            # num번째 문자열이 길이가 size인 문자열인지 체크
            if DP[size-1] < curNum <= DP[size]:
                p = curNum - DP[size-1]
                print(f'T[{curNum}]="{kthPermutation(size, p, alp, fact)}"')
                beforeSize = size


# 2^k를 3진법으로 표기하고 뒤집은 뒤 아스키 아트로 출력. k = [1, 170]
def gen7():
    WIDTH_MAX = 1000
    EXP_MAX = 171

    # pattern[i] = (0 = zero, 1 = one, 2 = two, 3 = comma, 4 = dot, 9 = nine)
    pattern = [['.####..', '##..##.', '##..##.', '##..##.', '.####..'], ['###.', '.##.', '.##.', '.##.', '.##.'], ['.####..', '##..##.', '...##..', '.##....', '######.'], ['......', '......', '......', '##....', '.#....'], ['....', '....', '....', '##..', '##..'], [], [], [], [], ['.####..', '##..##.', '.#####.', '....##.', '.####..']]

    result = [[], [], [], [], []]
    for i in range(EXP_MAX):
        # 2^i를 3진법으로 변환 후 뒤집기
        curNum = 2**i
        digit = []
        while curNum > 0:
            digit.append(str(curNum%3))
            curNum //= 3

        # 숫자 패턴 추가
        temp = [[], [], [], [], []]
        for curDigit in digit:
            for y in range(5):
                temp[y].extend(pattern[int(curDigit)][y])

        # 콤마 패턴 추가
        for y in range(5):
            temp[y].extend(pattern[3][y])

        # WIDTH_MAX 초과 시 result 출력 후 초기화
        if len(result[0]) + len(temp[0]) > WIDTH_MAX:
            # .으로 남은 공간 채우고 출력
            addSize = WIDTH_MAX - len(result[0])
            for y in range(5):
                result[y].extend('.' * (addSize))
                print(''.join(result[y]))
            print('.' * 1000)
            result = [[], [], [], [], []]

        for y in range(5):
            result[y].extend(temp[y])

    # 463~468줄 처리
    for curDigit in [0, 4]:
        for y in range(5):
            result[y].extend(pattern[curDigit][y])
    addSize = WIDTH_MAX-len(result[0])

    for y in range(5):
        result[y].extend('.' * (addSize))
        print(''.join(result[y]))
    print('.' * 1000)

    # 469~492줄 처리
    exceptPattern = ['01020102001020021020001020010200120000120001200102010200120120012001200102012001020102012001020102010102010201200120012012001220100200012002010201020102010200', '120012012001200120012001200120012001200120012012001201002000102001201200020020010020102001200001020102000120002010200102020000102001202002102001200202010201', '0201020010020201020201020200120010001200201200102012001200120102012002100002010200010200012022020012020102020102020102010909909990999909999902010200120012', '0012010201020102012001201201020120102012002001020012001200120012000120012001200210200120000120012001201200120102001001001001010100101000020102010200102001020001']
    for curLine in range(4):
        print('.' * 1000)
        result = [[], [], [], [], []]
        # 전처리한 숫자에 해당하는 패턴 추가
        for curDigit in exceptPattern[curLine]:
            for y in range(5):
                result[y].extend(pattern[int(curDigit)][y])

        # .으로 남은 공간 채우고 출력
        addSize = WIDTH_MAX - len(result[0])
        for y in range(5):
            result[y].extend('.' * (addSize))
            print(''.join(result[y]))


# 8방향 이동을 숫자 [0, 7]로 표기, 이동 2번에 해당하는 숫자를 십의자리, 일의자리에 표기. 그 후 아스키코드 45+k에 해당하는 문자로 인코딩. 출력할 때는 역과정 진행. k = [0, 77]
def gen8():
    move = "PZeooyzz-s-7-8.88C9CCCCDDDDNNNYOXYYYYYcZZZcdddeeeeoeooooyoypppyzzzzssss4--4---7-.-....7888889999BC9CCCCCCCCMCMDDDDMNMNNNONXXXXYOYXYYNOOYZdddncYYYOYYYcdnoooonddYcccdeoyppyyoodnednoopzzz4szoooooooyzs4-----4zzyzpzs--..778--4-ssss--.78999988-.--.-.889CCCDCC9B88888BCCCMMNMNDCCC9C9C9CDCNNNXYOONNMMDCMDMNNYYYYZYYYYXXXNONOOYOcYdZddcdYZYXYYYYYYZZddeeoennnddccccdddeooooyoyopeonneeeeenooyppzzzzzpoyoooopooypzzss4--s-sszzzzpzzzss--.-.-77-7--s4-ss4-4--.-8.888898777-7-.-....88C9C9CCC9C998B888898C9CCDCMDDDDCMCCCCC9C9CCCCCDCNNNNNXONNNMMMDDCMMNDNOOXYYYYYXYYYXXXXNXNXOOOYOYYcZYdZZccccYcYYYYXYYYYZYZZZdddnnnneedddcdZZZZdZdeeeoeoooyooooooennnnnnnnoeonpooyyyzpyzyyyyyooyoooopooyyyzzzssss44-sz4zzzzyzzzzzs4-------7--7----s-s4-ss4-4----7-77878888.78-77-7-.-.-7..7888BBC9BCBC9BBBB888898898BC9CCCCCCMCMDCDCCMCC9CC9CBCC9CCCCMCMMNDNNNNNNNNMMMMMDCMMDDMNMNNXXYOYOYXYYXYXXYONXONNXONXXYOYYYYYYcZYccZZYcZYYYYYYYYYYYYYYYYcZZZZdddddneddddddZccccdZcddddnnoeonooooonoooeoeenneeeeeeenoeoooopoppoyyzppppoypooyoooooyoooyoyyyzpzzzsz444ssz4zzzzzyzpzzzzzz4-s-4--------------s-s4-s44-s4-4------7.-78..78.78....-7-7-.--7-7.-778.8888BBBBC9999998B88888888B8BBBBCBCCCCCCCMCCDCCCCCCCCCBCC9C9C9CCBCCCMCDCMMMMNMNNNDNMNMMMMMDDCMDCMMDDMMNNNNONXYOXYOXYOXYOOOONXONNXNXNXXXXXYXYYYYYYYcYZYcYcYcYYcYYYYYYYOYYYYYYYYYYZYZZZZcdcddddddddddZccdZZZZZZZcdcdddednoenoeonooeononoennnnnnneednnnoenonooooopooypoyppoyypopopoooyooooooooyoopoyppppyzzzzzzszszz4zzzzzpyzpzpzpzzzzsssss-s-s---4-----s--s-s4-s444-ss4-s4-4------.-.-7...........-77-7-7-.--.--7-7-7....7888888BB998BB98B8B888888888888B9999BC9CCBCCCCCCCCMCCC9CCCC9C9C9C9C9C9C9CCCCCCCCDCMDDCNDDMMNMNDDMMMMMMDDCMCMDCMDCMMMMMNMNNNNONXXXXXYOOOOOOOONXNXNONNONNXONXXXXYXYXYYYYYYYYcYYYcYYZYYYYYYYYYXYYYXYYYXYYYYYYZYYcZYccccdZdcddcddcdcdZcccccccccZZZZccdcdddddneeennoenoenoenoennnnnneednednneeeeenoeonooooooopooyoyoyoyoyoyooyoooooooooooooopooopopoyppppyzpzzzzzzzzzzzzzpzpyzppyzpyzpzzzzzzsssss4-s4--s-4--s-4-4-s4-s44444-sssss4-s4-4---------7-.-7.-7..-77.-7.-7-.--7---7--.--.--7-77....787888888B8B988B88B888887887888888898BBBC9BCBCC9CCCBCCCCCC9CCBCC9C9C9BC9BC9C9BCC9CC9CCCCCMCCMDCMDDDCMNDDDDDDDDCMMDCMDCMCMCMCMDCDDCMMMMMNDNNNNNNONXOONXXXOONXONONNONNNNNNXNNXONXXXXYOXYXYYXYYYYYYYYYYYYcYYYYOYYYYXYYXYYXYYOYYXYYYYYYYYYcYZYZZYccccdZcdZcdZcdZcccccccccZZYccZZZZZZZZcdZddddddneeeeeeeeennnoeeeednnednedndnednednnnnoenoeonooooooooooyoopoooyoopooooooooooooooooeooooooyoooyoyoypppppyzpyzzpzzzpzzpzyzpyzppyyyzpppyyzpzpzzzzzzsz4444-ss4-s4-4-s4-s4-s4444444444444444444-s4-4--4-------7--7-.-.-.-7-7-7-7-.--.----7-----.----7--7-7.-7....78.8.88888888888888888788.8.788.88888888B9999BBC9C9BCC9CBCCBCC9CBCBCBC9BC9BC99BC99BC9BCBCBCCCBCCCCDCCCMCMCMDCMDDCMMDDCMMDCMDCMCMCMCDCCMCDCDCDCDCMDCMMMMNDMNNNNNNNNNXNXNXONONNXNNNNNNNNNNNNNNXNONONXXXXYOOYOYOYXYYYXYYYYYYXYYYYYXYYYOYYOYOYXYXYXYXYYOYYOYYYYYYYYYZYYcYcZZYccccccccccdZZZZZZZYccZZYcZYcZYcZZYccZZZZZZcdZddddddddneednneeeednnnednndndndndeddndndnednnnnnnoenonoonoooooooooooooooopooooooooonoooooeooonooooonoooopooooyopoypoyyppyyyzpyzpzpyzpzpyyzppyyyyyyyyyyyyyyyzppyzyzzzzzzzz4sssssssss444-ss4444-sssz444ssz44ssz44sssss44-s4-4--s-----------.---7--7--7--7---7-------7-------------7--.-.-.-7..-778..78788788878888.88.8.8.78.78.78.7878788888888B99999999BC9BC9BCBCBC9C9BC9BC99BBC999BBBBBC999BC9BC9C9C9CCCBCCCCDCCCDCCMCDCDCMCMDCMCMDCDCDCCMCDCCDCCCMCCDCCDCCMCDCDCMDDCMMMNDDMNNDNNNNNNNNNNONNNNNNNNNNNNNNDNNMNNNNNNNNXNXXOOOOOXYOXYOYOYXYYOYYOYYOYYOYYOYXYXYXYOYOXYOYOXYOYOYOYOYXYYYYOYYYZYYYYcYZYZYcZYcZZYcccZZZYccZZYcZZYZYcZYZYcYcZYZYcYcZZYccZZZZccdZdZddddddddndnedndnedndndndnddeddddeddddndededneeeeeeennonoeonoooeoooonoooooooooonoooooeoooeooeooeooeooeoooeoooooooooopoopopopoypppoyyyzppppyyyzppppyyyyyyppppoyypppoyyyppppppyzpyzpzzzzzzzz4sz4ssz4444444sssssz44sz44szsz4szsz4sz44sssz-sss4-s4-4--s---s---------7-----.---------.--4------------4------7----.--.-.-.-77......778.78.8.8.8.8.7878.778..778...7778..78.8.8.888888898B9998BC9999BBC99BC99BBC999BBBBBBBBBBBB999999999BBC99C9BCBCC9CCCC9CCCDCCCCCMCCMCCMCDCCMCDCCDCCDCCCMCCCCMCCCCCDCCCCDCCCDCCMCDCDCMDDCMMMMNDDMNMNNDNNNDNNNNNNNDNNNDNNDNDNDNDNDNMNNDNNNMNNNNONXNXXXOOOXXYOOXYOYOXYXYXYXYXYOYOYOXYOXYOXYOXXYOXXYOXXYOXYXYOYOYXYYXYYYYYYYYYYZYYYcYZYZYcYcZYcYcZYcZYcZYZYcYcYcYcYZYYcYcYZYYcYcYcYcZYcZZYcccccdZZdZdZdddddddddddnddnddeddddddndddddddddddddddededneednnoeeenoeoenooeonoonoooeoooeoonoonoonooeononooeoeoeoeoeonoonoooeoooooooooooyooyoyoyoypoyypppoyyyypppppoyyypppoyppoypoypoypoyypoyyppoyyyyyzppyzyzzyzzzzzzszsz4z4sz4ssz4sz4szsz4z4z4zszz4zszz4z4z4sz44ssssss44-s4-4-4--4---s---------s---------------s----4----s---4-----4--------7---.--.-.-7-77..-7777778...778.778..7778.....................778..8.78878888889898B98BBBB9999999999999999998BBB998B998BB998BBB99999BBC99BCBC9CBCCBCCCCCCCCCCCCCCCDCCCCCMCCCDCCCCCDCCCCCCCCCCCCCCCCDCCCCCCCCCDCCCDCCDCDCDCMDDCMMMMMMMNDMNDMNMNMNNDNDNMNMNMNMNDNDMNDMMNDMNDMNDNDNDNDNNNNNNNNNXNXOOONXXXYOOOXXYOOXYOXYOXXYOXXYOXXYOOOXXXXXYOOOOOXXXYOOXYOOXYXYXYXYYXYYYYYOYYYcYYYYYcYYZYYcYZYYcYcYcYZYZYYcYZYYZYYZYYYcYYZYYYcYYZYYZYYcYcYcYcZYccZZZZZZZZcdZcdcdddZdddddddddddddddZddddZddcddcdddZddddddddddededneeeeeeeeenoenoenonoeonononooeoeoeononoeoeoenoeoenoenoeoenoeoeoeoeooeooeoooooooooooopoooyopopopoypoypoypoypoyypoypoypoyoypopoyoyoypopopoyoypoypoyypppoyyzppyzpyzyzzzzzzzzzzzz4zszz4z4zszzszzz4zzzszzzzzz4zzz4zszszsz4sssssssss44-s4-4-4--s-4---s---s----s---4----s--4--4--4--4--s--s--s--s---s--------------7--7-.-.-.-7.-77...-777777777777777......-777..-77..-777...-77777778..78.8.87888888889898B98B98BB98BB998B998B98B98B8B9898B8B98B98B998BBB99BBBBC9BC9BCBCC9CC9CCCBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC9CCCCCCCC9CCCCCCCCCCCCCDCCCCMCCMCMCMCMDCMMDDDDDDDDDMMMNDMNDDMNDMNDMMNDMMNDDMMMNDDDDMMMNDDDMMNDMNDMNMNNMNNNNNNNONONOONXXOOOOOOOOOOOOOXXXXXYOOOOOOOOOOOONXXXXXXOOOOOOOOOOOOXXYOOXYOYOYOYOYYOYYYXYYYYYYYYYZYYYYYcYYYcYYYcYYZYYYZYYYYcYYYYZYYYYYYcYYYYYYcYYYYZYYYcYYcYZYZYZYcZYccZZZZZZZZccdZdZcdcddZddZddZddZddZdcdcddZdZcdcdcdcdcdcddZddcddddddddndnedneeednnoeeennoeenoenoenoenoeoenoenoennoennoennoeennoennoenoeeoenoeoeonooeooeooooooooooooooyoopoopooyoyoyoyoyoyoyoyoyoyoyoyopopooyopooyooyopopooyoyoyoyoypoyppoyyyyyyyyzpyzpzpzyzzzzyzzzzzzzzzzzz4zzzzzzzzzzzzzzzzzzzzzzzzzzzzszsz4sz444sss444-ss4-s4-4-4-4-4--s-4--s-4--s--s-s-4-4--s-s-s-s-s-s-s-s-s-s-4--s--s---s------------7---7-.-.-.-.-7-7..-7.-77..-7..-77..-7.-77.-7.-7.-7.-7-7.-77.-7..-77........778.78787888888888888B8989898B8B8B8B8B8B8988B88B8988988B8989898B98B99998BC999BBC9BC9C9C9CBCCBCCC9CCCBCCCCCC9CCCCCC9CCCCC9CCCC9CCC9CCC9CCC9CCC9CCCCBCCCCCCCCCCCCCCMCCCMCCMCMCMCMDCMMDCMMMMDDDDDDDDMMMMMMMNDDDDDDDDDDDDDDDDCMMMMMMMMMDDMMMMMMNDDMNDNDNDNNDNNNNNNNONONONXONXXONXXXOOONXXXOOONXXXOONXOONXOONXONXOONXXOONXXXXXXXXXYOOXYOXYOYOYOYXYYYOYYYYOYYYYYYYYYYYYYYZYYYYYYYYYYcYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYcYYYYYcYYZYYZYZYZYZYcZYccZZZZZZZZZZccdZcdZcdZcdZdZcdZdZcdZcdZcdZccdZccdZcdZZcdZcdcdZdZddZddddddddddndnedneednnnnnnnnnoeeennnoeeennoeeennnnoeeeeeennnnnnnnnoeeeeennoeenoeeoenoeoeonoonooonooooooooooooopooooyoooyooyooyooyooyooyooyoopooopoooyooopooopooopoopoopoopopooypopoypoyyppppozppppyzpyzpzpzpzzpzzyzzzzpzzzyzzzyzzzpzzpzzpzyzzyzzyzzzyzzzzzzzzzszszsz4ssz4444444-ss44-s4-s4-s4-4-s4-4-4-s-s4-s-s4-s-s4-s4-s4-s4-s4-s4-s-s4-4-s-s-4--s--4----s--------.----.---7-.--7-7-7-7-7.-.-7.-.-7-7.-.-7-7.-.-.-.-.-.-.-.-.-.-.-7-7.-7.-7.-77.........778.78.8788788888888888888B888B8889888888B888888888B8888988988B8B98B998BBBBBBBC99BBC9BCBC9C9C9CBCC9CC9CBCCC9CC9CC9CC9CC9CC9CBCCBCC9CBCC9CBCC9CBCCBCCBCCCBCCCCCCBCCCCDCCCCCCMCCDCCMCDCDCMCMDCMDDCMDDCMMMDDDCMMMDDDCMMDDDCMMDDCMMDCMMDDCMDDCMMDDDCMMMDDDDDDMMMNDMNDMNMNNMNNNNNNNNNNONNXNXONONXONONXONXONONXONONONXNXNXNXNXNXONONXONXONXXOOONXXXYOOOXXYOXYOXYXYYOYOYYOYYXYYYYYOYYYYYYYXYYYYYYYYYYYYOYYYYYYYYOYYYYYYOYYYYYYOYYYYYYYYYXYYYcYYYYYYYZYYYcYYcYZYZYcYcZYccZZYcccZZZZZZccccdZZZcccdZZcccdZZZcccccdZZZZZZZccccccdZZZccdZZcdZcdZdZddZddddddddddedededneednneeednnnnnnneeeeeeeeeednnnnneeednnneeeednnnneeeeeeeeeennnoeenoenoeoeoeonooeoonooooooeooooooooyooooooopooooopooooooyooooooyooooooooyoooooooooyooooooyooopoooyopooyopoyoypoyppoyypppppppyyyzpyzpyzpyzyzyzyzyzyzyzyzyzyzpzpyzyzpzpyzpzpyzyzyzyzyzzyzzzzzzzzzzzz4z4sz4ssz444sssss4444-ss44-ss44-s44-s44-s44-ss44-ss444-ss444-ss44-ss4-ss4-s4-s-s4-4-4--s--s---s--------------.----7--.--.--.--7-.--7-.--7-.--7-.--7--7-.--.--.--.--7--7-.--7-7-7-7-7.-.-77.-77........778..8.787878878888.888888888788888888.8888788888.888888888888888989898B98BB99999999BBBC9BBC9BCBC9BCBCBCBCBCBCBCBCBCBCBCBCBC9C9C9C9BCBC9C9C9BCBCBCBCBCBCBCC9CC9CCBCCCCBCCCCCCCCCCCDCCCCMCCDCCMCDCDCDCDCMCMDCMDCMDCMDCMDCMDCMDCDCMDCMDCMCMDCMCMDCMCMDCMDCMDCMDCMMDDCMMMMMMMMMMNDDMNDNDNDNMNNNNNNNNNNNNNNNONNONNXNNXNONNONNONNNXNNONNNONNNXNNXNONONONONXONXOOONXXXXXXYOOXXYOXYOYOXYXYXYYOYXYYXYYYOYYXYYYXYYYXYYYXYYYXYYYXYYYOYYXYYXYYYOYYXYYYOYYYOYYYXYYYYYYYXYYYYYcYYYYYYcYYZYYZYYcYcYcZYcYccZYcZZYcccZZZZZYccccccccZZZZZZZYcccccZZZZYccccZZZZYcccccccZZccccccdZZcdZcdZdZdcdddddddddddddndedndnednednedneednednnedneednednednednednednednednneednnneeeeeeennnoeenoenoeoeoeoeonooeoooeooooeooooooooooooooeoooooooooooooooooooooooooooooooooooeooooooooooyooooooopooooyooyopooyoyoypoypoyyppoyyyyyyyyyyyzppyyzppyyzpyzppyzppyzppyyzppyyzppyyzppyyzpyyzpyzpyzpyzyzzpzyzzzzzzzzzzzszz4szssz4ssz444sssssssssssssss444444444444444444444444444444444-sssss444-ss4-ss4-4-s-s-s-s-4--4----s------------------7----.----7---.---.----7---7----7----7----7----7---.---.---7--7-.--7-7-7.-.-7.-77...-7777778..778.78.787878788.8788.8788.88.8788.8.878788.8.8788.87888.888878888888B8989898B998BB99999999BBBC99BBC99BC9BC9BC9BC9BC9BBC9BC9BC9BC99BC9BC99BC9BC99BC9BC9BCBC9C9BCBCC9C9CC9CC9CCCC9CCCCCCCCCCCCCMCCCCMCCDCCDCCMCDCCMCMCDCDCDCDCDCDCDCCMCMCMCMCDCDCCMCMCDCDCCMCMCMCMCMCMCMDCDCMDCMDDCMDDDDCMMMMNDDDMMNDMNMNMNNDNNDNNNNNNDNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNONNNNNNXNNXNONONONXONXXOOOOOOOOOOOXXYOXYOOYOXYOYOYOYOYOYOYOYXYYOYXYXYYOYXYYOYOYXYYOYOYXYXYXYYOYOYXYXYYOYXYYOYYOYYXYYYXYYYYYYOYYYYYYYcYYYYYZYYYcYYcYZYZYYcZYZYcYcZYcZYccZYcZZYcZZYcZZYcZZYcZYccZYcZZYcZYcZYccZYcZZYcZZYccZZYccccccccccccdZZcdZcdZdZdcdddcdddddddddeddeddededdndndndndndndedededdndndeddndndededededndnednednneeeednnnoeeeennoenoenoeoeoeoeonooeooeoonooonooooeoooonooooonoooooeoooonoooooeooooeooonoooooeooooonooooooooooooooooooyooooyoopooyopopopoyoypoyppoyyppoyyyyyypppppppppyyyyyyyyyyyyyzppppppppppppppppppppppppppyyyyzppyzpyzpyzyzyzzpzzzzzzzzzzzzszz4z4sz4z44sz4ssz44ssz444ssz444ssz444ssz44ssz4ssz44ssz444sssz44444444444-sss44-s4-s4-4-s-s-4--s-4---4----4---------------------------7--------------.-------------------.--------7----7---7--7--7-7-7-7-7.-7.-7..-7777.....77778..778.778.78.7878.78.78.8.78.78.78.78.78.78.78.78.8.7878788.87888887888888B88B8B9898BB98BBB999999999999BBBBC9999BBBC999BBBC9999BBBBC9999BBBBC9999BBBC99BBC99BC99BC9BCBC9C9C9C9CBCCBCCCBCCCCCBCCCCCCCCCCMCCCCCCMCCCDCCCDCCCMCCDCCDCCCMCCMCCMCCDCCDCCCMCCDCCCMCCDCCCMCCMCCMCCMCDCCMCDCDCDCMCMDCMDCMDDCMMDDDDDDDDDDMMNDMMNMNDNDNDNDNMNNMNNNDNNNDNNNDNNNDNNNDNNMNNNDNNMNNNDNNNMNNNNNNNNNNNNNNNONNXNXONXONXXOOONXXXXYOOOOXXYOOXYOXXYOXYOYOXYOXYXYOYOXYOYOXYOYOXYOYOXYOYOXYOXYXYOXYOYOXYXYOYOYOYOYOYXYYOYXYYYOYYYOYYYYYYYYXZYYYYYYYYYcYYYcYYZYYcYZYYcYcYZYZYZYcYcYcZYZYcYcZYZYcYcZYZYZYcYcYcZYZYZYcYcYcZYZYcZYZYcZYcZYcZYccZZYcccccccccccdZZccdZcdcdcddZddcddddddddddddddddddeddddnddddnddddedddddeddddeddddnddeddndededednedneednnneeeeeennnoeennoenoeoenonoeoeononooeonoonooeooeooeooeooeooeonoonoonoonooeooeonoonoonoonoooeoonooonooooonooooooooooooooyoooopoooyooyopopopopopoypoypoypoyypoyyppoyypppoyypppoyypppoyypppoyyppoyypppoyypppoyyypppppoyyyyyyzppppyyzpyzpyzyzyzzpzzzzyzzzzzzzszzszz4zszsz4z4z4sz4z4sz4z4sz4z4sz4z4szsz4z4szsz4szsz4sz4sz44sz444ssssssssssss444-s4-s4-s4-4-4-4-4--s--s--4---4----4-------s--------4----------4---------s--------s---------------------------7---.---7--7-.-.--7.-.-7.-7.-77..-77777.......7777778....7778...7778...77778...77778....7778..778..78.78.78.8.8.88.888.888888888B8989898B98B98B998BBB9998BBBBB99999998BBBBBBB9999998BBBBB9999998BBBBBBBBBBBBC9999BBC99BC9BC9BC9C9BCC9C9CBCCBCCCBCCCCBCCCCCCCCCCCCCCCCCCCCDCCCCCCCDCCCCCCDCCCCCCMCCCCCCMCCCCCCDCCCCCCDCCCCCCMCCCCDCCCDCCCDCCDCCMCDCCMCMCMCMDCMDCMDDCMMDDDDDDDDDDDDDMMNDMMNDMNDMNMNDNDMNMNMNMNMNDNDNDNDNDNDMNMNMNDNDNDNDNDNDNMNMNNMNNNDNNNNNNNNNNNNNXNONONONXOONXOOONXXXXXXXXXYOOOOXXXYOOXXYOOXXYOXXYOOXYOOXXYOOXYOOXXYOOXXYOOXYOOXXYOXYOOXYOXYOXYOYOXYXYXYXYYOYXYYXYYYXYYYYYOYYYYYYYYYYYYZYYYYYYcYYYcYYZYYYcYYcYZYYZYYcYZYYcYZYYcYZYYcYYcYZYYcYZYYcYYcYZYYcYZYYcYcYZYZYZYZYZYZYcZYcYccZYcZZYccccZZZZZccccdZZcdZcdZdZdZdcddZddcddddZddddddZddddddddcdddddddcddddddddcddddddddddddddeddeddndndnednednneeednnnnnoeeeennoeenoenoenoenonoeoenononoeoeoeoeoeoeoeoeoeoeoeoenonononononononononononooeonooeonoonoooeooonooooooonoooooyoooooooyooopoopoopooyopopopopopoyoypoyoypoypoypoyoypoypoypoypoypoypoyoypoypoypoypoypoypoyppoyppoyypppoyyyyyyyyyyzpppyzpyzpyzyzyzzyzzzzpzzzzzzzzzzzz4zzszzz4zz4zszzszzszzszzszzszzszzszzszz4zszz4z4z4z4szsz4ssz4ssz44444444444-ss44-s4-s4-s4-4-4-4-4--s-4--s--s--s--4---s--4---4---4---s---s---s--4---4---4---s---s---4-----s------4------------.------7---7--7--7-7-.-.-7-7.-7.-7.-7..-77..-777....-77777.......-7777777......-777777..........-778.......7778..78.78.7878788.887888888888888B8988B8B8B9898B98B98B98B998B98B998B98B998B98B998B98B998B98BB998BB9998BBBBBBBBBBBBC999BBC9BC9BC9BCBCBCBCBCC9CC9CC9CCC9CCCCBCCCCCCCBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC9CCCCCCCCCCCCCCCCCCCMCCCCCCCCCCMCCCCDCCCDCCDCCDCCMCMCMCMCMDCMDCMDCMMDDCMMMMMDDDDDMMMMMNDDDMMMNDDMNDDMMNDMMNDMMNDMMNDMMNDDMNDDMNDDMNDDMNDMNDMNDMNDNDNDNDNMNNMNNNNMNNNNNNNNXNNXNXNXNXONXOONXOOONXXXOOOOOOOOOOOOOOOOOOOOOOOOOXXXXXXXXXXXXXXXXYOOOOOOOOOOXXXXXYOOOXXYOOXXYOXYOXYOXYOYOXYYOYOYXYYOYYXYYYXYYYYYXYYYYYYYYYYYYYYYcYYYYYYZYYYYYcYYYYcYYYZYYYYcYYYcYYYZYYYYcYYYZYYYYcYYYcYYYZYYYZYYYcYYZYYZYYcYYcYcYZYZYZYZYcZYZYcZZYcZZYcccccZZZZccccdZZccdZcdZcdZdZcdcddZdZdZdcddZdcddZddZdcddZdcddZdcddZdcddcddcddcdddcddddddddddddddddndededednednednnneeeeeeeeeeeeennnoeennoeenoennoenoenoeenoenoenoenoenoenoeenoenoenoenoenoenoenoeoenoeoenononononooeonoonoonooooeooooonooooooooooyooooooyooopoooyoopooyooyopopooyopopopooyoyoyoyoyoyopopopopopooyoyoyoyoyoyopoyoyoyoyoypopoypoypoypoyppoyyppoyyyyyyyyyyzppyyzpyzpyzyzyzyzzpzzyzzzzzpzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzszzzzzzzz4zzzz4zz4zz4z4z4z4szsz44sz444sssssssss4444-s44-s4-ss-s4-s-s4-4-4-4-4-4-4--s-s-4-4--s-4-4--s-4--s-s-4--s-4-4--s-4--s-4--s-4--4--s--4---s---s----4------------------7----7---7--7-.--7-.-.-.-.-7-7.-7.-7.-7.-7.-7..-7.-77.-77.-7..-7..-7..-7..-7.-77..-7..-77..-77..-7777...........7778..78.78.7878788.887888888888888888B88B88B898988B8B8B898989898988B8B8B8B8B8B89898B8B8B9898B98B98B998BB9998BBBBBBBC9999BBC9BC99BCBC9BCBCBCBCC9CBCC9CC9CC9CCBCCCBCCCCBCCCCBCCCCBCCCCCBCCCCC9CCCCC9CCCCBCCCCCBCCCCCBCCCCCCC9CCCCCCCCCCCCCCCCCCCCCCCMCCCCDCCCDCCDCCMCDCCMCMCMDCDCMDCMDCMMDDCMMDDDCMMMMDDDDDDDDDDDDDDDDDDDDDDMMMMMMMMMMMMMMNDDDDDDDDDDDMMMMMNDDDDMMNDDMMNDMNDMNDNDNDNDNMNNNMNNNNNNNNNNNNXNONNXNXONONXONXONXONXXOONXOOONXXOONXXOOONXXOOONXXOONXXXOONXXXOOONXXXXOOOOOOOOOOOOOOOOOXXXYOOXYOOXYOXYXYOYOXYYOYOYXYYOYYXYYYOYYYYOYYYYYYYXYYYYYYYYYYYYYYYYYYZYYYYYYYYYYYYYYYZYYYYYYYYYYYYYYcYYYYYYYYYYYZYYYYYYYZYYYYYZYYYYZYYYcYYZYYcYYcYcYZYZYcYcZYcZYcZYcZZYcccZZZZZZZZZZZZcccdZZZcdZZcdZZcdZcdZcdZcdZdZcdZcdZcdZdZcdZcdZcdZdZcdZdZcdZdZdZdZdZdZdcdddZdddcddddddddddeddedededednedneednneednnnnnnnnnnnnnnnnoeeeeennnnoeeennnoeeeennnoeeennnoeeennnoeeennnoeennoeenoeenoenoenoenoeoeoenonooeonooeooeoonoooonoooooooooooooooooooooopoooooyooooyoooyoopoooyoopoopoooyooyooyoopoopoooyooyooyoopoopoopooyooyopooyopooyoyoyoyoyoypopoypoyppoyppoyyyyppppppppyyyzppyyzpyzpzpyzyzyzyzzpzyzzyzzzpzzyzzzyzzzyzzzyzzzyzzzyzzzyzzzzpzzzzzpzzzzzzzzzzzzzzzszzszszszszsz4ssz4sssz44444444444-sss44-s"

    grid = [['.' for _ in range(1000)] for _ in range(1000)]
    grid[500][500] = '#'
    grid[501][501] = '#'

    # 인코딩된 문자를 변환 후 이동 표시
    curX = 501
    curY = 501
    for i in range(15252):
        decode = ord(move[i]) - 45
        for j in [decode//10, decode%10]:
            curX += dx[j]
            curY += dy[j]
            grid[curY][curX] = '#'

    # 출력
    for i in grid:
        print(''.join(i))


# 선분의 시작점, 방향, 길이를 전처리하여 출력
def gen9():
    MAX = 1003
    grid = [['.' for _ in range(MAX)] for _ in range(MAX)]
    lines = [[1, 812, 5, 131], [2, 544, 2, 443], [13, 488, 2, 48], [15, 636, 4, 875], [21, 110, 5, 55], [22, 506, 4, 764], [24, 146, 4, 845], [27, 388, 2, 117], [28, 475, 5, 44], [38, 296, 4, 208], [39, 840, 4, 612], [42, 76, 4, 330], [42, 408, 4, 153], [46, 258, 4, 65], [47, 790, 2, 213], [48, 0, 2, 20], [50, 872, 5, 529], [54, 398, 4, 62], [55, 703, 2, 231], [59, 233, 5, 234], [62, 96, 4, 175], [63, 854, 2, 149], [64, 0, 2, 297], [64, 657, 5, 298], [65, 428, 4, 751], [66, 246, 4, 279], [68, 637, 3, 9], [69, 824, 4, 303], [70, 50, 3, 832], [72, 661, 5, 258], [77, 856, 4, 723], [80, 70, 2, 864], [83, 124, 4, 506], [90, 396, 4, 43], [91, 612, 4, 818], [92, 643, 3, 257], [98, 84, 3, 371], [99, 511, 6, 6], [99, 831, 5, 193], [103, 736, 4, 124], [106, 202, 4, 44], [106, 590, 3, 413], [108, 827, 3, 176], [109, 670, 4, 93], [112, 674, 4, 658], [121, 898, 4, 419], [124, 678, 2, 325], [125, 0, 2, 913], [128, 454, 2, 7], [129, 484, 4, 708], [130, 477, 5, 160], [131, 707, 3, 95], [135, 680, 2, 131], [136, 734, 4, 263], [141, 872, 2, 117], [143, 151, 5, 152], [143, 362, 2, 198], [149, 816, 4, 502], [150, 620, 3, 203], [154, 916, 3, 87], [157, 429, 2, 510], [158, 198, 4, 428], [163, 328, 4, 264], [164, 207, 5, 30], [167, 611, 2, 311], [173, 978, 3, 25], [175, 978, 2, 25], [176, 0, 2, 315], [177, 696, 4, 302], [179, 956, 4, 759], [180, 122, 4, 791], [182, 347, 2, 271], [188, 374, 2, 203], [191, 373, 5, 4], [194, 391, 5, 217], [195, 24, 4, 550], [199, 592, 5, 305], [201, 470, 3, 468], [202, 0, 3, 334], [205, 767, 2, 137], [207, 564, 4, 764], [208, 236, 4, 487], [212, 676, 3, 30], [215, 895, 5, 74], [218, 780, 4, 426], [226, 55, 5, 56], [227, 302, 2, 236], [229, 348, 4, 294], [230, 556, 3, 447], [237, 412, 5, 413], [238, 84, 2, 164], [242, 238, 3, 186], [245, 0, 3, 46], [253, 303, 5, 304], [256, 756, 4, 323], [257, 724, 2, 279], [258, 0, 2, 222], [259, 853, 5, 250], [260, 215, 3, 629], [260, 964, 5, 307], [261, 356, 2, 602], [264, 760, 4, 57], [268, 874, 2, 40], [278, 345, 2, 109], [282, 570, 4, 514], [283, 454, 4, 627], [283, 553, 2, 346], [284, 1002, 5, 295], [288, 0, 3, 408], [289, 401, 3, 415], [291, 849, 5, 585], [295, 1002, 5, 245], [297, 183, 5, 112], [297, 192, 4, 187], [297, 1002, 5, 163], [298, 670, 2, 333], [299, 0, 2, 183], [301, 338, 3, 148], [302, 274, 4, 570], [305, 292, 3, 568], [306, 312, 3, 127], [306, 580, 3, 150], [306, 811, 5, 120], [307, 102, 4, 457], [312, 326, 4, 385], [314, 197, 2, 3], [320, 739, 5, 136], [321, 332, 4, 557], [324, 715, 5, 551], [324, 887, 2, 116], [325, 0, 2, 340], [325, 450, 4, 622], [325, 677, 5, 226], [345, 810, 4, 563], [352, 839, 3, 129], [359, 586, 4, 23], [362, 943, 2, 60], [363, 0, 2, 755], [369, 501, 2, 163], [369, 839, 5, 458], [376, 314, 4, 118], [381, 772, 5, 183], [384, 706, 2, 102], [385, 26, 4, 177], [390, 941, 5, 451], [396, 724, 3, 279], [397, 572, 3, 301], [400, 746, 4, 188], [406, 632, 4, 225], [413, 571, 5, 341], [415, 99, 5, 100], [417, 217, 5, 73], [420, 966, 2, 37], [421, 0, 2, 205], [421, 505, 5, 332], [423, 604, 4, 438], [426, 643, 5, 323], [427, 800, 4, 203], [429, 208, 3, 454], [434, 944, 4, 48], [436, 284, 2, 301], [438, 384, 5, 265], [443, 322, 5, 79], [453, 302, 3, 183], [456, 448, 3, 199], [466, 686, 2, 317], [467, 0, 2, 95], [468, 675, 2, 55], [470, 958, 4, 57], [473, 778, 2, 81], [474, 261, 2, 127], [474, 867, 3, 136], [480, 719, 5, 74], [486, 50, 2, 437], [491, 119, 5, 114], [502, 480, 5, 57], [512, 995, 5, 73], [513, 478, 2, 12], [517, 455, 3, 127], [517, 1002, 5, 49], [518, 538, 4, 466], [519, 166, 4, 368], [523, 0, 3, 108], [524, 562, 3, 291], [525, 830, 2, 173], [526, 0, 2, 214], [526, 878, 2, 125], [527, 0, 2, 462], [529, 515, 3, 143], [542, 590, 5, 89], [544, 376, 4, 229], [552, 474, 4, 397], [555, 16, 3, 171], [559, 1002, 5, 152], [561, 69, 2, 285], [564, 224, 3, 142], [564, 444, 3, 216], [569, 881, 5, 297], [574, 964, 4, 33], [576, 278, 2, 457], [577, 514, 2, 29], [577, 618, 4, 371], [579, 858, 3, 145], [584, 606, 4, 183], [587, 860, 4, 34], [592, 607, 2, 396], [593, 0, 2, 36], [606, 244, 2, 652], [614, 0, 3, 90], [619, 446, 2, 264], [620, 832, 4, 259], [621, 410, 2, 231], [622, 490, 3, 24], [624, 852, 3, 151], [627, 348, 3, 160], [651, 987, 2, 16], [652, 0, 2, 518], [652, 1002, 5, 109], [654, 266, 4, 273], [654, 483, 3, 19], [657, 502, 3, 200], [679, 0, 3, 175], [680, 0, 2, 30], [681, 0, 3, 101], [684, 488, 2, 59], [691, 349, 3, 80], [696, 393, 5, 3], [696, 764, 4, 196], [698, 402, 4, 13], [698, 523, 2, 131], [710, 610, 4, 39], [711, 377, 5, 94], [717, 222, 2, 370], [718, 596, 5, 218], [728, 0, 3, 181], [736, 607, 3, 231], [742, 294, 3, 137], [746, 38, 2, 324], [750, 544, 3, 158], [751, 552, 4, 136], [753, 444, 2, 559], [754, 0, 2, 84], [755, 180, 4, 67], [772, 355, 5, 133], [772, 969, 5, 223], [779, 0, 3, 116], [782, 980, 3, 23], [783, 793, 3, 55], [794, 990, 4, 43], [809, 0, 3, 175], [812, 76, 3, 55], [832, 775, 2, 147], [833, 898, 4, 140], [834, 204, 2, 7], [836, 327, 3, 71], [856, 360, 2, 466], [857, 523, 2, 16], [858, 295, 2, 171], [890, 529, 5, 95], [893, 103, 3, 87], [894, 84, 3, 52], [901, 566, 3, 19], [917, 688, 2, 190], [919, 674, 5, 23], [921, 934, 2, 69], [922, 0, 2, 300], [926, 463, 5, 59], [935, 371, 2, 279], [938, 625, 3, 59], [942, 174, 3, 58], [951, 403, 3, 9], [957, 524, 4, 19], [960, 601, 2, 245], [967, 903, 5, 11], [992, 197, 2, 747], [994, 583, 2, 420], [995, 0, 2, 46]]

    for i in range(len(lines)):
        curY, curX, way, lineSize = lines[i]

        grid[curY][curX] = '#'
        for _ in range(lineSize-1):
            curY += dy[way]
            curX += dx[way]
            grid[curY][curX] = '#'

    for i in grid:
        print(''.join(i))


# gen10에서 첫 번째 수열 출력
def gen10_1():
    MAX = 15
    gap = {1: "     ", 2: "      "}

    print('a_i = a_{i-1} . a_{i-2}\n\na_1 = 0\n\na_2 = 0 1\n')
    prev2 = [0]
    prev1 = [0, 1]
    for size in range(3, MAX+1):
        cur = prev1 + prev2
        if size < 9:
            print(f"a_{size} =", *cur)
            print()
        else:
            print(f"a_{size} =", *cur[:40])
            for i in range(1, len(cur)//40+1):
                print(f"{gap[len(str(size))]}", *cur[i*40:min((i+1)*40, len(cur))])
            print()
        prev2 = prev1
        prev1 = cur

    print()


# gen10_2 서브 함수1
def matrixMul(size, A, B):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] = (result[i][j] + A[i][k]*B[k][j]) % 2

    return result


# gen10_2 서브 함수2
def getPowerM(A, exp, size):
    R = [[0] * size for _ in range(size)]
    base = [i[:] for i in A]
    for y in range(size):
        for x in range(size):
            if y == x:
                R[y][x] = 1

    while exp:
        if exp & 1:
            R = matrixMul(size, R, base)

        base = matrixMul(size, base, base)
        exp >>= 1

    return R


# gen10에서 두 번째 수열 출력
def gen10_2():
    # a[19]까지 계산 
    prev2 = [0]
    prev1 = [0, 1]
    for _ in range(3, 20):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    pattern = cur

    MAX = 70
    print("(A_i)^n = B_i (mod 2)\n\nA_1 = 0   B_1 = 0\n")

    for size in range(2, MAX+1):
        curA = [pattern[size*i:size*(i+1)] for i in range(size)]
        curB = getPowerM(curA, MOD, size)

        if size < 10:
            for line in range(size):
                if line == size//2:
                    print(f"A_{size} =", *curA[line], f"  B_{size} =", *curB[line])
                else:
                    print("     ", *curA[line], "       ", *curB[line])
        else:
            for line in range(size):
                if line == size//2:
                    print(f"A_{size} =", *curA[line], f"  B_{size} =", *curB[line])
                else:
                    print("      ", *curA[line], "        ", *curB[line])
        print()


def main():
    N = int(input())
    if N == 0:
        gen0()
    elif N == 1:
        gen1()
    elif N == 1:
        gen1()
    elif N == 2:
        gen2()
    elif N == 3:
        gen3()
    elif N == 4:
        gen4()
    elif N == 5:
        gen5()
    elif N == 6:
        gen6()
    elif N == 7:
        gen7()
    elif N == 8:
        gen8()
    elif N == 9:
        gen9()
    elif N == 10:
        gen10_1()
        gen10_2()


main()
