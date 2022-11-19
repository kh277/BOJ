// 1. 문자열이 들어옴 -> char로 분해
// 2. 영어 글자를 전부 저장할 수 있는 크기 26의 배열 생성
// 3. char을 읽어 올 때마다 처음 들어온 값인지 확인
// 3-1. 처음 들어온 값일 경우 배열에 값을 증가시키고 다음 값 읽어옴
// 3-2. 이전에 들어온 값일 경우 바로 전 위치가 이전 값인지 확인
// 3-2-1. 바로 전 위치일 경우 배열에 값을 증가시키고 다음 값 읽어옴
// 3-2-2. 바로 전 위치가 아닐 경우 그룹 단어가 아님
// 4. 문자열의 모든 문자에 대해 검사를 끝낸 경우 count를 1 증가시킴

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int count = 0;
        for (int i = 0; i < N; i++)
        {
            boolean judge = true;
            // 1번
            String str = in.next();
            char[] strToChar = str.toCharArray();
            
            // 2번
            int[] num = new int[26];
            
            // 3번
            num[strToChar[0] - 'a']++;
            for (int j = 1; j < str.length(); j++)
            {
                // 3-1번
                if (num[strToChar[j]- 'a'] == 0)
                    num[strToChar[j] - 'a']++;
                // 3-2번
                else {
                    // 3-2-1번
                    if (strToChar[j-1] == strToChar[j])
                        num[strToChar[j] - 'a']++;
                    // 3-2-2번
                    else {
                        judge = false;
                        break;
                    }   
                }
            }
            // 4번
            if (judge == true)
                count++;
        }
        System.out.println(count);
    }
}