// 초항의 경우 그 수만큼 push후 pop 1번 (ex : 4일때 - push*4, pop*1)
// 2~N번째 항의 경우 이전 항과 현재 항을 비교.
// 이전 항보다 현재 항이 작을 경우, pop을 하여 수가 일치하는지 확인.
// 이전 항보다 현재 항이 클 경우, 숫자가 맞을 때까지 push를 함.
// 위의 경우에서 한번이라도 일치하지 않을 경우 false.
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main (String[] args) {
        Scanner in = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        
        int N = in.nextInt();
        int[] ex = new int[N];
        
        for (int i = 0; i < N; i++)
            ex[i] = in.nextInt();
        
        int top = 0;
        boolean key = true;
        int front = 1;
        String text = "";
        // 수열의 초항, 1~ex[0]까지의 자연수 스택 삽입
        for (int i = 1; i <= ex[0]; i++) {
            stack.push(i);
            sb.append('+').append('\n');
            front++;
        }
        stack.pop();    // 수열의 초항 생성.
        sb.append('-').append('\n');
        
        // 수열의 2~N번째 항
        for (int i = 1; i < N; i++) {
            // 이전 수보다 현재 수가 더 작을 경우
            if (ex[i] < ex[i-1])
                // 스택에 저장된 수와 비교
                if (stack.peek() == ex[i]) {
                    sb.append('-').append('\n');
                    stack.pop();
                }
                else {
                    key = false;
                    break;
                }
                    
            // 이전 수보다 현재 수가 더 클 경우
            else if (ex[i] > ex[i-1]) {
                for (int j = front; j <= ex[i]; j++) {
                    stack.push(j);
                    sb.append('+').append('\n');
                    front++;
                }
                stack.pop();
                sb.append('-').append('\n');
            }
        }
        if (key == true) {
            System.out.println(sb);
        }
        else
            System.out.println("NO");
    }
}
