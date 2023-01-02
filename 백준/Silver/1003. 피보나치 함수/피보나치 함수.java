import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        int[] data = new int[45];
        Arrays.fill(data, -1);
        data[0] = 0;
        data[1] = 1;
        data[2] = 1;
        
        for (int i = 0; i < T; i++) {
            int N = in.nextInt();
            if (N == 0) {
                System.out.printf("1 0%n");
                continue;
            }
            else if (N >= 3) {
               for (int j = 3; j <= N; j++) {
                   if (data[j] == -1) {
                       data[j] = data[j-1] + data[j-2];
                   }
                   else
                       continue;
                } 
            }
            System.out.printf("%d %d%n", data[N-1], data[N]);
        }
    }
}