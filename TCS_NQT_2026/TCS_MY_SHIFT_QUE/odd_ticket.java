package TCS_NQT_2026.TCS_MY_SHIFT_QUE;
import java.util.*;
public class odd_ticket {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int [] arr = new int[n];
        for (int i = 0; i<n;i++){
            arr[i] = sc.nextInt();
        }
        int sum_odd = 0;
        int count = 0;
        for(int num:arr){
            if(num % 2 != 0){
                sum_odd += num;
                count += 1;
            }
        }
        double avg;
        if (count > 0){
            avg = (double) sum_odd / count;
        }
        else{
            avg = 0;
        }
        System.out.println(sum_odd + " " +count +" " + avg);

    }
}
