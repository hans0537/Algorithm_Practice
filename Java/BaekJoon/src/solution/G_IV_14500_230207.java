package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #14500 테트로미노
// https://www.acmicpc.net/problem/14500
public class G_IV_14500_230207 {

	static int N, M;
	static int[][] box;
	static boolean[][] visited;
	static int max = Integer.MIN_VALUE;
	static int[] dx = {-1, 1, 0, 0}; // 상 하
	static int[] dy = {0, 0, -1, 1}; // 좌 우
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		box = new int[N][M];
		visited = new boolean[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				box[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				visited[i][j] = true;
				// 처음 위치 값 sum 에 넣기
				tetro(i, j, box[i][j], 1);
				visited[i][j] = false;
			}
		}
		
		System.out.println(max);
	}
	
	public static void tetro(int x, int y, int sum, int depth) {
		
		// 4개로 모양 만들었으면 최대값가 비교후 재귀 종료
		if (depth == 4) {
			max = Math.max(max, sum);
			return;
		}
		
		// 상하좌우 탐색하면서 테트로미노 모양 만들기
		for (int i = 0; i < 4; i++) {
			int mx = x + dx[i];
			int my = y + dy[i];
			
			// 벽을 나가면 다시 가능한 경로로 다시 탐색
			if (mx < 0 || mx >= N || my < 0 || my >= M) {
				continue;
			}
			
			// 아직 방문 하지 않은 칸이면
			if(!visited[mx][my]) {
				// ㅗ 모양을 탐색하기 위해선 2번째에서 한번더 탐색을 해주어야 한다.
				if (depth == 2) {
					visited[mx][my] = true;
					// 다음위치로 보내는게 아닌 현재 위치에서 다른 쪽으로 뻗어 나가야 하니
					// 다음 위치 갔다가 현재 위치에서 다른쪽으로 뻗어나가기
					// tetro(mx, my, sum + box[mx][my], depth + 1); => 틀림
					tetro(x, y, sum + box[mx][my], depth + 1);
					visited[mx][my] = false;
				}
				visited[mx][my] = true;
				tetro(mx, my, sum + box[mx][my], depth + 1);
				visited[mx][my] = false;
			}
		}
	}

}
