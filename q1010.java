
import java.util.*;

public class q1010 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int t=0; t<T; t++){
            int M = sc.nextInt();
            int N = sc.nextInt();

            int den = 1;
            int num = 1;

            for(int i=N-M+1; i<N+1; i++){
                num*=i;
                den*=M;
                M--;
            }

            System.out.println(num/den);
        }
        
        sc.close();
    }    
}
