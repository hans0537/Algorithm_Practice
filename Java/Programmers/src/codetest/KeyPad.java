package codetest;

public class KeyPad {

	public static String solution(int[] numbers, String hand) {
        String answer = "";
        
        int left = 10;  //"*" 을 10으로 가정
        int right = 12; //"#" 을 12으로 가정
        
        
        for(int i : numbers) {
        	if(i == 1 || i == 4 || i == 7) {
        		answer += "L";
        		left = i;
        	}else if (i == 3 || i == 6 || i == 9) {
        		answer+= "R";
        		right = i;
        	}else {
        		if(i == 0) i = 11; // 0은 11로 가정 
        		
        		if (Math.abs(i - left)/3 + Math.abs(i - left)%3 < Math.abs(i - right)/3 + Math.abs(i - right)%3) {
					answer += "L";
					left = i;
				}else if(Math.abs(i - left)/3 + Math.abs(i - left)%3 == Math.abs(i - right)/3 + Math.abs(i - right)%3) {
					if(hand.equals("left")) {
						answer += "L";
						left = i;
					}else {
						answer += "R";
						right = i;
					}
				}else {
					answer += "R";
					right = i;
				}
        	}
        }
        return answer;
    }
	
	public static void main(String[] args) {
		System.out.println(solution(new int[] {1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5}, "right"));
		System.out.println(solution(new int[] {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2}, "left"));
		System.out.println(solution(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}, "right"));

	}

}
