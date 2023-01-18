package solution;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// #1003 피보나치 함수
// https://www.acmicpc.net/problem/1003

// 주석 => 시간초과 코드
// 이유: 숫자가 클수록 계속적으로 재귀를 호출하여 카운트를 셈으로 시간초과 난다.

/*
public static int fibonacci(int n) {
	
	if(n == 0) {
		cnt0 ++;
		return 0;
	}else if (n == 1) {
		cnt1 ++;
		return 1;
	}else {
		return fibonacci(n - 1) + fibonacci(n - 2);
	}
}
*/

// 시간초과 해결 코드
// f(0) -> 0 : 1개, 1 : 0개
// f(1) -> 0 : 0개, 1 : 1개
// f(2) => f(0) + f(1) 0 : 1개 , 1 : 1개
// f(3) => f(2) + f(1) 즉 f(2)의 0과 1의 갯수에 f(1)의 각 갯수를 더하면 된다
// f(4) => f(3) + f(2) f(3) 0,1 갯수와 f(2) 0,1 갯수의 합
// 위와 같은 규칙으로 전 값의 0과 1의 갯수를 저장해놓으면 된다

public class S_III_1003_230118 {

//	static int cnt0;
//	static int cnt1;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		
		// 40보다 작거나 같고 또는 0이므로 크기는 41
		int[] f_0 = new int[41];
		// f(0) 저장
		f_0[0] = 1;
		f_0[1] = 0;
		
		int[] f_1 = new int[41]; 
		// f(1) 저장
		f_1[0] = 0;
		f_1[1] = 1;
		
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			
			for (int j = 2; j <= N; j++) {
				f_1[j] = f_1[j - 1] + f_1[j - 2];
				f_0[j] = f_0[j - 1] + f_0[j - 2];
			}

			System.out.println(f_0[N] + " " + f_1[N]);
//			cnt0 = 0;
//			cnt1 = 0;
//			fibonacci(Integer.parseInt(br.readLine()));
//			System.out.println(cnt0 + " " + cnt1);
			
			
		}

	}

}
