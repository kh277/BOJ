import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        
        // 이 문제의 제한시간은 0.5초로 매우 짧기 때문에 println() 대신
        // BufferedReader, BufferedWriter를 사용하는 것이 좋다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] queue = new int[10005];
        int front = 0;
        int rear = 0;
        
        for (int i = 0; i < N; i++) {
            String[] order = br.readLine().split(" ");
            switch (order[0]) {
                case "push" :
                    queue[rear] = Integer.parseInt(order[1]);
                    rear++;
                    break;
                case "pop" :
                    if (front == rear)
                        bw.write("-1" + "\n");
                    else {
                        bw.write(queue[front] + "\n");
                        front++;
                    }
                    break;
                case "size" :
                    bw.write((rear - front) + "\n");
                    break;
                case "empty" :
                    if (front == rear)
                        bw.write("1" + "\n");
                    else
                        bw.write("0" + "\n");
                    break;
                case "front" :
                    if (front == rear)
                        bw.write("-1" + "\n");
                    else
                        bw.write(queue[front] + "\n");
                    break;
                case "back" :
                    if (front == rear)
                        bw.write("-1" + "\n");
                    else
                        bw.write(queue[rear-1] + "\n");
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}