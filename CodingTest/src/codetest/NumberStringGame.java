package codetest;

import java.util.*;

public class NumberStringGame {

	public static int solution(String s) {
        int answer = 0;
        
        String ans = "";
        
        Map<String, Integer> numbers = new HashMap<String, Integer>();
        numbers.put("zero", 0);
        numbers.put("one", 1);
        numbers.put("two", 2);
        numbers.put("three", 3);
        numbers.put("four", 4);
        numbers.put("five", 5);
        numbers.put("six", 6);
        numbers.put("seven", 7);
        numbers.put("eight", 8);
        numbers.put("nine", 9);
        
        
        String[] temp = s.split("");
        String tempS = "";
        for (int i = 0; i < temp.length; i++) {
        	tempS += temp[i];

        	if(isNumber(tempS)) {
        		ans += tempS;
        		tempS = "";
        	}else if(isStringNumber(numbers, tempS)) {
        		ans += Integer.toString(numbers.get(tempS));
        		tempS = "";
        	}
		}

        answer = Integer.parseInt(ans);
        return answer;
    }
	
	public static boolean isNumber(String s) {
		return s.matches("[+-]?\\d*(\\.\\d+)?");
	}
	
	public static boolean isStringNumber(Map<String, Integer> numbers, String s) {
		return numbers.containsKey(s);
	}
	
	public static void main(String[] args) {

		System.out.println(solution("one4seveneight"));
		System.out.println(solution("23four5six7"));
		System.out.println(solution("2three45sixseven"));
		System.out.println(solution("123"));
		
	}

}
