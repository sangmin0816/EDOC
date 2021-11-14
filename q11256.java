import java.util.*;

public class q11256 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt(); // 테스트 케이스
        for(int i=0; i<T; i++){
            int J = sc.nextInt(); // 사탕 갯수
            int N = sc.nextInt(); // 상자 갯수
            int[] arr = new int[N];
            int ans = 0;

            for(int j=0; j<N; j++){
                //상자 가로 세로 크기
                int R = sc.nextInt();
                int C = sc.nextInt();
                arr[j]=R*C;
            }
            
            Arrays.sort(arr);
            
            for(int j=N-1; j>=0; j--){
                J-=arr[j];
                ans++;
                if(J<=0){
                    System.out.println(ans);
                    break;
                }
            }
        }

        sc.close();
    }
}