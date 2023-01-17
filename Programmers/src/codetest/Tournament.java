package codetest;

public class Tournament {
	
	public static int solution(int n, int a, int b)
    {
        int answer = 0;

        answer = round(answer, n,a,b);
        
        return answer;
    }
	
	public static int round(int answer, int n, int a, int b) {
		answer++;
		
		if((a + 1) / 2 == (b + 1) / 2){
            return answer;
        }
		
        if(a % 2 == 1){
            a = (a+1)/2;
        }else{
            a = a/2;
        }
        
        if(b % 2 == 1){
            b = (b+1)/2;
        }else{
            b = b/2;
        }
        return round(answer, n/2,a,b);
	}
	
	public static void main(String[] args) {

		System.out.println(solution(8,4,7));
	}

}
