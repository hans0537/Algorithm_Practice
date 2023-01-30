package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #14499 주사위 굴리기
// https://www.acmicpc.net/problem/14499

public class G_IV_14499_230130 {
	
	static int N, M, x, y;
	static int[][] map;
	
	//   1
	// 3 0 2
	//   4
	//   5
	static int[] dice = new int[6];
	
	// 동 = 1, 서 = 2, 북 = 3, 남 = 4 을 위한 이동 좌표
	static int[] dx = {0, 0, -1, 1};
	static int[] dy = {1, -1, 0, 0};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		x = Integer.parseInt(st.nextToken());
		y = Integer.parseInt(st.nextToken());
		
		int K = Integer.parseInt(st.nextToken());
		
		map = new int[N][M];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		// 이동 명령 실행
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < K; i++) {
			int m = Integer.parseInt(st.nextToken());
			move(m - 1);
		}
	}
	
	public static void move(int m) {
		int mx = x + dx[m];
		int my = y + dy[m];
		
		// 범위를 벗어났을때 무시
		if(mx < 0 || mx > N - 1 || my < 0 || my > M - 1) return;
		
		// 주사위 굴리기
		roll(m,mx,my);

		x = mx; y = my;
	}
	
	public static void roll(int m, int x, int y) {
		// 방향에 따라 주사위 배열 위치 변경
		// 위를 바라보는 방향은 0번째, 바닥면은 5번째
		int tmp = dice[0];
		switch (m) {
		case 0: // 동
			dice[0] = dice[3];
			dice[3] = dice[5];
			dice[5] = dice[2];
			dice[2] = tmp;
			break;
		case 1: // 서
			dice[0] = dice[2];
			dice[2] = dice[5];
			dice[5] = dice[3];
			dice[3] = tmp;
			break;
		case 2: // 북
			dice[0] = dice[4];
			dice[4] = dice[5];
			dice[5] = dice[1];
			dice[1] = tmp;
			break;
		case 3: // 남
			dice[0] = dice[1];
			dice[1] = dice[5];
			dice[5] = dice[4];
			dice[4] = tmp;
			break;
		}
		
		// map 이 0일때 와 아닐때 처리
		if(map[x][y] == 0) {
			map[x][y] = dice[5];
		}else {
			dice[5] = map[x][y];
			map[x][y] = 0;
		}
		
		System.out.println(dice[0]);
	}
}
