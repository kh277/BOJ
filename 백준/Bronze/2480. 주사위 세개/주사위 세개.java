import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int[] num = new int[3];
        num[0] = in.nextInt();
        num[1] = in.nextInt();
        num[2] = in.nextInt();
        Arrays.sort(num);

        int[] arr = calculate(num[0], num[1], num[2]);
        System.out.println(arr[0]*10000 + arr[1]*1000 + arr[2]*100);

    }
    
    // a에는 10000원의 개수, b에는 1000원의 개수, c에는 100원의 개수
    public static int[] calculate(int a, int b, int c) {
        int[] arr = new int[3];
        if (a != b && b != c) {
            arr[0] = 0;
            arr[1] = 0;
            arr[2] = c;
        }
        else if (a != b || b != c) {
            arr[0] = 0;
            arr[1] = 1;
            arr[2] = compare(a, b, c);
        }
        else {
            arr[0] = 1;
            arr[1] = compare(a, b, c);
            arr[2] = 0;
        }
        return arr;
    }
    
    // 세 숫자 중 같은 수 반환
    public static int compare (int a, int b, int c) {
        if (a == b)
            return a;
        else if (b == c)
            return b;
        else
            return a;
    }
}