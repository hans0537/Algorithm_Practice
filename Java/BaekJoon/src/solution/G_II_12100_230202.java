package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #12100 2048문제
// https://www.acmicpc.net/problem/12100
public class G_II_12100_230202 {

	static int N;
	static int max = Integer.MIN_VALUE;
	static int[][] board;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		board = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		move(0);
	}
	
	public static void move(int cnt, ) {
		
		if (cnt == 0) {
			
		}
		
		
	}
}
