package D5;

import java.util.Scanner;

// 1247. [S/W 문제해결 응용] 3일차 - 최적 경로
public class D5_1247_230117 {
	
	// 미완성
	static int dis;
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int num = sc.nextInt();
			
			Node[] list = new Node[num + 2];
			
			// 집 저장
			list[0] = new Node(sc.nextInt(), sc.nextInt());
			
			// 회사 저장
			list[num + 1] = new Node(sc.nextInt(), sc.nextInt());
			
			for (int i = 0; i < num; i++) {
				int x = sc.nextInt();
				int y = sc.nextInt();
				list[i] = new Node(x, y);
			}
			
			dis = 0;
			minDis(list, 0, 2, 0);
		}
		
	}
	
	public static int distance(Node[] list, int idx1, int idx2) {
		
		return Math.abs(list[idx1].x - list[idx2].x) + Math.abs(list[idx1].y - list[idx2].y);
	}
	
	public static void minDis(Node[] list, int i, int j, int cnt) {
		int min = distance(list, i, j);
		
		if(cnt == list.length) return;
		
		int tmp = distance(list, i, i);
		
		if(min > tmp) {
			min = tmp;
			minDis(list, i, j + 1, cnt);
		}else {
			minDis(list, i, j + 1, cnt);
		}
		
	}
	
}

class Node {
	
	int x;
	int y;
	
	public Node(int x, int y) {
		this.x = x;
		this.y = y;
	}
	
}
