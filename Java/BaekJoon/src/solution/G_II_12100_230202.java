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
		System.out.println(max);
	}

	public static void start(int cnt) {

		// 5번 이동 끝나면 최대값 찾기
		if (cnt == 5) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					max = Math.max(max, board[i][j]);
				}
			}
			return;
		}

		int[][] map = new int[N][N];
		// 각 경우의 수마다 기존 형태를 유지 해야하므로 임시 맵에다가 복사 해놓기
		for (int i = 0; i < board.length; i++) {
			map[i] = board[i].clone();
		}
		
		// 4방향 탐색
		for (int i = 0; i < 4; i++) {
			move(i);
			start(cnt + 1);
			
			// 탐색이 끝난후 복사해놓은것을 다시 board에 초기화 해주기
			for (int j = 0; j < N; j++) {
				board[j] = map[j].clone();
			}
		}
		

	}

	public static void move(int d) {
		// 4방향 이동 시작
		switch (d) {
		// 위로 몰기
		case 0:
			for (int i = 0; i < N; i++) {
				// 블럭들이 바로 위에 차곡차곡 쌓여야 함으로 그 위치를 줄 변수선언
				int idx = 0;
				// 쏠린 쪽의 최근 블럭의 값을 저장할 변수
				int block = 0;
				for (int j = 0; j < N; j++) {
					// 0이면 무시 아니면 이전에 저장한 블럭이 현재 위치의 블럭과 같은지 판별
					if (board[j][i] != 0) {
						if(block == board[j][i]) {
							// 같으면 현재위치를 0으로 바꿔주고
							// 쏠린쪽에 합쳐지게 함
							board[idx - 1][i] = block*2;
							block = 0;
							board[j][i] = 0;
						}else {
							// 블럭이 다른거면 쏠린 쪽 바로 위에 쌓아준다
							block = board[j][i];
							board[j][i] = 0;
							board[idx][i] = block;
							idx++;
						}
					}
				}
			}
			break;
		// 아래로 몰기
		case 1: 
			for (int i = 0; i < N; i++) {
				int idx = N - 1;
				int block = 0;
				for (int j = N - 1; j >= 0; j--) {
					if (board[j][i] != 0) {
						if(block == board[j][i]) {
							board[idx + 1][i] = block*2;
							block = 0;
							board[j][i] = 0;
						}else {
							block = board[j][i];
							board[j][i] = 0;
							board[idx][i] = block;
							idx--;
						}
					}
				}
			}
			break;
		// 왼쪽
		case 2: 
			for (int i = 0; i < N; i++) {
				int idx = 0;
				int block = 0;
				for (int j = 0; j < N; j++) {
					if (board[i][j] != 0) {
						if(block == board[i][j]) {
							board[i][idx - 1] = block*2;
							block = 0;
							board[i][j] = 0;
						}else {
							block = board[i][j];
							board[i][j] = 0;
							board[i][idx] = block;
							idx++;
						}
					}
				}
			}
			break;
		// 오른쪽
		case 3: 
			for (int i = 0; i < N; i++) {
				int idx = N - 1;
				int block = 0;
				for (int j = N - 1; j >= 0; j--) {
					if (board[i][j] != 0) {
						if(block == board[i][j]) {
							board[i][idx + 1] = block*2;
							block = 0;
							board[i][j] = 0;
						}else {
							block = board[i][j];
							board[i][j] = 0;
							board[i][idx] = block;
							idx--;
						}
					}
				}
			}
			break;
		}
	}
}
