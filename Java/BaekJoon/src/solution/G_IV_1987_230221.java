package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #1987 알파벳
// https://www.acmicpc.net/problem/1987
public class G_IV_1987_230221 {

	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static int R, C;
	static int[][] board;
	static boolean[] visited;
	static int MAX = Integer.MIN_VALUE;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		board = new int[R][C];
		visited = new boolean[26];	// 지나간 알파벳 확인 배열

		for (int i = 0; i < R; i++) {
			String tmp = br.readLine();
			for(int j = 0; j < C; j++) {
				// 알파벳을 인덱스로 접근하기 위한 연산
				board[i][j] = tmp.charAt(j) - 'A';
			}
		}

		dfs(0, 0, 1);
		System.out.println(MAX - 1);
	}	

	static void dfs(int x, int y, int s) {
		
		// 이미 방분했던 알파벳 이면 최대값 갱신
		if (visited[board[x][y]]) {
			MAX = Math.max(MAX, s);
			return;
		}else {
			// 현재 위치를 방문표시후
			visited[board[x][y]] = true;
			
			// 4방향 탐색
			for (int i = 0; i < 4; i++) {
				int mx = x + dx[i];
				int my = y + dy[i];

				if (mx >= 0 && mx < R && my >= 0 && my < C) {
					dfs(mx, my, s + 1);
				}
			}
			// 다음 경우의 수를 위해 방문처리 취소
			visited[board[x][y]] = false;
		}
	}

}
