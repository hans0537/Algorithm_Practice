package codetest;

import java.util.ArrayList;
import java.util.Arrays;

public class LottoHighAndLow {

	public static int[] solution(int[] lottos, int[] win_nums) {
		int[] answer = new int[2];

		int low = 0;
		int high = 0;

		ArrayList<Integer> lottosTemp = new ArrayList<Integer>();
		ArrayList<Integer> win_numsTemp = new ArrayList<Integer>();

		for (int i : lottos) {
			lottosTemp.add(i);
		}
		for (int i : win_nums) {
			win_numsTemp.add(i);
		}

		for (int i = 0; i < lottosTemp.size(); i++) {
			if(win_numsTemp.contains(lottosTemp.get(i))) low++;
			if(lottosTemp.get(i) == 0) high++;
		}

		high = high + low;

		answer[0] = getScore(high);
		answer[1] = getScore(low);

		return answer;
	}
	
	public static int getScore(int num) {
		if(num == 6) return 1;
		else if(num == 5) return 2;
		else if(num == 4) return 3;
		else if(num == 3) return 4;
		else if(num == 2) return 5;
		return 6;
	}
	
	public static void main(String[] args) {

		int[] test1 = solution(new int[] {44, 1, 0, 0, 31, 25}, new int[] {31, 10, 45, 1, 6, 19});
		int[] test2 = solution(new int[] {0, 0, 0, 0, 0, 0}, new int[] {38, 19, 20, 40, 15, 25});
		int[] test3 = solution(new int[] {45, 4, 35, 20, 3, 9}, new int[] {20, 9, 3, 45, 4, 35});

		System.out.println(Arrays.toString(test1));
		System.out.println(Arrays.toString(test2));
		System.out.println(Arrays.toString(test3));
	}

}
