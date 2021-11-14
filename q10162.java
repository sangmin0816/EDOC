import java.util.*;

public class q10162 { 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        int[] BCA = {60, 10, 5};
        int [] ans = new int[3];

        if(T%5!=0)
            System.out.println(-1);
        else{
            int i=0;
            while(T!=0){
                ans[i]=T/BCA[i];
                T%=BCA[i];
                i++;
            }
            System.out.printf("%d %d %d", ans[2], ans[0], ans[1]);
        }
        sc.close();
    }
}
