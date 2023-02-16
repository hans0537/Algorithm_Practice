package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// # 16234 인구이동
// https://www.acmicpc.net/problem/16234
public class G_V_16234_230216 {

	static int N, L, R;
	static int[][] A;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static boolean[][] visited;
	static ArrayList<int[]> list; //인구 이동이 필요한 좌표 리스트

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		A = new int[N][N];
		L = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		for (int r = 0; r < N; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < N; c++) {
				A[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		System.out.println(move());
	}
	
	// 이동한 날짜를 반환
	static int move() {
		int ans = 0;
		
		while(true) {
			boolean check = false;
			visited = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if(!visited[i][j]) {
						// bfs 탐색으로 열리는 국경이 있는지 확인하고
						// 없으면 list 배열이 비어있음
						// 인구를 받아와 인구 변동을 해준다
						int sum = bfs(i, j);
						if(list.size() > 1) {
							// 열린 국경선 인구 변경 시작
					        int avg = sum / list.size();
					        for(int[] k : list) {
					            A[k[0]][k[1]] = avg;
					        }
					        check = true;
						}
					}
				}
			}
			if(!check) return ans;
			ans++;
		}
	}
	
	// 인구 이동
	static int bfs(int x, int y) {
		// 인접한 모든 노드를 방문하기 위한 큐
		Queue<int[]> q = new LinkedList<>();
		// 인접한 모든 노드를 방문하여 이동이 가능한 것들만 넣는 배열
		list = new ArrayList<>();
		
		q.offer(new int[] {x,y});
		list.add(new int[] {x,y});
		visited[x][y] = true;
		
		int sum = A[x][y];
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			
			for (int d = 0; d < 4; d++) {
				int mx = cur[0] + dx[d];
				int my = cur[1] + dy[d];
				if(mx >= 0 && my >= 0 && mx < N && my < N && !visited[mx][my]) {
					int diff = Math.abs(A[cur[0]][cur[1]] - A[mx][my]);
					if(L <= diff && diff <= R) {
						q.offer(new int[] {mx, my});
						list.add(new int[] {mx, my});
						sum += A[mx][my];
						visited[mx][my] = true;
					}
				}
			}
		}
		return sum;
	}
}
