package codetest;

public class IntegerTriangle {

	public static int maxSum(int[][] triangle) {
		int answer = 0;
		
		int[][] temp = new int[triangle.length][triangle.length];
		
		temp[0][0] = triangle[0][0];
		for (int i = 1; i < triangle.length; i++) {
			for (int j = 0; j < triangle[i].length; j++) {
				if(j == 0) {
					temp[i][j] = temp[i-1][j] + triangle[i][j];
				}else if(j == triangle.length - 1) {
					temp[i][j] = temp[i-1][j-1] + triangle[i][j];
				}else {
					temp[i][j] = Math.max(temp[i-1][j] + triangle[i][j], temp[i-1][j-1] + triangle[i][j]);
				}
			}
		}
		
		for (int i = 0; i < temp[temp.length-1].length; i++) {
			if(answer < temp[temp.length-1][i]) {
				answer = temp[temp.length-1][i];
			}
		}
		return answer;
	}
	
	public static void main(String[] args) {

		int[][] triangle = {{7},{3,8},{8,1,0},{2,7,4,4},{4,5,2,6,5}};
        System.out.println(maxSum(triangle));
	}

}
