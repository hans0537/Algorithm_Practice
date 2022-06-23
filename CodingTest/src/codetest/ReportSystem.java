package codetest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ReportSystem {

	public static int[] solution(String[] id_list, String[] report, int k) {
		int[] answer = {};


		Map<String, Integer> reportNum = new HashMap<>();
		for (int i = 0; i < id_list.length; i++) {
			reportNum.put(id_list[i], 0);
		}

		Map<String, ArrayList<String>> reportList = new HashMap<>();
		
		for (int i = 0; i < report.length; i++) {
			String[] temp = report[i].split(" ");
			if(temp[0].equals(temp[1])) {
				return null;
			}else if(!reportNum.containsKey(temp[0]) || !reportNum.containsKey(temp[1])) {
				return null;
			}else {
				if(reportList.containsKey(temp[0])) {
					if(!reportList.get(temp[0]).contains(temp[1])) {
						reportList.get(temp[0]).add(temp[1]);
					}
				}else {
					reportList.put(temp[0], new ArrayList<String>());
					reportList.get(temp[0]).add(temp[1]);
				}
			}
		}
		
		for (String key : reportList.keySet()) {
			for (String i : reportList.get(key)) {
				reportNum.put(i, reportNum.get(i) + 1);
			}
		}
		System.out.println(reportList);
		System.out.println(reportNum);
		return answer;

	}

	public static void main(String[] args) {

		int[] test1 = solution(new String[] {"muzi", "frodo", "apeach", "neo"}, new String[] {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"}, 2);
		int[] test2 = solution(new String[] {"con", "ryan"}, new String[] {"ryan con", "ryan con", "ryan con", "ryan con"}, 3);


	} 

}
