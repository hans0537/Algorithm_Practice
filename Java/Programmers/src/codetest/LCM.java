package codetest;

public class LCM {
	
	public static int solution(int[] arr) {
		int answer = arr[0];
		
		// 배열의 첫번째 값을 기준으로 나머지와 비교
		// 최소공배수 이기때문에 루프 한번이면 끝
		for (int i = 0; i < arr.length; i++) {
			answer = lcm(answer, arr[i]);
		}
		
		return answer;
	}
	
	public static int gcd (int a, int b) {
		while(b!=0) {
			int r = a%b;
			a=b;
			b=r;
		}
		return a;
	}
	
	public static int lcm (int a, int b) {
		return a*b/gcd(a,b);
	}
	
	public static void main(String[] args) {

		int[] arr1 = {2,6,8,14};
		System.out.println(solution(arr1));
	}

}
