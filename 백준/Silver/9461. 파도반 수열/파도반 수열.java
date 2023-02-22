import java.util.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();
        BigInteger[] dp = new BigInteger[105];
        Arrays.fill(dp, BigInteger.valueOf(0));

        dp[0] = BigInteger.valueOf(-1);     // 미사용
        dp[1] = BigInteger.valueOf(1);
        dp[2] = BigInteger.valueOf(1);
        dp[3] = BigInteger.valueOf(1);
        dp[4] = BigInteger.valueOf(2);
        dp[5] = BigInteger.valueOf(2);

        for (int i = 0; i < T; i++) {
            int N = in.nextInt();
            if (dp[N] == BigInteger.valueOf(0)) {
                for (int j = 6; j <= N; j++) {
                    if (dp[j] != BigInteger.valueOf(0))
                        continue;
                    else
                        dp[j] = dp[j-1].add(dp[j-5]);    // 점화식
                }
            }
            System.out.println(dp[N]);
        }
    }
}