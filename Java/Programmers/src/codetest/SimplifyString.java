package codetest;

public class SimplifyString {

	public static int solution(String s) {
		int answer = s.length();
		
		for (int i = 1; i <= s.length()/2; i++) {
			int count = 1;
			String str1 = s.substring(0,i);
			StringBuilder result = new StringBuilder();
			
			for (int j = i; j <= s.length(); j+=i) {
				String str2 = s.substring(j, j+i >= s.length() ? s.length() : j + i);
				
				if(str2.equals(str1)) count++;
				else {
					result.append((count != 1 ? count : "") + str1);
					str1 = str2;
					count = 1;
				}
			}
			if(i != str1.length()) result.append(str1);
			answer = Math.min(answer, result.toString().length());
		}

		return answer;
	}

	public static void main(String[] args) {

		System.out.println(solution("aabbaccc"));
		System.out.println(solution("ababcdcdababcdcd"));
		System.out.println(solution("abcabcdede"));
		System.out.println(solution("abcabcabcabcdededededede"));
		System.out.println(solution("xababcdcdababcdcd"));

	}

}
