import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int[] dp = new int[3];    // N-1까지의 최소값들 저장
        int[] arr = new int[3];    // N번째 입력값들 저장

        // N이 1인 경우
        dp[0] = in.nextInt();
        dp[1] = in.nextInt();
        dp[2] = in.nextInt();

        // N이 2 이상인 경우
        for (int i = 1; i < N; i++) {
            arr[0] = in.nextInt();
            arr[1] = in.nextInt();
            arr[2] = in.nextInt();

            int a = min1(dp[1], dp[2]) + arr[0];
            int b = min1(dp[0], dp[2]) + arr[1];
            int c = min1(dp[0], dp[1]) + arr[2];

            dp[0] = a;
            dp[1] = b;
            dp[2] = c;
        }
        System.out.println(min2(dp[0], dp[1], dp[2]));
    }

    public static int min1(int a, int b) {
        if (a <= b)
            return a;
        else
            return b;
    }

    public static int min2(int a, int b, int c) {
        if (a <= b && a <= c)
            return a;
        else if (b <= a && b <= c)
            return b;
        else
            return c;
    }
}