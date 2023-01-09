import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        
        int N = in.nextInt();
        int sum = 1;
        for (int i = 1; i <= N; i++)
            sum *= i;
        
        System.out.println(sum);
    }
}