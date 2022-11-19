// 1. 괄호 문자열을 입력받는다.
// 2. 빈 스택을 만들고 문자열에서 한 글자씩 순서대로 가리킨다.
// 3-1. 여는 괄호가 나올 경우 스택에 집어넣는다.
// 3-2. 닫는 괄호가 나올 경우 스택이 비어있는지 확인한다.
// 3-2-1. 스택이 비어있을 경우 NO를 출력한다.
// 3-2-2. 스택에 비어있지 않는 경우 pop시켜준다.
// 4. 모든 괄호에 대해서 다 입력받고, 남은 괄호가 있을 경우 NO를 출력한다.

import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int T = in.nextInt();
        
        for (int i = 0; i < T; i++)
        {
            boolean judge = true;
            
            // 1번
            String PS = in.next();
            
            // 2번
            Stack<Character> stack = new Stack<>();
            for (int j = 0; j < PS.length(); j++) {
                char s = PS.charAt(j);
                // 3-1번
                if (s == '(')
                    stack.push(s);
                // 3-2번
                else
                {
                    // 3-2-1번
                    if (stack.empty()) {
                        judge = false;
                        break;
                    }
                    // 3-2-2번
                    else
                        stack.pop();
                }
            }
            // 4번
            if (!stack.empty())
                judge = false;
            System.out.println((judge) ? "YES" : "NO");
        }
    }
}