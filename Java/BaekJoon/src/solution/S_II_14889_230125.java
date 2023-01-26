package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 14889 스타트와 링크
// https://www.acmicpc.net/problem/14889
public class S_II_14889_230125 {

	static int[][] arr;
	static int min = Integer.MAX_VALUE;
	static boolean[] check;
	static int N;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		
		N = Integer.parseInt(st.nextToken());
		
		arr = new int[N][N];
		check = new boolean[N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0, 0);
		System.out.println(min);
	}
	
	// cnt는 팀조합 개수
	public static void dfs(int idx, int cnt) {
		
		// 팀이 만들어지면 해당 재귀 종료
		// 능력치 계산후 최소값 최신화
		if (cnt == N / 2) {
			ability();
			return;
		}
		
		for (int i = idx; i < N; i++) {
			// 방문 체크
			if(!check[i]) {
				check[i] = true;
				dfs(i + 1, cnt + 1);
				// 재귀가 끝나면 다시 원상복구
				check[i] = false;
			}
		}
	}
	
	public static void ability() {
		int start = 0;
		int link = 0;
		
		// 모든 사람 비교
		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				// i 와 j 가 서로 방문 되어 있으면 스타트 팀으로 능력치 추가
				if(check[i] == true && check[j] == true) {
					start += arr[i][j] + arr[j][i];
				}
				// i 와 j 가 서로 방문 안되어 있으면 링크 팀
				else if(check[i] == false && check[j] == false) {
					link += arr[i][j] + arr[j][i];
				}
			}
		}
		
		int ans = Math.abs(start - link);
		
		// 만약 0 이면 최소값이므로 바로 종료
		if(ans == 0) {
			System.out.println(ans);
			System.exit(0);
		}
		min = Math.min(min, ans);
	}

}
