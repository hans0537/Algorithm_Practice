package D4;

import java.util.Scanner;

// 1226. [S/W 문제해결 기본] 7일차 - 미로1
public class D4_1226_230109 {

	static int ans = 0;

	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);

		for(int test_case = 1; test_case <= 10; test_case++)
		{
			int T = sc.nextInt();

			int[][] box = new int[16][16];

			for (int i = 0; i < box.length; i++) {
				String line = sc.next();
				for (int j = 0; j < box.length; j++) {
					box[i][j] = Integer.parseInt(line.split("")[j]);
				}
			}

			ans = 0;
			move(box, 1, 1);

			System.out.println("#" + T + " " + ans);
		}
	}

	public static void move(int[][] arr, int i, int j) {
		if(arr[i][j] == 3) {
			ans = 1;
			return;
		}

		arr[i][j] = 2;

		if(arr[i + 1][j] == 0 || arr[i + 1][j] == 3) {
			move(arr, i + 1, j);
		}

		if(arr[i][j + 1] == 0 || arr[i][j + 1] == 3) {
			move(arr, i, j + 1);
		}

		if(arr[i - 1][j] == 0 || arr[i - 1][j] == 3) {
			move(arr, i - 1, j);
		}

		if(arr[i][j - 1] == 0 || arr[i][j - 1] == 3) {
			move(arr, i, j - 1);
		}
	}
}
