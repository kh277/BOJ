import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        int[] data = new int[15];
        Arrays.fill(data, -1);
        data[0] = 0;
        data[1] = 1;    // 1은 1 -> 1가지
        data[2] = 2;    // 2는 2, 1+1 -> 2가지
        data[3] = 4;    // 3은 3, 1+2, 2+1, 1+1+1 -> 4가지
        
        for (int i = 0; i < T; i++)
        {
            int N = in.nextInt();

            for (int j = 4; j <= N; j++)
            {
                if (data[j] == -1) {
                    // F(n)의 값은 1+F(n-1), 2+F(n-2), 3+F(n-3)
                    data[j] = data[j-1] + data[j-2] + data[j-3];
                }
                else
                    continue;
            }
            System.out.println(data[N]);
        }
    }
}