import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt();
        int[] P = new int[N];
        int sum = 0;
        
        for (int i = 0; i < N; i++)
            P[i] = in.nextInt();
        
        Arrays.sort(P);
        
        for (int i = 0; i < N; i++)
            sum += P[i] * (N - i);
        
        System.out.println(sum);
    }
}