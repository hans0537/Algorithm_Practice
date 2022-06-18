package codetest;

import java.util.ArrayList;
public class Solution {

	public static void main(String[] args) {

		int n = 5;
		String[] plans = {"100 1 3", "500 4", "2000 5"};
		String[] clients = {"300 3 5", "1500 1", "100 1 3", "50 1 2"};

		int[] answer = new int[clients.length];

		ArrayList<Integer>[] tempData = new ArrayList[plans.length];
		for (int i = 0; i < tempData.length; i++) {
			tempData[i] = new ArrayList<Integer>();
		}

		ArrayList<Integer>[] dataList = new ArrayList[plans.length];
		for (int i = 0; i < dataList.length; i++) {
			dataList[i] = new ArrayList<Integer>();
		}

		for (int i = 0; i < plans.length; i++) {
			String[] temp = plans[i].split(" ");
			int[] temp1 = new int[temp.length];
			for (int j = 0; j < temp1.length; j++) {
				temp1[j] = Integer.parseInt(temp[j]);
			}
			for (int j = 0; j < temp1.length; j++) {
				tempData[i].add(temp1[j]);
			}
		}

		for (int i = 0; i < dataList.length; i++) {
			if(i == 0) {
				dataList[i] = tempData[i];
			}else {
				dataList[i] = tempData[i];
				for (int j = 1; j < dataList[i-1].size(); j++) {
					if(!dataList[i].contains(dataList[i-1].get(j))) {
						dataList[i].add(dataList[i-1].get(j));
					}
				}
			}

		}

		for (int i = 0; i < clients.length; i++) {
			String[] temp = clients[i].split(" ");
			int[] temp1 = new int[temp.length];
			for (int j = 0; j < temp1.length; j++) {
				temp1[j] = Integer.parseInt(temp[j]);
			}

			for (int j2 = 0; j2 < dataList.length; j2++) {
				if(temp1[0] > dataList[j2].get(0)) {
					answer[i] = 0;
				}
			}
			
			

		}
	}

}
