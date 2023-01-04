import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        int sum = 0;
        int K = in.nextInt();
        
        for (int i = 0; i < K; i++) {
            int N = in.nextInt();
            if (N == 0)
                stack.pop();
            else
                stack.push(N);  
        }
        
        for (int num : stack)
            sum += num;
        
        System.out.println(sum);
    }
}