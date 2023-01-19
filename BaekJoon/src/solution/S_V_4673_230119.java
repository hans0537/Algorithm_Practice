package solution;

import java.util.ArrayList;

// #4673 셀프 넘버
// https://www.acmicpc.net/problem/4673

public class S_V_4673_230119 {

	public static void main(String[] args) {

		ArrayList<Integer> genList = new ArrayList<Integer>();
		
		// 제너레이터 숫자를 배열에 넣고 
		for (int i = 1; i <= 10000; i++) {
			genList.add(isGen(i));
		}
		
		// 비교
		for (int i = 1; i <= 10000; i++) {
			if (!genList.contains(i)) {
				System.out.println(i);
			}
		}
		
	}
	
	// generator 함수 
	public static int isGen(int num) {
		int tot = num;
		
		while (num > 0){
			tot += num % 10;
			num /= 10;
		}
		
		return tot;
	}
}
