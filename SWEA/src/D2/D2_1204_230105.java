package D2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

// 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
public class D2_1204_230105 {
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			int j = sc.nextInt();
			Map<Integer, Integer> map = new HashMap<Integer, Integer>();

			for (int i = 0; i < 1000; i++) {
				int num = sc.nextInt();

				if(map.containsKey(num)) map.put(num, map.get(num) + 1);
				else map.put(num, 1);
			}

			int maxVal = Collections.max(map.values());

			List<Integer> keys = new ArrayList<Integer>();
			for(int key : map.keySet()) {
				if(map.get(key) == maxVal) keys.add(key);
			}

			System.out.println("#" + j + " " + Collections.max(keys));
		}
	}
}
