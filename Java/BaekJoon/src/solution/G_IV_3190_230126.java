package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
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
		
		// 뱀 설정 (길이)
		ArrayList<int[]> snake = new ArrayList<int[]>();
		snake.add(new int[] {0,0});
		
		for (int i = 0; i < K; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			// 사과를 2로 설정
			board[x-1][y-1] = 2;
		}
		
		int L = Integer.parseInt(br.readLine());
		// 시간과 방향 정보
		int[][] dir = new int[L][2];
		
		for (int i = 0; i < L; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			dir[i][0] = Integer.parseInt(st.nextToken());
			dir[i][1] = (st.nextToken().equals("D") ? 1 : -1); // D이면 +1, L이면 -1
		}
		
		int time = 0, idx = 0, x = 0, y = 0, d = 0;
		
		while(true) {
			time++;
			
			int mx = x + dx[d];
			int my = y + dy[d];
			
			// 보드를 나갔을 경우
			if (mx == -1 || my == -1 || mx == N || my == N) break;
			
			// 몸통에 닿은 경우
			if(check(snake, mx, my)) break;
			
			// 다음에 사과를 먹으면
			if(board[mx][my] == 2) {
				// 몸길이 늘려 저장
				// 사과 삭제
				board[mx][my] = 0;
				snake.add(new int[] {mx, my});
			}else {
				// 사과가 없으면 늘리고 꼬리 삭제
				snake.add(new int[] {mx, my});
				snake.remove(0);
			}
			
			x = mx;
			y = my;
			
			// 시간이 지나면 방향 전환
			if (idx < L) {
                if (time == dir[idx][0]) { // 다음 방향 설정
                    d = (d + dir[idx][1]) % 4;
                    if (d == -1) d = 3;
                    idx++;
                }
            }
		}
		
		System.out.println(time);
	}
	
	public static boolean check(ArrayList<int[]> snake, int mx, int my) {
		for (int i = 0; i < snake.size(); i++) {
			int[] s = snake.get(i);
			// 몸의 좌표와 다음 좌표가 같으면 부딪힘
			if(mx == s[0] && my == s[1]) return true;
		}
		return false;
	}
}
