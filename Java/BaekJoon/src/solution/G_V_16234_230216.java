package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

// # 16234 인구이동
// https://www.acmicpc.net/problem/16234
public class G_V_16234_230216 {

	static int N, L, R;
	static int[][] A;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		A = new int[N][N];
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < N; c++) {
				A[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		
	}
	
	static void move() {
		
	}
	
	
}
