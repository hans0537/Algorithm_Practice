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

		start(0);
	}

	public static void start(int cnt) {

		// 5번 이동 끝나면 최대값 찾기
		if (cnt == 5) {
			//Math.max(cnt, cnt)
			return;
		}

		int[][] map = new int[N][N];
		// 각 경우의 수마다 기존 형태를 유지 해야하므로 임시 맵을 복사해서 사용
		for (int i = 0; i < board.length; i++) {
			map[i] = board[i].clone();
		}

	}

	public static void move(int d) {
		// 4방향 이동 시작
		switch (d) {
		// 위로 몰기
		case 0:
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N - 1; j++) {
					if(board[j][i] == board[j + 1][i]) {
						board[j][i] += board[j + 1][i];
						board[j + 1][i] = 0;
					}else if(board[j + 1][i] == 0) {
						board[j][i] = board[j + 1][i];
						board[j + 1][i] = 0;
					}
				}
			}
			break;
		// 아래로 몰기
		case 1: 
			for (int i = 0; i < N; i++) {
				for (int j = N - 1; j > 0; j--) {
					if(board[j][i] == board[j - 1][i]) {
						board[j][i] += board[j - 1][i];
						board[j - 1][i] = 0;
					}else if(board[j - 1][i] == 0) {
						board[j][i] = board[j - 1][i];
						board[j - 1][i] = 0;
					}
				}
			}
			break;
		// 왼쪽
		case 2: 
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(board[i][j] == board[i + 1][j]) {
						board[i][j] += board[i + 1][j];
						board[i + 1][j] = 0;
					}else if(board[i + 1][j] == 0) {
						board[i][j] = board[i + 1][j];
						board[i + 1][j] = 0;
					}
				}
			}
			break;
		// 오른쪽
		case 3: 
			for (int i = 0; i < N; i++) {
				for (int j = N - 1; j > 0; j--) {
					if(board[i][j] == board[i - 1][j]) {
						board[i][j] += board[i - 1][j];
						board[i - 1][j] = 0;
					}else if(board[i - 1][j] == 0) {
						board[i][j] = board[i - 1][j];
						board[i - 1][j] = 0;
					}
				}
			}
			break;
		}
	}
}
