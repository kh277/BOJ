import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int N = in.nextInt();
        int[] example = new int[N];
        for (int i = 0; i < N; i++)
            example[i] = in.nextInt();
        
        // 정렬
        Arrays.sort(example);
        
        int M = in.nextInt();
        
        // 이진 탐색
        for (int i = 0; i < M; i++) {
            int A = in.nextInt();
            boolean result = binarySearch(0, N-1, A, example);
            if (result == true)
                System.out.println("1");
            else
                System.out.println("0");
        } 
    }
    
    // 이진 탐색 함수
    public static boolean binarySearch(int first, int last, int target, int[] example) {
        if (first > last)
            return false;
            
        int mid = (last + first) / 2;
            
        if (example[mid] > target)
            return binarySearch(first, mid-1, target, example);
        else if (example[mid] < target)
            return binarySearch(mid+1, last, target, example);
        else
            return true;
    }
}