import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        
        for (int i = 0; i < T; i++) {
            int N = in.nextInt();
            int M = in.nextInt();
            int sum = 1;
            
            // mCn = mCm-n이므로 계산 간략화
            if (M - N <= N)
                N = M - N;
            
            // mCn 계산
            for (int j = 1; j <= N; j++)
                sum = sum * (M - j + 1) / j;
            
            System.out.println(sum);
        }
    }
}