package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// #14503 로봇청소기
// https://www.acmicpc.net/problem/14503

public class G_V_14503_230117 {

	public static int[][] area;
	public static int cnt,n,m;
	public static int[] dx = {0,1,0,-1}; // 동서
	public static int[] dy = {-1,0,1,0}; // 남북

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		area = new int[n][m];

		st = new StringTokenizer(br.readLine(), " ");
		int ry = Integer.parseInt(st.nextToken());
		int rx = Integer.parseInt(st.nextToken());
		int rd = Integer.parseInt(st.nextToken());

		// 처음 자리 청소
		cnt = 1;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < m; j++) {
				area[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		clean(rx, ry, rd);
		System.out.println(cnt);
	}

	public static void clean(int rx, int ry, int rd) {
		// 현재 위치 청소 처리
		area[ry][rx] = 2;
		
		// 동서남북 청소 체크
		for (int i = 0; i < 4; i++) {
			rd = (rd + 3) % 4; // 북 -> 서, 동 -> 북, 남 -> 동, 서 -> 남
			
			if(area[ry + dy[rd]][rx + dx[rd]] == 0) {
				// 빈곳으로 움직이는 것이므로 미리 cnt 올려주기
				cnt++;
				clean(rx + dx[rd], ry + dy[rd], rd);
				// 움직이고 나중에 다시 호출될때 안움직이게 리턴
				return;
			}

		}

		// 위에서 동서남북 확인을 하고 나왔기 때문에
		// 뒤에 벽이 있는지만 체크하면 된다.
		int tmp = (rd + 2) % 4; // 뒤로가기
		
		if(area[ry + dy[tmp]][rx + dx[tmp]] != 1) {
			clean(rx + dx[tmp], ry + dy[tmp], rd);
		}
	}
}
