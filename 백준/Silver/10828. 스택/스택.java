import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        // 이 문제의 제한시간은 0.5초로 매우 짧기 때문에 println() 대신
        // BufferedReader, BufferedWriter를 사용하는 것이 좋다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] stack = new int[10005];
        int end = 0;
        
        for (int i = 0; i < N; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push" :
                    stack[end++] = Integer.parseInt(order[1]);
                    break;
                case "pop" :
                    if (end == 0)
                        bw.write("-1" + "\n");
                    else
                        bw.write(stack[--end] + "\n");
                    break;
                case "size" :
                    bw.write(end + "\n");
                    break;
                case "empty" :
                    if (end == 0)
                        bw.write("1" + "\n");
                    else
                        bw.write("0" + "\n");
                    break;
                case "top" :
                    if (end == 0)
                        bw.write("-1" + "\n");
                    else
                        bw.write(stack[end-1] + "\n");
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}