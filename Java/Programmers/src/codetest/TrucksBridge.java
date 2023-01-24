package codetest;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class TrucksBridge {

	public static void main(String[] args) {

		int bridge_length = 2;
		int weight = 10;
		int[] truck_weights = {7,4,5,6};
		
		int answer = 0;
		int total_weight = 0;
		
		Queue<Integer> bridge = new LinkedList<Integer>();
		
		for (int i = 0; i < truck_weights.length; i++) {
			
			while(true) {
				if(bridge.isEmpty()) {
					bridge.offer(truck_weights[i]);
					total_weight += truck_weights[i];
					answer += 1;
					break;
				}else if(bridge.size() == bridge_length) {
					total_weight -= bridge.poll();
				}else {
					if(truck_weights[i] + total_weight <= weight) {
						bridge.offer(truck_weights[i]);
						total_weight += truck_weights[i];
						answer += 1;
						break;
					}else {
						bridge.offer(0);
						answer += 1;
					}
				}
			}
		}
		System.out.println(answer + bridge_length);
        
	}

}
