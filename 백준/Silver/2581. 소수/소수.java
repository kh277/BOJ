import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int M = in.nextInt();
        int N = in.nextInt();
        // M이 N보다 클 경우 -1 출력
        if (M > N) {
            System.out.println("-1");
        }
        
        // 일반적인 경우
        else {
            // 소수의 배열을 arr에 저장함
            int[] arr = judge(M, N);
            
            // arr의 최소값, 총합
            int sum = 0;
            for (int num : arr) {
                sum += num; 
            }
            
            if (arr[0] == 0) {
            	System.out.println("-1");
            }
            else {
            	System.out.println(sum);
            	System.out.println(arr[0]);
            }
            
        }
    }
    
    public static int[] judge (int M, int N) {
        int[] odd = new int[N-M+1];
        int count = 0;
        // M 이상 N 이하의 자연수 중에서
        for (int i = M; i <= N; i++) {
        	int original = i;
            // 소수 판별
            label : while (i > 1)
            {
                for (int j = 2; j <= i; j++) {
                	if (j == original) {
                        odd[count] = original;
                        count++;
                        break label;
                    }
                    if (i % j == 0) {
                    	break label;
                    }
                }
            }
        }
        return odd;
    }
}