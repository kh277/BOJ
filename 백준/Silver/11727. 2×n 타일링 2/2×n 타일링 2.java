import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // 1 3 5 11 21 43 85 171 ...
        // f(1) = 1, f(2) = 3
        // n = k일 때, f(n) = f(n-1) + 2f(n-2)
        
        int N = in.nextInt();
        int[] dp = new int[1005];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 3;
        for (int i = 3; i <= N; i++)
            dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007;
        
        System.out.println(dp[N]);
        
    }
}
