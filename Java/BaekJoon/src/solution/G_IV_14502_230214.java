package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// #14502 연구소
// https://www.acmicpc.net/problem/14502
public class G_IV_14502_230214 {
	
	// 바이러스 좌표를 담을 클래스 선언 
	static class virus{
		int x, y;
		public virus(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
    static int N, M;
    static int[][] lab;
    // 상 하 좌 우
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    // 안전 지역 최대
    static int max = Integer.MIN_VALUE;
    
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        lab = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                lab[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        // 벽 세우기 시작
        dfs(0);
        System.out.println(max);
    }
    
    static void dfs(int wall) {
    	// 벽을 3개 세웠으면 바이러스 확산 시작
    	if (wall == 3) {
    		bfs();
    		return;
    	}
    	
    	// DFS를 통해 벽을 세우는 모든 경우의 수를 탐색
    	for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(lab[i][j] == 0) {
					lab[i][j] = 1;
					dfs(wall + 1);
					// 벽 처리가 끝나면 다음 경우의 수를 위해 0으로 다시 초기화
					lab[i][j] = 0;
				}
			}
		}
    }
    
    static void bfs() {
    	// 바이러스 확산을 모든 경우에 해야 하므로 
    	// 새로운 배열을 카피하여 최신화 하기 위함
    	int[][] copyLab = new int[N][M];
    	
    	// 기존에 있는 바이러스와 확산된 바이러스를 또 확산하기 위한 대기열
    	Queue<virus> q = new LinkedList<virus>();
    	
    	// 깊은복사를 하면서 처음 바이러스들의 위치를 큐에 저장
    	for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				copyLab[i][j] = lab[i][j];
				if (lab[i][j] == 2) q.add(new virus(i, j));
			}
		}
    	
    	// 큐가 빌때까지
    	while(!q.isEmpty()) {
    		// 먼저 들어온 바이러스부터 확산 시작
    		virus v = q.poll();
    		
    		// 바이러스 4방향 탐색 
    		for (int d = 0; d < 4; d++) {
				int mx = v.x + dx[d];
				int my = v.y + dy[d];
				
				// 범위 내에 있는 0인 공간으로 퍼트린후
				// 퍼트린 위치의 바이러스를 큐 대기열에 넣기
				if (mx >= 0 && mx < N && my >= 0 && my < M) {
					if(copyLab[mx][my] == 0) {
						copyLab[mx][my] = 2;
						q.add(new virus(mx, my));
					}
				}
			}
    	}
    	
    	int cnt = 0;
    	for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if(copyLab[i][j] == 0) cnt++;
			}
		}
    	
    	max = Math.max(max, cnt);
    }
}