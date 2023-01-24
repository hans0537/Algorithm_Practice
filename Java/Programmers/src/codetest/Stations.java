package codetest;

public class Stations {
	public static int solution(int n, int[] stations, int w) {
        int answer = 0;
        int left = 1;
        
        for(int i : stations) {
        	if(left < i - w) {
        		int right = i - w;
        		
        		int length = right - left;
        		
        		if(length % (w*2 + 1) == 0) {
    				answer += length/(w*2 + 1);
    			}else {
    				answer += length/(w*2 + 1) + 1;
    			}
        	}
        	left = i + w + 1;
        }
        
        if(stations[stations.length - 1] + w < n) {
        	left = stations[stations.length - 1] + w;
        	
        	int length = n - left;
        	
        	if(length % (w*2 + 1) == 0) {
				answer += length/(w*2 + 1);
			}else {
				answer += length/(w*2 + 1) + 1;
			}
        }
        return answer;
	}
        	
	
	public static void main(String[] args) {

		int[] a = {4,11};
		int[] b = {9};
		
		System.out.println(solution(11,a,1));
		System.out.println(solution(16,b,2));
		System.out.println(solution(12,new int[] {4,7,11}, 1));
	}

}
