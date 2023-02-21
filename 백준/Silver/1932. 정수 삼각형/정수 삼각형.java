import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[][] arr = new int[N][N];
        int[][] dp;
        dp = new int[N][N+3];    // dp를 0으로 초기화

        for(int i = 0; i < N; i++) {
            for(int j = 0; j <= i; j++) {
                arr[i][j] = in.nextInt();
                if (i == 0)    // 제일 윗층인 경우
                    dp[0][0] = arr[i][j];
                else if (j == 0)    // 좌측 끝인 경우
                    dp[i][j] = arr[i][j] + dp[i-1][j];
                else if (j == i)    // 우측 끝인 경우
                    dp[i][j] = arr[i][j] + dp[i-1][j-1];
                else    // 윗 값들 사이에 비교가 필요한 경우
                    dp[i][j] = arr[i][j] + bigNumber(dp[i-1][j-1], dp[i-1][j]);
            }
        }

        System.out.println(bigArrayNumber(dp[N-1]));

    }

    public static int bigNumber(int a, int b) {
        if (a >= b) return a;
        else return b;
    }

    public static int bigArrayNumber (int[] arr) {
        int big = 0;
        for (int i = 0; i < arr.length; i++) {
            if (big < arr[i])
                big = arr[i];
        }
        return big;
    }
}
/*
입력 배열 (arr)
7
3 8
8 1 0

총합 배열 (dp)
16을 결정할 때는 왼쪽 위와 오른쪽 위의 값을 비교하여 큰 값 저장
7
10 15
8 16 15
*/