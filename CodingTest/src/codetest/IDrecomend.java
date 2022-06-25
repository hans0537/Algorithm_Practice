package codetest;

public class IDrecomend {

	public static String solution(String new_id) {
		String answer = "";

		// 1단계 대문자 => 소문자로 변경
		answer = new_id.toLowerCase();

		// 2단계 "소문자, 숫자, -, _, ." 제외한 모든 문자 제거
		String charsToRemove = "~!@#$%^&*()=+[{]}:?,<>/";
		for(char i : charsToRemove.toCharArray()) {
			answer = answer.replace(String.valueOf(i), "");
		}

		// 3단계 . 2번연속 이상 제거
		while(answer.contains("..")) {
			answer = answer.replace("..", ".");
		}
		
		// 4단계 . 앞과 뒤 제거
		if(answer.charAt(0) == '.') answer = answer.substring(1);
		if(answer.length() != 0 && answer.charAt(answer.length() - 1) == '.') answer = answer.substring(0, answer.length() - 1);
		
		// 5단계 빈문자열 => 'a' 대입
		if(answer.length() == 0) answer += 'a';
		
		// 6단계 16자 이상이면 15자 까지 남기고 제거 (단 제거후 마지막이 . 이면 .도 제거)
		if(answer.length() >= 16) answer = answer.substring(0, 15);
		if(answer.charAt(answer.length() - 1) == '.') answer = answer.substring(0, answer.length() - 1);
		
		// 7단계 2자 이하이면 3자 될때까지 마지막 부분 반복
		while(answer.length() <= 2) {
			answer += answer.charAt(answer.length() - 1);
		}
		
		return answer;
	}

	public static void main(String[] args) {

		System.out.println(solution("...!@BaT#*..y.abcdefghijklm"));
		System.out.println(solution("z-+.^."));
		System.out.println(solution("=.="));
		System.out.println(solution("123_.def"));
		System.out.println(solution("abcdefghijklmn.p"));

	}
}
