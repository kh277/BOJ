import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int K = in.nextInt();
        int sum = 0;
        int[] arr = new int[N];

        for (int i = 0; i < N; i++)
            arr[i] = in.nextInt();

        for (int i = N-1; i >= 0 ; i--) {
            int result = K / arr[i];
            sum += result;
            K -= result * arr[i];
        }
        System.out.println(sum);
    }
}