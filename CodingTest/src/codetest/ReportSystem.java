package codetest;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class ReportSystem {

	// 다른 사람의 코드 리뷰
	public static int[] anotherSolution(String[] id_list, String[] report, int k) {
		// 중복 신고는 streamApi distinct 로 제거
		List<String> list = Arrays.stream(report).distinct().collect(Collectors.toList());
		HashMap<String, Integer> count = new HashMap<>();
		for (String s : list) {
			String target = s.split(" ")[1];
			//key값이 없을시 default값으로 간단하게 처리
			count.put(target, count.getOrDefault(target, 0) + 1);
		}

		return Arrays.stream(id_list).map(_user -> {
			final String user = _user;
			List<String> reportList = list.stream().filter(s -> s.startsWith(user + " ")).collect(Collectors.toList());
			return reportList.stream().filter(s -> count.getOrDefault(s.split(" ")[1], 0) >= k).count();
		}).mapToInt(Long::intValue).toArray();
	}

	// 나의 코드
	public static int[] mySolution(String[] id_list, String[] report, int k) {
		int[] answer = new int[id_list.length];

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

		int i = 0;
		for(String id : id_list) {
			int cnt = 0;
			if(reportList.containsKey(id)) {
				for(String id1 : reportList.get(id)) {
					if(reportNum.get(id1) >= k) {
						cnt ++;
					}
				}
			}
			answer[i++] = cnt;
		}
		return answer;

	}

	public static void main(String[] args) {

		int[] test1 = mySolution(new String[] {"muzi", "frodo", "apeach", "neo"}, new String[] {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"}, 2);
		int[] test2 = mySolution(new String[] {"con", "ryan"}, new String[] {"ryan con", "ryan con", "ryan con", "ryan con"}, 3);

		for (int i = 0; i < test1.length; i++) {
			System.out.println(test1[i]);
		}
		for (int i = 0; i < test2.length; i++) {
			System.out.println(test2[i]);
		}
	} 

}
