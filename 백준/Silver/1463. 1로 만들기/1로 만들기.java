import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[] count = new int[1000005];
        count[0] = 0;    // 0은 미사용 인덱스
        count[1] = 0;    // 1은 0회 연산
        for (int i = 2; i <= N; i++)
        {
            if (i % 3 == 0) {
                // 2와 3 모두 나눠떨어지는 경우
                if (i % 2 == 0)
                    count[i] = min(count[i/3], count[i/2], count[i-1]) + 1;
                // 3으로 나눠떨어지고, 2로 나눠떨어지지 않는 경우
                else
                    count[i] = min(count[i/3], count[i-1]) + 1;
            }
            
            // 2로 나눠떨어지고, 3으로 나눠떨어지지 않는 경우
            else if (i % 2 == 0)
                count[i] = min(count[i/2], count[i-1]) + 1;
            
            // 2와 3 모두 나눠떨어지지 않는 경우
            else    
                count[i] = count[i-1] + 1;
        }
        System.out.println(count[N]);
    }
    
    public static int min (int a, int b) {
        if (a <= b)
            return a;
        else
            return b;
    }
    
    public static int min (int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= a && b <= c)
            return b;
        else
            return c;
    }
}