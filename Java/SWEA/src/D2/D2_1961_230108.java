package D2;

import java.util.Scanner;

// 1961. 숫자 배열 회전
public class D2_1961_230108 {
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int n = sc.nextInt();

			int[][] arr = new int[n][n];
			String[][] answer = new String[n][3];
			
			for (int i = 0; i < arr.length; i++) {
				for (int j = 0; j < arr.length; j++) {
					arr[i][j] = sc.nextInt();
				}
			}
			
			rotate90(answer, arr);
			rotate180(answer, arr);
			rotate270(answer, arr);
			
			System.out.println("#" + test_case);
			for (int i = 0; i < answer.length; i++) {
				for (int j = 0; j < answer[i].length; j++) {
					System.out.print(answer[i][j] + " ");
				}
				System.out.println();
			}
		}
	}
	
	public static void rotate90(String[][] answer, int[][] arr) {
		for (int i = 0; i < arr.length; i++) {
			String num = "";
			for (int j = arr.length-1; j >= 0; j--) {
				num += arr[j][i];
			}
			answer[i][0] = num;
		}
	}

	public static void rotate180(String[][] answer, int[][] arr) {
		int k = 0;
		for (int i = arr.length - 1; i >= 0; i--) {
			String num = "";
			for (int j = arr.length-1; j >= 0; j--) {
				num += arr[i][j];
			}
			answer[k++][1] = num;
		}
	}

	public static void rotate270(String[][] answer, int[][] arr) {
		int k = 0;
		for (int i = arr.length - 1; i >= 0; i--) {
			String num = "";
			for (int j = 0; j < arr.length; j++) {
				num += arr[j][i];
			}
			answer[k++][2] = num;
		}
	}
}
