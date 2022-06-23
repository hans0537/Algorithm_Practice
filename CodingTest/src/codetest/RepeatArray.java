package codetest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class RepeatArray {
	
	public static int[] repeatArray(int[] arr) {
		int[] answer = {};
		
		// 기존 HashMap형태는 key값이 정수일때 자동 오름차순 정렬이 된다
		// LinkedHashMap은 입력한 순서대로 저장이 되므로 앞에 있는 숫자들 부터 중복된 숫자를 저장 가능하다
		Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
		ArrayList<Integer> temp = new ArrayList<Integer>();
		
		for (int i = 0; i < arr.length; i++) {
			if (!map.containsKey(arr[i])) {
				map.put(arr[i], 1);
			}else {
				map.put(arr[i], map.get(arr[i])+1);
			}
		}
		
		List<Integer> keySet = new ArrayList<Integer>(map.keySet());
		
		for (int i = 0; i < keySet.size(); i++) {
			if(map.get(keySet.get(i)) != 1) {
				temp.add(map.get(keySet.get(i)));
			}
		}
		
		if(temp.size()==0) {
			answer = new int[1];
			answer[0] = -1;
		}else {
			answer = new int[temp.size()];
			for (int i = 0; i < temp.size(); i++) {
				answer[i] = temp.get(i);
			}
		}
		
		return answer;
		
	}
	public static void main(String[] args) {

		int[] arr1 = {1, 2, 3, 3, 3, 3, 4, 4};
		int[] arr2= {3, 2, 4, 4, 2, 5, 2, 5, 5};
		int[] arr3 = {3, 5, 7, 9, 1};
		int[] arr4 = {10, 7,3, 5 ,7,7,7,7, 9, 1, 10,3,3};
		
		System.out.println(Arrays.toString(repeatArray(arr1)));
		System.out.println(Arrays.toString(repeatArray(arr2)));
		System.out.println(Arrays.toString(repeatArray(arr3)));
		System.out.println(Arrays.toString(repeatArray(arr4)));
	}

}
