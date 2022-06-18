package codetest;

public class Stations {
	public static int solution(int n, int[] stations, int w) {
        int answer = 0;

        if(stations.length == 1) {
        	int left = 0;
        	if(stations[0] == 1) {
        		left = 1 + w;
        	}else if(stations[0] == n) {
        		left = stations[0] - w - 1;
        	}
        	
			if(left % (w*2 + 1) == 0) {
				answer += left/(w*2 + 1);
			}else {
				answer += left/(w*2 + 1) + 1;
			}
			int right = n - stations[0] - w;
			if(right % (w*2 + 1) == 0) {
				answer += right/(w*2 + 1);
			}else {
				answer += right/(w*2 + 1) + 1;
			}
        }else if(stations.length == 2) {
        	int left = stations[0] - w - 1;
			if(left % (w*2 + 1) == 0) {
				answer += left/(w*2 + 1);
			}else {
				answer += left/(w*2 + 1) + 1;
			}
			
			int right = 0;
			if(stations[1] == n) {
				right = n - w;
			}else {
				right = n - stations[1] - w;
				if(right % (w*2 + 1) == 0) {
					answer += right/(w*2 + 1);
				}else {
					answer += right/(w*2 + 1) + 1;
				}
			}
			
			left = stations[0] + w;
			int between = right - left - 1;
			
			if(between <= 0) {
				answer += 0;
			}else {
				if(between % (w*2 + 1) == 0) {
					answer += between/(w*2 + 1);
				}else {
					answer += between/(w*2 + 1) + 1;
				}
			}
			
        }else {
        	for (int i = 0; i < stations.length; i++) {
        		if (i == 0) {
        			int left = stations[i] - w - 1;
        			if(left % (w*2 + 1) == 0) {
        				answer += left/(w*2 + 1);
        			}else {
        				answer += left/(w*2 + 1) + 1;
        			}
        		}else if(i == stations.length - 1) {
        			int right = n - stations[i] - w;
        			if(right % (w*2 + 1) == 0) {
        				answer += right/(w*2 + 1);
        			}else {
        				answer += right/(w*2 + 1) + 1;
        			}
        		}else {
        			int left = stations[i-1] + w;
        			int right = stations[i] - w;
        			int between = right - left - 1;
        			
        			if(between <= 0) {
        				answer += 0;
        			}else {
        				if(between % (w*2 + 1) == 0) {
        					answer += between/(w*2 + 1);
        				}else {
        					answer += between/(w*2 + 1) + 1;
        				}
        			}
        		}
        		
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {

		int[] a = {4,11};
		int[] b = {9};
		
		System.out.println(solution(11,a,1));
		System.out.println(solution(16,b,2));
	}

}
