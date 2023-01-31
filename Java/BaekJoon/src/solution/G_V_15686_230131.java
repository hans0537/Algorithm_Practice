package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

// #15686 치킨배달
// https://www.acmicpc.net/problem/15686

public class G_V_15686_230131 {
	
	static int[][] arr;
	static int N, M;
	// 치킨집과 집의 좌표를 저장할 배열 선언
	static ArrayList<int[]> chicken;
	static ArrayList<int[]> house;
	static int min = Integer.MAX_VALUE;
	static boolean[] visit;
	
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		arr = new int[N][N];
		chicken = new ArrayList<>();
		house = new ArrayList<>();
		
		// 입력을 받을때 치킨집과 집의 좌표를 배열에 저장
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			
				if(arr[i][j] == 1) house.add(new int[] {i, j});
				else if (arr[i][j] == 2) chicken.add(new int[] {i, j});
			}
		}
		
		visit = new boolean[chicken.size()];
		dfs(0,0);
		System.out.println(min);
	}
	
	public static void dfs(int cnt, int start) {
		// 치킨집이 M개의 수가 될때 각 집과의 최단거리를 계산하여
		// 최단거리 최신화
		if(cnt == M) {
			int tot = 0;
			
			for (int i = 0; i < house.size(); i++) {
				int dis = Integer.MAX_VALUE;
				
				// 집과 치킨집 중 open한 치킨집의 모든 거리를 비교한다.
                // 그 중, 최소 거리를 구한다.
				for (int j = 0; j < chicken.size(); j++) {
					if(visit[j]) {
						int tmp = Math.abs(house.get(i)[0] - chicken.get(j)[0]) + Math.abs(house.get(i)[1] - chicken.get(j)[1]);
						dis = Math.min(dis, tmp);
					}
				}
				tot += dis;
			}
			min = Math.min(min, tot);
			return;
		}
		
		// 백트랙킹
		for (int i = start; i < chicken.size(); i++) {
			if(!visit[i]) {
				visit[i] = true;
				dfs(cnt + 1, i + 1);
				visit[i] = false;
			}
		}
	}
}
