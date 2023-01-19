package solution;

import java.util.ArrayList;

public class S_V_4673_230119 {

	public static void main(String[] args) {

		ArrayList<Integer> genList = new ArrayList<Integer>();
		
		for (int i = 1; i <= 10000; i++) {
			genList.add(isGen(i));
		}
		
		for (int i = 1; i <= 10000; i++) {
			if (!genList.contains(i)) {
				System.out.println(i);
			}
		}
		
	}

	public static int isGen(int num) {
		int tot = num;
		
		while (num > 0){
			tot += num % 10;
			num /= 10;
		}
		
		return tot;
	}
}
