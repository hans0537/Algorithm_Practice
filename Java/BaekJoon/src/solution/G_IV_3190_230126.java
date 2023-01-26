package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #3190 뱀
// https://www.acmicpc.net/problem/3190
public class G_IV_3190_230126 {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		int[][] board = new int[N][N];
		
		// D이면 현재 위치(idx)에서 +1 
		// L이면 현재 위치(idx)에서 -1 
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		
		// 뱀 설정
		board[0][0] = 1;
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			// 사과를 2로 설정
			board[x-1][y-1] = 2;
		}
		
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				System.out.print(board[i][j] + " ");
			}
			System.out.println();
		}
		
		int L = Integer.parseInt(br.readLine());
		int[] seconds = new int[L];
		String[] dir = new String[L];
		for (int i = 0; i < L; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			seconds[i] = Integer.parseInt(st.nextToken());
			dir[i] = st.nextToken();
		}
		
		int time, idx = 0;
		while(true) {
			
		}
	}

}
