import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int count = 0;
        for (int i = 0; i < N; i++)
        {
            boolean judge = true;
            int num = in.nextInt();
            // num이 1일 때
            if (num == 1) {
                judge = false;
                continue;
            }
            
            // num이 1이 아닐 때
            label : while (num > 1)
            {
                for (int j = 2; j <= num; j++) {
                	if (j == num)
                        break label;
                    
                    if (num % j == 0)
                    {
                        judge = false;
                        break label;
                    }
                }
            }
            if (judge == true)
                count++;
        }
        System.out.println(count);
    }
}