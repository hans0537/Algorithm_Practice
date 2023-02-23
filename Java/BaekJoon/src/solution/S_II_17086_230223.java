package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// #17086 아기상어2
// https://www.acmicpc.net/problem/17086
public class S_II_17086_230223 {

	static int N, M;
	static int[][] board;
	// 8 방향 탐색		상 상우 우 우하 하 좌하 좌 좌상 
	static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
	static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
	static int ans = 0;
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				bfs(i, j);
			}
		}
		
		System.out.println(ans);
	}

	static void bfs(int s, int e) {
		Queue<int[]> q = new LinkedList<>();
		int[][] visited = new int[N][M];
		
		q.add(new int[] {s, e});
		visited[s][e] = 1;
				
		while(!q.isEmpty()) {
			int[] tmp = q.poll();
			
			if(board[tmp[0]][tmp[1]] == 1) {
				ans = Math.max(ans, visited[tmp[0]][tmp[1]] - 1);
				break;
			}
			
			for (int d = 0; d < 8; d++) {
				int mx = tmp[0] + dx[d];
				int my = tmp[1] + dy[d];
				
				if (0 <= mx && mx < N && 0 <= my && my < M && visited[mx][my] == 0) {
					q.add(new int[] {mx, my});
					visited[mx][my] = visited[tmp[0]][tmp[1]] + 1;
				}
				
			}
		}
	}
}
