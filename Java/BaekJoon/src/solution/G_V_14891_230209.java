package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #14891 톱니바퀴
// https://www.acmicpc.net/problem/14891
public class G_V_14891_230209 {

	static String[] t1;
	static String[] t2;
	static String[] t3;
	static String[] t4;
	// 회전 시킬 톱니바퀴
	static int[] t;
	// 회전 시킬 방향
	static int[] d;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		t1 = br.readLine().split("");
		t2 = br.readLine().split("");
		t3 = br.readLine().split("");
		t4 = br.readLine().split("");
		
		int K = Integer.parseInt(br.readLine());
		t = new int[K];
		d = new int[K];
		
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine());
			t[i] = Integer.parseInt(st.nextToken());
			d[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 0; i < K; i++) {
			if (t[i] == 1) {
				
			}
		}
		
	}
}
