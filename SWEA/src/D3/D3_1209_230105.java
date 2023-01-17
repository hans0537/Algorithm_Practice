package D3;

import java.util.Scanner;

// 1209. [S/W 문제해결 기본] 2일차 - Sum
public class D3_1209_230105 {
	
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);

        for(int test_case = 1; test_case <= 10; test_case++)
		{
            int T;
			T=sc.nextInt();
            int[][] arr = new int[100][100];
            for(int i = 0; i < arr.length; i++) {
             	for(int j = 0; j < arr.length; j++) {
					arr[i][j] = sc.nextInt();
                }   
            }
            int max1 = maxRow(arr);
            int max2 = maxCol(arr);
            int max3 = maxDiag(arr);
            
            System.out.println("#" + T + " " + Math.max(Math.max(max1, max2), max3));
		}
	}
    
    public static int maxRow(int[][] arr) {
        int max = 0;
        for(int i = 0; i < arr.length; i++) {
            int sum = 0;
            for(int j = 0; j < arr.length; j++) {
                sum += arr[i][j];
            }
            if(max < sum) max = sum;
        }
        return max;
    }
    
    public static int maxCol(int[][] arr) {
        int max = 0;
        for(int i = 0; i < arr.length; i++) {
            int sum = 0;
            for(int j = 0; j < arr.length; j++) {
                sum += arr[j][i];
            }
            if(max < sum) max = sum;
        }
        return max;
    }
    
    public static int maxDiag(int[][] arr) {
        int sum1 = 0;
        for(int i = 0; i < arr.length; i++) {
            sum1 += arr[i][i];
        }        
        
        int sum2 = 0;
        for(int i = arr.length - 1; i >= 0; i--) {
            sum2 += arr[arr.length - i - 1][i];
        }
        
        if(sum1 < sum2) return sum2;
        else if(sum1 > sum2) return sum1;
        else return sum1;
    }
    
}
